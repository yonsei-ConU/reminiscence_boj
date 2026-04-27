from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
passed_turns = 0


def coordinate21(v, h):
    global n, m
    return v + h * n


def coordinate12(x):
    global n, m
    return [x % n, x // n]


g = []
monster_count = 1
chest_count = 0

for i in range(n):
    t = list(input().rstrip())
    if '@' in t:
        z = t.index('@')
        initial_location = [i, z]
        location = [i, z]
    monster_count += t.count('&')
    chest_count += t.count('B')
    g.append(t)

movement = deque(input().rstrip())
info = [0] * (n * m)

for i in range(monster_count):
    t = input().split()
    info[coordinate21(int(t[0]) - 1,
                      int(t[1]) - 1)] = {
                          'name': t[2],
                          'attack': int(t[3]),
                          'defence': int(t[4]),
                          'max_hp': int(t[5]),
                          'cur_hp': int(t[5]),
                          'exp_reward': int(t[6])
                      }

for i in range(chest_count):
    t = input().split()
    try:
        t[3] = int(t[3])
    except ValueError:
        pass
    info[coordinate21(int(t[0]) - 1,
                      int(t[1]) - 1)] = {
                          'type': t[2],
                          'value': t[3]
                      }

last_visited = '.'


def move(r, c):
    global g, n, m
    if 0 <= r < n and 0 <= c < m:
        if g[r][c] == '#':
            return 0, r, c
        return 1, r, c
    else:
        return 0, r, c


player_hp = 20
player_max_hp = 20
player_attack = 2
player_defence = 2
level = 1
exp = 0
wkdtlsrn = []
dx = 0


def spike_trap(r, c):
    global player_hp, g, dx
    dmg_dealt = 5
    if dx:
        dmg_dealt = 1
    if player_hp <= dmg_dealt:
        die('SPIKE TRAP')
        g[r][c] = '^'
    else:
        player_hp -= dmg_dealt


def die(reason):
    global wkdtlsrn
    if 'RE' in wkdtlsrn:
        return reincarnate()
    else:
        game_set(-1, reason)


def reincarnate():
    global wkdtlsrn, g, location, last_visited, player_hp, player_max_hp
    wkdtlsrn.remove('RE')
    g[location[0]][location[1]] = last_visited
    try:
        info[coordinate21(*location)]['cur_hp'] = info[coordinate21(
            *location)]['max_hp']
    except TypeError:
        pass
    g[initial_location[0]][initial_location[1]] = '@'
    location = [initial_location[0], initial_location[1]]
    player_hp = player_max_hp
    last_visited = '.'


weapon_atk = 0
armor_def = 0


def calc_attack(bonus):
    global level
    return 2 * level + bonus


def calc_defence(bonus):
    global level
    return 2 * level + bonus


def win_fight(reward):
    global level, exp, player_max_hp, player_hp, player_attack, player_defence, weapon_atk, armor_def
    exp += reward
    if exp >= level * 5:
        level += 1
        exp = 0
        player_max_hp += 5
        player_hp = player_max_hp
        player_attack = calc_attack(weapon_atk)
        player_defence = calc_defence(armor_def)


def game_set(result, killedby=''):
    global passed_turns, g, level, exp, player_hp, player_max_hp, weapon_atk, armor_def, movement, last_visited, location
    movement = deque()
    if result == -1:
        g[location[0]][location[1]] = last_visited
        player_hp = 0
    for temp in g:
        print(''.join(temp))
    print(f'Passed Turns : {passed_turns}')
    print(f'LV : {level}')
    print(f'HP : {player_hp}/{player_max_hp}')
    print(f'ATT : {2 * level}+{weapon_atk}')
    print(f'DEF : {2 * level}+{armor_def}')
    print(f'EXP : {exp}/{5 * level}')
    if result == 1:
        print('YOU WIN!')
    elif result == -1:
        print(f'YOU HAVE BEEN KILLED BY {killedby}..')
    else:
        print('Press any key to continue.')
    exit()


while movement:
    next_move = movement.popleft()
    r, c = location
    if next_move == 'R':
        t, r_, c_ = move(r, c + 1)
    elif next_move == 'L':
        t, r_, c_ = move(r, c - 1)
    elif next_move == 'U':
        t, r_, c_ = move(r - 1, c)
    else:
        t, r_, c_ = move(r + 1, c)
    if not t:
        if last_visited == '^':
            spike_trap(r, c)
        passed_turns += 1
        continue
    else:
        if last_visited == '^':
            g[r][c] = '^'
        else:
            g[r][c] = '.'
        last_visited = g[r_][c_]
        location = [r_, c_]
        g[r_][c_] = '@'
        if last_visited == '.':
            passed_turns += 1
            continue
        elif last_visited == '^':
            passed_turns += 1
            spike_trap(r_, c_)
        elif last_visited == 'B':
            x = coordinate21(r_, c_)
            y = info[x]
            if y['type'] == 'W':
                weapon_atk = int(y['value'])
                player_attack = calc_attack(weapon_atk)
            elif y['type'] == 'A':
                armor_def = int(y['value'])
                player_defence = calc_defence(armor_def)
            elif y['type'] == 'O':
                z = y['value']
                if z in wkdtlsrn or len(wkdtlsrn) == 4:
                    pass
                else:
                    wkdtlsrn.append(z)
                if z == 'DX':
                    dx = 1
            last_visited = '.'
            passed_turns += 1
        elif last_visited in ['&', 'M']:
            passed_turns += 1
            x = coordinate21(r_, c_)
            y = info[x]
            z = 0
            if 'HU' in wkdtlsrn and last_visited == 'M':
                player_hp = player_max_hp
            while True:
                if z == 0 and 'CO' in wkdtlsrn:
                    y['cur_hp'] -= max(1,
                                       (2 + dx) * player_attack - y['defence'])
                else:
                    y['cur_hp'] -= max(1, player_attack - y['defence'])
                if y['cur_hp'] <= 0:
                    reward = y['exp_reward']
                    if 'EX' in wkdtlsrn:
                        reward = reward * 6 // 5
                    win_fight(reward)
                    if 'HR' in wkdtlsrn:
                        player_hp = min(player_max_hp, player_hp + 3)
                    if last_visited == 'M':
                        game_set(1)
                    last_visited = '.'
                    break
                if z == 0 and 'HU' in wkdtlsrn and last_visited == 'M':
                    pass
                else:
                    player_hp -= max(1, y['attack'] - player_defence)
                if player_hp <= 0:
                    die(y['name'])
                    break
                z += 1

game_set(0)
