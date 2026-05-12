import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


tc = 1
print_people = ['divine.', 'human.', 'evil.']
print_daynight = ['day.', 'night.']
while True:
    n = int(input_())
    if not n: break
    conversation = []
    for i in range(n):
        z = input_().split()
        tmp = [ord(z[0][0]) - 65]
        if z[1] == 'It':
            tmp = [1] + tmp
            time = z[3]
            if time == 'day.':
                tmp.append(0)
            else:
                assert time == 'night.'
                tmp.append(1)
        else:
            tmp = [2] + tmp
            if z[1] == 'I':
                tmp.append(ord(z[0][0]) - 65)
            else:
                tmp.append(ord(z[1]) - 65)
            t = z[-1]
            if t == 'divine.':
                tmp.append(0)
            elif t == 'human.':
                tmp.append(1)
            elif t == 'evil.':
                tmp.append(2)
            else:
                assert t == 'lying.'
                tmp.append(False)
            if z[3] == 'not':
                tmp.append(False)
            else:
                tmp.append(True)
        conversation.append(tmp)

    # 모든 상태마다 n개의 쿼리가 들어옴

    # 1번 쿼리는 `1 a b`의 형태로 주어짐
    # a는 말한 사람, b가 0이면 낮, b가 1이면 밤

    # 2번 쿼리는 `2 a b c d`의 형태로 주어짐
    # a는 말한 사람, b는 타겟
    # c가 0이면 divine, 1이면 human, 2이면 evil, False이면 lying
    # c가 False면 저 말이 거짓이어야 함

    ans = []
    for a in range(3):
     for b in range(3):
      for c in range(3):
       for d in range(3):
        for e in range(3):
         for daynight in range(2):
             lst = [a, b, c, d, e, daynight]
             tf = [True] * 5
             for i in range(5):
                 if lst[i] == 0:  # a가 divine인 경우 밤낮과 상관없이 참을 말해야 함
                     tf[i] = True
                 elif lst[i] == 1 and daynight == 0:  # a가 human이고 낮인 경우
                     tf[i] = True
                 elif lst[i] == 1 and daynight == 1:  # a가 human이고 밤인 경우
                     tf[i] = False
                 else:  # a가 evil인 경우
                     tf[i] = False
             chk = True
             for query in conversation:
                 if query[0] == 1:
                     p, q = query[1:]
                     if not tf[p] ^ q ^ daynight:  # q ^ daynight이 1이면 거짓말한거임
                         chk = False
                         break
                 else:
                     p, q, r, s = query[1:]
                     # lst[q] == r이면 참인진술
                     if lst[q] == False:
                         t = tf[q]
                     else:
                         t = (lst[q] == r)
                     if not tf[p] ^ t ^ s:
                         chk = False
                         break
             if chk:
                 ans.append(lst)

    print(f"Conversation #{tc}")
    if not ans:
        print("This is impossible.")
    else:
        a = b = c = d = e = f = -1
        ac = bc = cc = dc = ec = fc = 1
        for at, bt, ct, dt, et, ft in ans:
            if a == -1:
                a, b, c, d, e, f = at, bt, ct, dt, et, ft
            else:
                if a != at:
                    ac = 0
                if b != bt:
                    bc = 0
                if c != ct:
                    cc = 0
                if d != dt:
                    dc = 0
                if e != et:
                    ec = 0
                if f != ft:
                    fc = 0
        if not (ac + bc + cc + dc + ec + fc):
            print("No facts are deducible.")
        else:
            if ac:
                print(f"A is {print_people[a]}")
            if bc:
                print(f"B is {print_people[b]}")
            if cc:
                print(f"C is {print_people[c]}")
            if dc:
                print(f"D is {print_people[d]}")
            if ec:
                print(f"E is {print_people[e]}")
            if fc:
                print(f"It is {print_daynight[f]}")
    tc += 1
