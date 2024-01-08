game_state = [[0 for _ in range(9)] for _ in range(9)]
previous_states = []
groups = []

class Group:
    def __init__(self, owner, stones):
        self.owner = owner
        self.stones = []
        for stone in stones:
            self.stones.append(stone)

    def get_merged(self, other_group) -> ['Group']:
        """
        Merges the current group with another group.
        Args:
            other_group: the group to be merged with the current group
        Returns:
            a new group containing all the stones from both groups
        """
        new_group = Group(self.owner, self.stones)
        for stone in other_group.stones:
            new_group.stones.append(stone)
        return new_group

    def compute_liberties(self, game_state) -> int:
        """
        Computes the number of liberties of the current group in the given game_state.
        Args:
            game_state: the game state to be analyzed
        Returns:
            the number of liberties of the current group
        """
        liberties = 0
        for stone in self.stones:
            row, col = stone
            adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for r, c in adjacent_positions:
                if 0 <= r < len(game_state) and 0 <= c < len(game_state[0]):
                    if r < 0 or r >= len(game_state) or c < 0 or c >= len(game_state[0]):
                        continue
                    if game_state[r][c] == 0:
                        liberties += 1
        return liberties

    def __str__(self):
        return f"{self.owner}\n{self.stones}"

def insert_stone(row, col, player):
    """
    Inserts a stone in the game state.
    Args:
        row: the row where the stone is to be inserted
        col: the column where the stone is to be inserted
        player: the player who inserts the stone
    """
    game_state[row][col] = player

    new_group = Group(player, [(row, col)])
    groups.append(new_group)

    adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in adjacent_positions

print(groups[0])