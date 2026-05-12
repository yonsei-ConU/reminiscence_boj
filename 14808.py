import sys
from algorithms import floyd_warshall
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    N, Q = minput()
    horses = [list(minput()) for _ in range(N)]
    g = [list(map(lambda x: int(x) if x != '-1' else 10 ** 18, input_().split())) for _ in range(N)]

    # STEP 1: calcluate shortest path between cities
    dist = floyd_warshall(g)
    # STEP 2: construct a new graph representing the shortest time
    g2 = []
    for i in range(N):
        tmp = []
        for j in range(N):
            if dist[i][j] <= horses[i][0]:
                tmp.append(dist[i][j] / horses[i][1])
            else:
                tmp.append(float('inf'))
        g2.append(tmp)
    # STEP 3: calcluate shortest time between cities
    ans = floyd_warshall(g2)

    output = []
    for _ in range(Q):
        U, V = minput()
        U -= 1; V -= 1
        output.append(str(ans[U][V]))

    print(f"Case #{tc}: {' '.join(output)}")
"""
sol
**Short answer:**  
Perform two Floyd-Warshall computations. First, run Floyd-Warshall on the given distances to find the shortest distance between every pair of cities. Then, use these shortest distances to build a time matrix that represents the best possible travel times starting with each city’s horse and potentially switching horses along the way. Run Floyd-Warshall again on this time matrix to account for intermediate horse changes. Finally, answer each query from this precomputed matrix.

---

**Detailed explanation:**

1. **Understanding the problem**  
   You have \( N \) cities, each with a horse that has two attributes:  
   - \( E_i \): The maximum distance this horse can travel before it gets too tired.
   - \( S_i \): The speed of the horse (distance per hour).

   You also have routes between cities with given distances \( D_{ij} \) (or \(-1\) if no direct route exists). After computing routes, you need to answer queries of the form: "What is the fastest time to get from city \( U \) to city \( V \)?"

   Key points:
   - You start at city \( U \) with city \( U \)’s horse.
   - At each city you reach, you may instantly switch to that city’s horse.
   - A horse’s maximum distance \( E_i \) is a hard cap on how far it can go before you must switch or stop.
   - Travel times are affected by possibly switching horses multiple times.
   - The graph is not necessarily symmetric, and might not follow the triangle inequality.  

2. **First challenge: shortest distances**  
   You are given direct distances \( D_{ij} \), which may be \(-1\) if no direct route exists. You need the shortest distances between all pairs of cities. This is a classic all-pairs shortest path problem.

   **Step 1: Compute shortest paths using Floyd-Warshall**
   - Initialize a distance matrix \(\text{dist}\) with:
     \[
     \text{dist}[i][j] = 
     \begin{cases}
     D_{ij}, & \text{if } D_{ij} \geq 0 \\
     \infty, & \text{otherwise} \\
     \end{cases}
     \]
     and \(\text{dist}[i][i] = 0\) for all \( i \).
     
   - Run Floyd-Warshall:
     \[
     \text{for } k = 1 \text{ to } N:\quad
       \text{for } i = 1 \text{ to } N:\quad
         \text{for } j = 1 \text{ to } N:\quad
           \text{dist}[i][j] = \min(\text{dist}[i][j], \text{dist}[i][k] + \text{dist}[k][j])
     \]
   
   After this, \(\text{dist}[i][j]\) will hold the shortest possible distance between cities \( i \) and \( j \).

3. **Second challenge: considering horse limits and speeds**  
   For each city \( i \), you have a horse with range \( E_i \) and speed \( S_i \). If you start in city \( i \) on that horse, you can only travel directly to city \( j \) if:
   \[
   \text{dist}[i][j] \leq E_i
   \]
   If that’s true, you can go directly from \( i \) to \( j \) using city \( i \)’s horse in:
   \[
   \text{time} = \frac{\text{dist}[i][j]}{S_i}
   \]
   If \(\text{dist}[i][j] > E_i\), you cannot directly travel on city \( i \)’s horse alone. Initially, let’s only consider direct rides from the starting city’s horse, without any intermediate changes.

   **Step 2: Construct initial time matrix**
   Create a matrix \( T \) where:
   \[
   T[i][j] = 
     \begin{cases}
     \frac{\text{dist}[i][j]}{S_i}, & \text{if } \text{dist}[i][j] \leq E_i \\
     \infty, & \text{otherwise}
     \end{cases}
   \]

   At this point, \( T[i][j] \) represents the minimum time to go **directly** from city \( i \) to city \( j \) **if you only use the horse from city i** and never switch.

4. **Third challenge: allowing horse switches**  
   The problem allows you to switch horses at intermediate cities. Suppose you want to go from city \( i \) to city \( j \), and you consider stopping at some city \( k \) along the way:
   - Travel from \( i \) to \( k \) on city \( i \)’s horse (time: \( T[i][k] \)).
   - At city \( k \), switch to city \( k \)’s horse instantly.
   - Then from city \( k \) to city \( j \), you now start fresh with city \( k \)’s horse, so the time needed is \( T[k][j] \) (as if starting a new journey with city \( k \) as the origin).

   Notice something important: after you’ve computed \( T[i][j] \) with the direct criterion, you can run Floyd-Warshall again on the \( T \) matrix to incorporate these "switching" opportunities. Why does this work?

   Initially, \( T[i][j] \) only accounts for direct travel from \( i \) using \( i \)’s horse. But if we do:
   \[
   T[i][j] = \min_{k}( T[i][k] + T[k][j] )
   \]
   On the right-hand side, \( T[k][j] \) is computed from the perspective of starting at \( k \) (using \( k \)’s horse initially). Adding them together simulates:
   - Going from \( i \) to \( k \) with horse \( i \)
   - Switching at \( k \) (now we can think of starting anew with \( k \)’s horse)
   - Then going from \( k \) to \( j \) using \( k \)’s horse.

   By applying Floyd-Warshall to \( T \), you allow any number of intermediate switches at any city. After this step, \( T[i][j] \) truly represents the minimal time to travel from city \( i \) to city \( j \) starting on city \( i \)’s horse and switching optimally along the way.

   **Step 3: Run Floyd-Warshall on the time matrix**
   \[
   \text{for } k = 1 \text{ to } N:\quad
     \text{for } i = 1 \text{ to } N:\quad
       \text{for } j = 1 \text{ to } N:\quad
         T[i][j] = \min(T[i][j], T[i][k] + T[k][j])
   \]

5. **Answering queries**  
   After these steps:
   - \( T[i][j] \) is the minimal travel time starting at city \( i \)’s horse, with unlimited switching allowed, to reach city \( j \).

   For each query \((U_k, V_k)\), the answer is simply:
   \[
   \text{answer} = T[U_k][V_k]
   \]

   Because you always start on the horse of the starting city \( U_k \).

6. **Complexity considerations**  
   - Floyd-Warshall on \( N \) cities is \( O(N^3) \). With \( N \leq 100 \), this is manageable.
   - You do Floyd-Warshall twice. That is still \( O(N^3) \) and acceptable given the constraints.
   - Answering each query afterward is just \( O(1) \).

7. **Summary of the solution steps**:
   1. Use Floyd-Warshall on the input \( D \)-matrix to get shortest distances \(\text{dist}[i][j]\).
   2. Construct \( T[i][j] \) using the conditions \(\text{dist}[i][j]\) and \( E_i, S_i \).
   3. Apply Floyd-Warshall again on \( T \) to account for switching horses.
   4. Answer queries from the final \( T \) matrix.

---

**In conclusion:**  
This problem can be solved by first finding shortest distances between every pair of cities, then building and refining a time matrix that accounts for travel limits and speeds of horses by running Floyd-Warshall twice. The second run of Floyd-Warshall on the time matrix enables considering all possible intermediate horse switches implicitly.

When you first read the problem, it might feel a bit complicated because it involves two layers of constraints:

Distances between cities: You need to know how far apart the cities are to figure out travel times.
Horses with limited range and fixed speed: Even if you know the distance between two cities, you can’t necessarily just hop on a horse and go. A horse can only travel a certain total distance before it must stop, and you can switch horses only when you reach another city.
So how does one naturally arrive at the "Second challenge" idea?

Initial Human Thought Process:

Start with what you know best:
You know how to find shortest paths between cities: that’s a standard problem. Even if some direct connections are missing or distances are odd, the Floyd-Warshall algorithm will give you a neat matrix of shortest distances between every pair of cities. It’s a logical first step—"If I know the shortest distances, I at least have a baseline understanding of the geography."
The twist—each city has a unique horse with limitations:
Once you have these shortest distances, the next question is: "How do I model the fact that I can start with a certain horse that can only go so far?" A natural way to think about it is:
If I start in city 
i
i, I have city 
i
i’s horse. This horse has a maximum range 
E
i
E 
i
​	
 . That means from city 
i
i, I can only directly reach those cities 
j
j for which the shortest distance
dist
[
i
]
[
j
]
dist[i][j] is less than or equal to 
E
i
E 
i
​	
 .
If I can reach city 
j
j directly from city 
i
i with city 
i
i’s horse, the time is simply 
dist
[
i
]
[
j
]
/
S
i
dist[i][j]/S 
i
​	
 . If I cannot, there’s no direct "one-hop" way to get there on city 
i
i’s horse.
From distances to times with a single horse: Now, you’ve got a kind of "time-to-travel" matrix that only considers traveling straight from your starting city’s horse to another city with no intermediate switches. This is simpler. You’re basically saying: "If I never switch horses, what cities are reachable and how long does it take?" This step clarifies the problem. You’ve taken the complicated idea of switching at multiple stops and momentarily ignored it, focusing just on the initial jump out of each city with that city’s horse.
Relating this back to well-known shortest-path logic: Once you’ve got this "direct travel time" idea, your intuition from pathfinding problems suggests: "Wait, but what if I consider using a city 
k
k as a stepping stone? At city 
k
k, I can grab a fresh horse that can again travel a certain maximum distance, possibly getting me further or faster than if I stuck with my original horse." This is exactly what another shortest-path algorithm does—Floyd-Warshall checks if a path through an intermediate node 
k
k improves your route.
Seeing the pattern: The key insight is recognizing that switching horses is just like having a new "start condition" at an intermediate node. Initially, your time matrix only accounts for travel starting with city 
i
i’s horse. But after one intermediate step, you might as well be "starting over" from city 
k
k with 
k
k’s horse. This is precisely what a second application of Floyd-Warshall (or a similar all-pairs consideration) can capture. It effectively says:
"The best time to get from 
i
i to 
j
j might be improved if you first go from 
i
i to 
k
k (on the 
i
i-horse), then switch at 
k
k (now treat 
k
k as a starting point with 
k
k-horse), and then go from
k
k to 
j
j."
Doing this repeatedly for all 
k
k gives you the minimal possible time incorporating any number of switches.
In other words, the main idea behind the "Second challenge" part is:

Start small: Convert your shortest path distances into a time matrix that assumes you never switch horses.
Then recognize that switching horses at intermediate stops can be modeled as an all-pairs shortest path problem on this new "time graph."
By running Floyd-Warshall again, you let the algorithm automatically consider all sequences of horse changes, just as it considers all intermediate nodes in a normal shortest-path problem.
Flow of the idea:

Get shortest distances → This sets the stage.
From distances, figure out direct travel times using the horse from the starting city only → This breaks the problem into simpler subproblems and gives you a baseline.
Reapply shortest-path logic (like Floyd-Warshall) on the time matrix → This leverages your existing shortest-path toolkit to handle the complexity of switching horses, turning a seemingly complicated scenario into something solvable by a known algorithmic pattern.
This "Aha!" moment comes from noticing the structural similarity: both shortest travel time (with switching) and shortest distance problems are about combining partial routes optimally. Once you see that switching horses can be treated just like adding another level of shortest-path computation, the rest falls into place.
"""