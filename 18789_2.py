from random import choice, randint, random
from sys import setrecursionlimit, stdin
from collections import deque
import math
input_ = stdin.readline
def minput(): return map(int, input_().split())

# 재귀 제한을 늘립니다.
setrecursionlimit(1000000)


def get_adjacent_indices(index, columns=14, total_cells=112):
    """
    주어진 인덱스의 인접한 셀들의 인덱스를 반환합니다.
    대각선과 직교 방향의 이웃을 고려합니다.

    Args:
        index (int): 현재 셀의 인덱스.
        columns (int): 한 행의 셀 수.
        total_cells (int): 전체 셀의 수.

    Returns:
        list: 인접한 셀들의 인덱스 리스트.
    """
    adjacent = []
    row, col = divmod(index, columns)

    # 8가지 방향 (대각선 포함)
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
    """
    그리드에서 특정 값과 일치하는 모든 인덱스를 반환합니다.

    Args:
        value (int): 찾고자 하는 값.
        grid (list): 숫자로 이루어진 그리드.

    Returns:
        list: 값과 일치하는 셀의 인덱스 리스트.
    """
    return [index for index, cell_value in enumerate(grid) if cell_value == value]


def get_next_indices(current_value, next_value, current_indices, grid):
    """
    현재 값의 인덱스에서 다음 값과 일치하는 인접 셀의 인덱스를 찾습니다.

    Args:
        current_value (int): 현재 숫자.
        next_value (int): 다음 숫자.
        current_indices (list): 현재 숫자가 위치한 인덱스 리스트.
        grid (list): 숫자로 이루어진 그리드.

    Returns:
        list: 다음 숫자가 위치할 수 있는 인접 셀의 인덱스 리스트.
    """
    next_indices = []
    for index in current_indices:
        neighbors = get_adjacent_indices(index)
        matching_neighbors = [n for n in neighbors if grid[n] == next_value]
        next_indices.extend(matching_neighbors)
    return next_indices


def find_max_constructible_number(grid):
    """
    그리드에서 인접한 셀을 따라 숫자를 이어가며 만들 수 있는 최대 숫자를 찾습니다.
    최대 숫자는 8140 이하입니다.

    Args:
        grid (list): 숫자로 이루어진 그리드.

    Returns:
        int: 만들 수 있는 최대 숫자.
    """
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
            # 모든 자릿수가 연결되었음
            continue
        # 연결되지 않은 경우 이전 숫자를 반환
        return num - 1
    return 8140


def generate_grid(rows=8, columns=14):
    """
    주어진 행과 열의 크기로 랜덤한 숫자 그리드를 생성합니다.

    Args:
        rows (int): 그리드의 행 수.
        columns (int): 그리드의 열 수.

    Returns:
        list: 생성된 그리드.
    """
    return [choice(range(10)) for _ in range(rows * columns)]


def simulated_annealing(grid, initial_score,
                        rows=8, columns=14,
                        initial_temp=100.0,
                        cooling_rate=0.99,
                        iterations=10000):
    """
    간단한 담금질 기법을 적용하여 그리드를 개선하려고 시도합니다.

    Args:
        initial_score (int): 초기 그리드 점수.
        rows (int): 그리드의 행 수.
        columns (int): 그리드의 열 수.
        initial_temp (float): 초기 온도.
        cooling_rate (float): 온도 감소율.
        iterations (int): 담금질 반복 횟수.

    Returns:
        (best_grid, best_score): 담금질 후의 최고 점수와 그 그리드.
    """
    best_grid = grid[:]
    best_score = initial_score

    current_grid = grid[:]
    current_score = initial_score

    temperature = initial_temp

    for i in range(iterations):
        # 그리드 중 하나의 셀을 골라 값을 바꾼다.
        # 무작위 인덱스 선택 후 새로운 값을 할당
        idx = randint(0, rows * columns - 1)
        old_value = current_grid[idx]
        new_value = choice(range(10))
        current_grid[idx] = new_value

        new_score = find_max_constructible_number(current_grid)

        # 점수 개선
        if new_score > current_score:
            current_score = new_score
            # 최고 점수 갱신
            if new_score > best_score:
                best_score = new_score
                best_grid = current_grid[:]
        else:
            # 개선되지 않은 경우 확률적으로 수용
            # 확률 = exp((new_score - current_score) / temperature)
            delta = new_score - current_score
            acceptance_prob = math.exp(delta / temperature) if temperature > 0 else 0
            if random() < acceptance_prob:
                current_score = new_score
            else:
                # 되돌린다.
                current_grid[idx] = old_value

        # 온도 감소
        temperature *= cooling_rate
        if not i % 250:
            print(f"Iteration {i}: Best={best_score}, Current={current_score}, Temp={temperature}")

    return best_grid, best_score


def main():
    grid = list(map(int, list(input_().rstrip())))
    max_number = find_max_constructible_number(grid)
    print(max_number)
    # 담금질 기법 적용
    best_grid, best_score = simulated_annealing(grid, max_number)
    print("After simulated annealing:", best_score)
    print(''.join(map(str, best_grid)))


if __name__ == "__main__":
    main()