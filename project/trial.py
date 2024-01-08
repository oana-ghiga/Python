import pygame

Screen_Width = 1000
Screen_Height = 1000

Black = (0, 0, 0)
White = (255, 255, 255)

game_state = [[0 for _ in range(9)] for _ in range(9)]
previous_states = []
groups = []

# Creating buttons for the main menu
BTN_SIZE = 62
X_OFFSET = 375
Y_OFFSET = 200
x_offset = 30
y_offset = 70
PIECE_SIZE = 50
RADIUS = 25
CELL_WIDTH = 100
CELL_HEIGHT = 100

# Define the size of the grid
grid_size_x = 9
grid_size_y = 9
initial_point = (231, 214)
cell_width = 67
cell_height = 67


def compare(game_state1: list[list[int]], game_state2: list[list[int]]) -> bool:
    """
    Compares two game states.
    Args:
        game_state1:
        game_state2:

    Returns:
        True if the game states are the same, False otherwise
    """
    for row1, row2 in zip(game_state1, game_state2):
        for cell1, cell2 in zip(row1, row2):
            if cell1 != cell2:
                return False
    return True


def was_seen_before(game_state: list[list[int]]) -> bool:
    """
    Checks if the current game state has already been seen before.
    Args:
        game_state: the new game state (the one we want to insert)
    Returns:
        True if the game state has already been seen before, False otherwise
    """
    for prev_state in previous_states:
        if compare(game_state, prev_state):
            return True
    return False


def copy_game_state(game_state) -> list[list[int]]:
    """
    Creates a deep copy of the game state matrix.
    Args:
        game_state: the matrix to be copied

    Returns:
        game_state_copy: a deep copy of the game state matrix
    """
    new_game_state = []
    for row in game_state:
        new_game_state.append(row[:])
    return new_game_state


# Generate the 81 intersections
def generate_intersections(grid_size_x, grid_size_y, initial_point, cell_width, cell_height) -> list[tuple[int, int]]:
    """
    Generates the 81 intersections of the game board.
    Args:
        grid_size_x: width of the grid
        grid_size_y: height of the grid
        initial_point: coordinates of the top left intersection
        cell_width: x distance between two adjacent intersections
        cell_height: y distance between two adjacent intersections

    Returns:
        intersections: a list of 81 tuples, each tuple representing an intersection
    """
    intersections = []
    x, y = initial_point

    for i in range(grid_size_x):
        for j in range(grid_size_y):
            intersection = (x + i * cell_width, y + j * cell_height)
            intersections.append(intersection)

    return intersections


# Generate the specific 81 intersections
specific_intersections = generate_intersections(grid_size_x, grid_size_y, initial_point, cell_width, cell_height)

pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
clock = pygame.time.Clock()
lobby_image = pygame.image.load('img/lobby.png')
lobby_image = pygame.transform.scale(lobby_image, (Screen_Width, Screen_Height))
board_image = pygame.image.load('img/board.png')
board_image = pygame.transform.scale(board_image, (Screen_Width, Screen_Height))
rules_go_image = pygame.image.load('img/rules_go.png')
rules_go_image = pygame.transform.scale(rules_go_image, (Screen_Width, Screen_Height))
black_piece_image = pygame.image.load('img/black.png')
black_piece_image = pygame.transform.scale(black_piece_image, (50, 50))
white_piece_image = pygame.image.load('img/white.png')
white_piece_image = pygame.transform.scale(white_piece_image, (50, 50))
black_won=pygame.image.load('img/black_won.png')
black_won=pygame.transform.scale(black_won, (Screen_Width, Screen_Height))
white_won=pygame.image.load('img/white_won.png')
white_won=pygame.transform.scale(white_won, (Screen_Width, Screen_Height))


def insert_stone(row, col, player):
    """
    Inserts a stone in the game state.
    Args:
        row: the row (in the matrix) where the stone is to be inserted
        col: the column (in the matrix) where the stone is to be inserted
        player: the player who inserts the stone
    """
    game_state[row][col] = player

    new_group = Group(player, [(row, col)])

    adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in adjacent_positions:
        if r < 0 or r >= len(game_state) or c < 0 or c >= len(game_state[0]):
            continue
        if game_state[r][c] == player:
            for group in groups:
                if (r, c) in group and group.owner == player:
                    new_group = new_group.get_merged(group)
                    groups.remove(group)
                    break
    groups.append(new_group)


def place_black_piece(x, y, intersections, game_state):
    """
    Renders a black piece on the board at the closest intersection to the mouse position.
    Args:
        x: x coordinate of the mouse position
        y: y coordinate of the mouse position
        intersections:
        game_state:

    Returns:

    """
    closest_intersection = calculate_closest_intersection((x, y), intersections)
    if closest_intersection:
        row = intersections.index(closest_intersection) // 9
        col = intersections.index(closest_intersection) % 9
        if game_state[row][col] == 0:
            screen.blit(black_piece_image,
                        (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
            insert_stone(row, col, 1)
            print(f"Player 1 placed a piece at {closest_intersection}")
        else:
            print("Invalid position for Player 1")
    else:
        print("Invalid position for Player 1")


def place_white_piece(x, y, intersections, game_state):
    closest_intersection = calculate_closest_intersection((x, y), intersections)
    if closest_intersection:
        row = intersections.index(closest_intersection) // 9
        col = intersections.index(closest_intersection) % 9
        if game_state[row][col] == 0:
            screen.blit(white_piece_image,
                        (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
            insert_stone(row, col, 2)
            print(f"Player 2 placed a piece at {closest_intersection}")
        else:
            print("Invalid position for Player 2")
    else:
        print("Invalid position for Player 2")


class Button:
    def __init__(self, rect, image_path):
        self.btn_rect = rect
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.is_active = True
        self.is_pressed = False

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_active:
            if event.button == 1 and self.btn_rect.collidepoint(event.pos):
                self.is_pressed = True
                print(f"Button {self.image_path} pressed at {event.pos}")

    def draw(self):
        screen.blit(self.image, self.btn_rect)


buttons = []
button_names = ["pvp.png", "pvai.png", "rules.png", "quit.png"]
num_buttons = len(button_names)
button_height = BTN_SIZE + y_offset

for i, button_name in enumerate(button_names):
    image = pygame.image.load(f"img/{button_name}")
    image_width, image_height = image.get_rect().size

    rect = pygame.Rect(X_OFFSET, Y_OFFSET + i * button_height, image_width, image_height)
    button = Button(rect, f"img/{button_name}")
    buttons.append(button)


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

    def copy(self):
        new_stones = self.stones[:]
        return Group(self.owner, new_stones)

    def __contains__(self, stone):
        return stone in self.stones

    def __str__(self):
        return f"{self.owner}\n{self.stones}"


def print_groups():
    for group in groups:
        print(group)
    print('*' * 10)


class PassButton:
    def __init__(self, rect, image_path):
        self.btn_rect = rect
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.is_active = True
        self.is_pressed = False

    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_active:
            mouse_pos = pygame.mouse.get_pos()
            if self.btn_rect.collidepoint(mouse_pos):
                self.is_pressed = True
                return True  # Signal that the pass button is clicked
        return False

    def draw(self, screen):
        screen.blit(self.image, self.btn_rect)


def calculate_closest_intersection(mouse_pos: tuple[int, int], intersections: list[tuple[int, int]]) -> tuple[int, int]:
    """
    Calculates the closest intersection to the mouse position.
    Args:
        mouse_pos: coordinates of the mouse position
        intersections: list of all 81 intersections

    Returns:
        closest_intersection: the closest intersection to the mouse position
    """
    min_distance = 20
    closest_intersection = None
    for intersection in intersections:
        x, y = intersection
        distance = ((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_intersection = intersection
    return closest_intersection


def render_board(intersections: list[tuple[int, int]], game_state: list[list[int]]) -> None:
    """
    Renders the current game state.
    Args:
        intersections: list of all 81 intersections as tuple of their coordinates
        game_state: matrix of the current game state

    Returns:
        None
    """

    pass_button_rect = pygame.Rect(X_OFFSET, Y_OFFSET + num_buttons * button_height + 100, 200, 100)
    pass_button_image = pygame.image.load("img/pass.png")
    pass_button_image = pygame.transform.scale(pass_button_image, (200, 100))
    screen.blit(board_image, (0, 0))
    screen.blit(pass_button_image, pass_button_rect)
    for i, row in enumerate(game_state):
        for j, val in enumerate(row):
            if val == 1:
                screen.blit(black_piece_image, (
                intersections[i * 9 + j][0] - PIECE_SIZE // 2, intersections[i * 9 + j][1] - PIECE_SIZE // 2))
            elif val == 2:
                screen.blit(white_piece_image, (
                intersections[i * 9 + j][0] - PIECE_SIZE // 2, intersections[i * 9 + j][1] - PIECE_SIZE // 2))


def check_move(x, y, intersections, current_player) -> bool:
    """
    Checks if the move is valid.
    Args:
        x:
        y:
        intersections:
        game_state:
        current_player:

    Returns:
        True if the move is valid, False otherwise
    """

    """
        ko rule:
            if the move we want to make can't be found in the history of states
        rule of liberty:
            and the move we want to make does not make the current player lose a group
        
    """
    global game_state
    closest_intersection = calculate_closest_intersection((x, y), intersections)
    if not closest_intersection:
        return False

    row = intersections.index(closest_intersection) // 9
    col = intersections.index(closest_intersection) % 9
    if game_state[row][col] != 0:
        print("Invalid position - Already occupied")
        return False

    global groups
    # copy the groups array
    groups_copy = []
    for group in groups:
        groups_copy.append(group.copy())
    game_state_copy = copy_game_state(game_state)
    insert_stone(row, col, current_player)

    if was_seen_before(game_state):
        print("Invalid move - Board state repeated")
        groups = groups_copy
        game_state = game_state_copy
        return False

    if not check_liberties(row, col, game_state):
        print("Invalid move - No liberties")
        groups = groups_copy
        game_state = game_state_copy
        return False
    groups = groups_copy
    game_state = game_state_copy
    return True


def check_liberties(row, col, game_state):
    print("Checking liberties")
    for group in groups:
        if (row, col) in group:
            return group.compute_liberties(game_state) > 0

def capture_stones(x, y, intersections):
    global game_state
    global groups
    row = intersections.index((x, y)) // 9
    col = intersections.index((x, y)) % 9
    opponent = 2 if game_state[row][col] == 1 else 1
    adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

    for r, c in adjacent_positions:
        if r < 0 or r >= len(game_state) or c < 0 or c >= len(game_state[0]):
            continue
        if game_state[r][c] == opponent:
            for group in groups:
                if (r, c) in group and group.owner == opponent:
                    if group.compute_liberties(game_state) == 0:
                        print(f"Player {opponent} lost a group: {group.stones}")
                        for stone in group.stones:
                            stone_row, stone_col = stone
                            print(f"Removing stone at ({stone_row}, {stone_col})")
                            game_state[stone_row][stone_col] = 0
                        groups.remove(group)
                        print(f"Player {opponent} lost a group")
                    break

def calculate_score(game_state):
    """
    Calculates the score of each player. The score is the number of free intersections
    surrounded by the player's stones. If there's an opponent's stone in that area,
    the free intersection is not counted. The score is calculated for each player
    separately at the end of the game.

    Args:
        game_state: The matrix representing the current state of the game

    Returns:
        score: A tuple containing the score of each player
    """

    def is_valid(row, col):
        return 0 <= row < len(game_state) and 0 <= col < len(game_state[0])

    def dfs(row, col, visited, player_stone):
        if not is_valid(row, col) or visited[row][col] or game_state[row][col] != player_stone:
            return 0

        visited[row][col] = True
        count = 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            count += dfs(row + dr, col + dc, visited, player_stone)

        return count

    player_scores = [0, 0]  # Player 1 score, Player 2 score

    for player in [1, 2]:
        visited = [[False for _ in range(len(game_state[0]))] for _ in range(len(game_state))]
        for i in range(len(game_state)):
            for j in range(len(game_state[0])):
                if game_state[i][j] == player and not visited[i][j]:
                    player_scores[player - 1] += dfs(i, j, visited, player)

    return tuple(player_scores)

def render_scores(screen, game_state):
    """
    Renders the scores for both players on the screen.

    Args:
        screen: Pygame screen object to render on
        font: Pygame font object to render text
        game_state: The matrix representing the current state of the game

    Returns:
        None
    """
    font=pygame.font.Font('freesansbold.ttf', 32)
    black_score, white_score = calculate_score(game_state)
    white_text = font.render(f"{white_score}", True, (255, 255, 255))
    black_text = font.render(f"{black_score}", True, (0, 0, 0))
    screen.blit(white_text, (95, 685))
    screen.blit(black_text, (900, 685))


def main():
    pass_button_rect = pygame.Rect(X_OFFSET, Y_OFFSET + num_buttons * button_height + 100, 200, 100)
    pass_button_image = pygame.image.load("img/pass.png")
    pass_button_image = pygame.transform.scale(pass_button_image, (200, 100))
    pass_button = PassButton(pass_button_rect, "img/pass.png")
    is_game_over = False
    current_player = 1
    background = lobby_image
    consecutive_passes = [0, 0]

    while not is_game_over:

        # Display the background image
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True
            if background == board_image and pass_button.process_event(event):
                consecutive_passes[current_player - 1] += 1
                print(f"Current player {current_player} passed")

                # Check if both players passed consecutively
                if consecutive_passes[0] >= 2 or consecutive_passes[1] >= 2:
                    black_score, white_score = calculate_score(game_state)
                    if black_score > white_score:
                        background = black_won
                        print("Black player won!")
                    else:
                        background = white_won
                        print("White player won!")

                    print("Game over!")
                    screen.blit(background, (0, 0))
                if consecutive_passes[0] < 2 and consecutive_passes[1] < 2:
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                    print(f"Current player switched to {current_player}")

                # Reset the consecutive pass count for the current player if they made a move
                if check_move(x, y, specific_intersections, current_player):
                    consecutive_passes = [0, 0]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Mouse position at {mouse_pos}")
                if background == lobby_image:
                    for button in buttons:
                        if button.btn_rect.collidepoint(mouse_pos) and button.is_active:
                            if button.image_path in ["img/pvai.png", "img/pvp.png"]:
                                background = board_image
                                screen.blit(background, (0, 0))

                            elif button.image_path == "img/rules.png":
                                background = rules_go_image
                                screen.blit(background, (0, 0))

                            elif button.image_path == "img/quit.png":
                                is_game_over = True
                                pygame.quit()
                                quit()
                elif background == rules_go_image:
                    background = lobby_image
                elif background == board_image:
                    screen.blit(pass_button_image, pass_button_rect)
                    pygame.display.flip()
                    closest_intersection = calculate_closest_intersection(mouse_pos, specific_intersections)
                    if closest_intersection:
                        x, y = closest_intersection
                        valid_move = check_move(x, y, specific_intersections, current_player)
                        if valid_move:
                            if current_player == 1:
                                place_black_piece(x, y, specific_intersections, game_state)
                                current_player = 2
                            else:
                                place_white_piece(x, y, specific_intersections, game_state)
                                current_player = 1
                            capture_stones(x, y, specific_intersections)
                            print_groups()
                            previous_states.append(copy_game_state(game_state))
                            render_board(specific_intersections, game_state)
                            render_scores(screen, game_state)

        # Display and handle button clicks only in the lobby
        if background == lobby_image:
            screen.blit(background, (0, 0))
            for button in buttons:
                button.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
