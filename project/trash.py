def calculate_score(game_state):
    def is_valid(i, j):
        return 0 <= i < 9 and 0 <= j < 9

    def flood_fill(i, j):
        stack = [(i, j)]
        region = {(i, j)}
        touches_border = False
        border_touches = set()
        while stack:
            i, j = stack.pop()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if is_valid(x, y):
                    if game_state[x][y] == 0 and (x, y) not in region:
                        region.add((x, y))
                        stack.append((x, y))
                    elif game_state[x][y] != 0:
                        touches_border = True
                        border_touches.add((x, y))
        return region if not (touches_border and len(region) > len(border_touches)) else set()

    def get_surrounding_stones(region):
        surrounding_stones = set()
        for i, j in region:
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if is_valid(x, y) and game_state[x][y] != 0:
                    surrounding_stones.add(game_state[x][y])
        return surrounding_stones

    score = [0, 0]
    visited = [[False] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if game_state[i][j] == 0 and not visited[i][j]:
                region = flood_fill(i, j)
                for x, y in region:
                    visited[x][y] = True
                surrounding_stones = get_surrounding_stones(region)
                if len(surrounding_stones) == 1:
                    player = surrounding_stones.pop()
                    score[player - 1] += len(region)
    return tuple(score)


# Example usage:
game_state_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

game_state_2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

game_state_3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

game_state_4 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 2, 2, 0],
    [0, 0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
]

game_state_5 = [
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 1, 0, 1, 0, 0, 2, 2, 0],
    [0, 0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
]

game_state_6 = [
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 2],
    [0, 1, 0, 1, 0, 0, 2, 2, 0],
    [0, 0, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [2, 2, 0, 0, 0, 0, 0, 1, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 1],
]

game_state_7 = [
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

result1 = calculate_score(game_state_1)
result2 = calculate_score(game_state_2)
result3 = calculate_score(game_state_3)
result4 = calculate_score(game_state_4)
result5 = calculate_score(game_state_5)
result6 = calculate_score(game_state_6)
result7 = calculate_score(game_state_7)
print(result1, result2, result3, result4, result5, result6, result7)
