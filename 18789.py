from random import choice, randint, random, shuffle
from sys import setrecursionlimit, stdin
from collections import deque
import math

input_ = stdin.readline


def minput():
    return map(int, input_().split())


setrecursionlimit(1000000)


def get_adjacent_indices(index, columns=14, total_cells=112):
    adjacent = []
    row, col = divmod(index, columns)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < total_cells // columns and 0 <= new_col < columns:
            adjacent_index = new_row * columns + new_col
            adjacent.append(adjacent_index)
    return adjacent


def get_indices_with_value(value, grid):
    return [i for i, v in enumerate(grid) if v == value]


def get_next_indices(current_value, next_value, current_indices, grid):
    next_indices = []
    for index in current_indices:
        neighbors = get_adjacent_indices(index)
        matching_neighbors = [n for n in neighbors if grid[n] == next_value]
        next_indices.extend(matching_neighbors)
    return next_indices


def find_max_constructible_number(grid):
    # 여기서는 원래 코드 로직 그대로 사용
    # 더 효율적으로 만들려면 이진 탐색 등을 사용할 수 있음
    for num in range(10, 8141):
        digits = deque(map(int, str(num)))
        current_indices = get_indices_with_value(digits[0], grid)
        for k in range(len(digits) - 1):
            current_digit = digits[k]
            next_digit = digits[k + 1]
            current_indices = get_next_indices(current_digit, next_digit, current_indices, grid)
            if not current_indices:
                break
        else:
            continue
        return num - 1
    return 8140


def generate_neighbor(grid, rows=8, columns=14):
    """
    기존 방식: 하나의 셀 값을 변경
    개선된 방식: 몇 가지 전략 중 랜덤하게 선택
    1. 하나의 셀 값 변경
    2. 두 개의 셀 값 서로 교환
    3. 일정 확률로 여러 셀(2~3개) 변경
    """
    new_grid = grid[:]
    action = random()
    length = rows * columns

    if action < 0.5:
        # 하나의 셀 값 변경
        idx = randint(0, length - 1)
        new_grid[idx] = choice(range(10))
    elif action < 0.75:
        # 두 개의 셀 값 서로 교환
        idx1 = randint(0, length - 1)
        idx2 = randint(0, length - 1)
        new_grid[idx1], new_grid[idx2] = new_grid[idx2], new_grid[idx1]
    else:
        # 여러 셀 변경(2~3개 랜덤 선택)
        count = randint(2, 3)
        indices = [randint(0, length - 1) for _ in range(count)]
        for i in indices:
            new_grid[i] = choice(range(10))
    return new_grid


def simulated_annealing(grid, initial_score,
                        rows=8, columns=14,
                        initial_temp=100.0,
                        cooling_rate=0.99,
                        iterations=10000,
                        no_improve_limit=1000,
                        reheat_factor=2.0):
    best_grid = grid[:]
    best_score = initial_score

    current_grid = grid[:]
    current_score = initial_score

    temperature = initial_temp
    no_improvement_count = 0

    for i in range(iterations):
        neighbor = generate_neighbor(current_grid, rows, columns)
        new_score = find_max_constructible_number(neighbor)

        if new_score > current_score:
            current_grid = neighbor
            current_score = new_score
            # 최고 점수 갱신
            if new_score > best_score:
                best_score = new_score
                best_grid = neighbor[:]
                no_improvement_count = 0
            else:
                no_improvement_count += 1
        else:
            # 점수가 나빠진 경우 확률적으로 수용
            delta = new_score - current_score
            acceptance_prob = math.exp(delta / temperature) if temperature > 1e-9 else 0
            if random() < acceptance_prob:
                current_grid = neighbor
                current_score = new_score
                no_improvement_count += 1
            else:
                no_improvement_count += 1

        # 일정 횟수 이상 개선 없으면 reheat
        if no_improvement_count > no_improve_limit:
            temperature *= reheat_factor
            no_improvement_count = 0
            # 옵션: 최적해로 되돌아갈 수도 있음
            # current_grid = best_grid[:]
            # current_score = best_score

        # 냉각, 개선도가 없으면 cooling rate 약간 변화(여기서는 간단히)
        if no_improvement_count > no_improve_limit // 2:
            # 개선 적으면 온도 낮추는 속도를 조금 늦춘다
            temperature *= (cooling_rate + 0.001)
        else:
            temperature *= cooling_rate

        if not i % 250:
            print(f"Iteration {i}: Best={best_score}, Current={current_score}, Temp={temperature}")

    return best_grid, best_score


def main():
    grid = list(map(int, list(input_().rstrip())))
    max_number = find_max_constructible_number(grid)
    print("Initial:", max_number)
    best_grid, best_score = simulated_annealing(grid, max_number)
    print("After simulated annealing:", best_score)
    print(''.join(map(str, best_grid)))


if __name__ == "__main__":
    main()
8716209573392961037117210612668945198052809878213021884531430290475345541951799631910685078715621226926416547474
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111