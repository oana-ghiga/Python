def calculate_score(game_state):
    def is_valid(i, j):
        return 0 <= i < 9 and 0 <= j < 9

    def dfs(i, j, player):
        if not is_valid(i, j) or visited[i][j] or game_state[i][j] != 0:
            return False
        visited[i][j] = True
        territory[player].append((i, j))
        result = True
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            result &= dfs(x, y, player)
        return result

    score = [0, 0]
    visited = [[False] * 9 for _ in range(9)]
    territory = {1: [], 2: []}

    for i in range(9):
        for j in range(9):
            if game_state[i][j] == 0 and not visited[i][j]:
                for player in [1, 2]:
                    if dfs(i, j, player):
                        if len(territory[player]) > len(territory[3 - player]):
                            score[player - 1] += len(territory[player])
                        territory[player] = []
                        territory[3 - player] = []
                        break

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

result1 = calculate_score(game_state_1)
result2 = calculate_score(game_state_2)
result3 = calculate_score(game_state_3)
print(result1, result2, result3)
