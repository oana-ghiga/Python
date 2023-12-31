import pygame

Screen_Width = 1000
Screen_Height = 1000

Black = (0, 0, 0)
White = (255, 255, 255)
previous_states = set()# List to store previous game states

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

def generate_intersections(grid_size_x, grid_size_y, initial_point, cell_width, cell_height):
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

previous_move_sequences = set()
previous_states_hashes = set()
class GameState:
    def __init__(self):
        self.pass_button_rect = pygame.Rect(X_OFFSET, Y_OFFSET + num_buttons * button_height + 100, 200, 100)
        self.game_state = [[0 for _ in range(9)] for _ in range(9)]
        self.previous_states = []
        self.moves_history = []
        # Define pass_button and its image here
        pass_button_rect = pygame.Rect(X_OFFSET, Y_OFFSET + num_buttons * button_height + 100, 200, 100)
        self.pass_button = PassButton(pass_button_rect, "img/pass.png")
        self.pass_button_image = pygame.image.load("img/pass.png")
        self.pass_button_image = pygame.transform.scale(self.pass_button_image, (200, 100))

    @staticmethod
    def calculate_closest_intersection(mouse_pos, intersections):
        # Find the closest grid intersection to the mouse position
        min_distance = float('inf')
        closest_intersection = None
        for intersection in intersections:
            x, y = intersection
            distance = ((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_intersection = intersection
        return closest_intersection

    def is_valid_position(self, row, col):
        return 0 <= row < len(self.game_state) and 0 <= col < len(self.game_state[0])

    def check_move(self, x, y, intersections, current_player):
        closest_intersection = self.calculate_closest_intersection((x, y), intersections)

        if closest_intersection:
            row = intersections.index(closest_intersection) // 9
            col = intersections.index(closest_intersection) % 9

            print(f"Checking move at ({row}, {col}) for player {current_player}")

            if self.game_state[row][col] == 0:
                print("Position is empty")
            else:
                print("Position is occupied")

            if self.check_liberties(row, col):
                print("There are liberties")
            else:
                print("No liberties")

            if self.game_state[row][col] == 0 and self.check_liberties(row, col):
                return True
            else:
                print("Invalid move")
                return False
        else:
            print("Invalid position - Outside the board")
            return False

    def add_move_to_history(self, move):
        self.moves_history.append(move)

    def check_repetition(self):
        if len(self.moves_history) < 4:  # Check repetition after at least 4 moves
            return False

        moves_subset = self.moves_history[-4:]  # Consider the latest 4 moves
        if tuple(moves_subset) in previous_move_sequences:
            print("Repetition in game state detected")
            return True

        previous_move_sequences.add(tuple(moves_subset))
        return False

    def add_board_state(self):
        state_hash = hash(str(self.game_state))
        if state_hash in previous_states_hashes:
            print("Repetition in game state detected2")
            return True

        previous_states_hashes.add(state_hash)
        return False

    def check_liberties(self, row, col):
        visited = set()
        adjacent_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

        liberties = False
        for r, c in adjacent_positions:
            if self.is_valid_position(r, c):
                if self.game_state[r][c] == 0:
                    liberties = True
                    break
                elif self.game_state[r][c] == self.game_state[row][col] and (r, c) not in visited:
                    visited.add((r, c))
                    liberties = liberties or self.check_liberties(r, c)

        return liberties

    def mark_territories(self):
        territories = [[0 for _ in range(9)] for _ in range(9)]

        def flood_fill(row, col, player):
            stack = [(row, col)]
            visited = set()

            while stack:
                x, y = stack.pop()
                if not (0 <= x < 9) or not (0 <= y < 9) or (x, y) in visited or territories[x][y] != 0 or self.game_state[x][
                    y] != 0:
                    continue

                visited.add((x, y))
                territories[x][y] = player

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

        for i in range(9):
            for j in range(9):
                if self.game_state[i][j] == 0 and territories[i][j] == 0 and self.is_valid_position(i, j):
                    black_surrounding = any(
                        self.game_state[i + dx][j + dy] == 1 if self.is_valid_position(i + dx, j + dy) else False
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    )
                    white_surrounding = any(
                        self.game_state[i + dx][j + dy] == 2 if self.is_valid_position(i + dx, j + dy) else False
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    )

                    if black_surrounding and not white_surrounding:
                        flood_fill(i, j, 1)
                    elif white_surrounding and not black_surrounding:
                        flood_fill(i, j, 2)
        return territories

    def check_liberties_after_move(self, x, y, current_player, territories):
        opposite_player = 2 if current_player == 1 else 1
        visited = set()

        def check_liberties_recursive(row, col, player):
            if not self.is_valid_position(row, col) or (row, col) in visited:
                return set()

            visited.add((row, col))
            captured = {(row, col)}

            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                captured |= check_liberties_recursive(r, c, player) if self.is_valid_position(r, c) and \
                                                                       self.game_state[r][c] == player else set()

            return captured

        captured_stones = set()
        for i in range(len(self.game_state)):
            for j in range(len(self.game_state[0])):
                if self.game_state[i][j] == opposite_player:
                    surrounded = check_liberties_recursive(i, j, opposite_player)
                    captured_stones |= surrounded

        for stone_row, stone_col in captured_stones:
            self.game_state[stone_row][stone_col] = 0

        territories = self.mark_territories()
        return self.game_state, territories

    def place_black_piece(self, x, y, intersections):
        closest_intersection = self.calculate_closest_intersection((x, y), intersections)

        if closest_intersection:
            row = intersections.index(closest_intersection) // 9
            col = intersections.index(closest_intersection) % 9

            if self.game_state[row][col] == 0 and self.check_liberties(row, col):
                screen.blit(black_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))
                self.game_state[row][col] = 1  # Set the grid position to represent a black piece
                self.add_board_state()  # Add the current state to the set of previous states
                self.add_move_to_history((x, y))  # Add the current move to the history
                return True
            else:
                print("Invalid move")
                return False
        else:
            print("Invalid position - Outside the board")
            return False

    def place_white_piece(self, x, y, intersections):
        closest_intersection = self.calculate_closest_intersection((x, y), intersections)

        if closest_intersection:
            row = intersections.index(closest_intersection) // 9
            col = intersections.index(closest_intersection) % 9

            if self.game_state[row][col] == 0 and self.check_liberties(row, col):
                screen.blit(white_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))
                self.game_state[row][col] = 2  # Set the grid position to represent a white piece
                self.add_board_state()  # Add the current state to the set of previous states
                self.add_move_to_history((x, y))  # Add the current move to the history
                return True
            else:
                print("Invalid move")
                return False
        else:
            print("Invalid position - Outside the board")
            return False

    def render_board(self, intersections):
        # Draw the board
        screen.blit(board_image, (0, 0))

        # Draw the stones
        for i in range(len(self.game_state)):
            for j in range(len(self.game_state[0])):
                if self.game_state[i][j] == 1:
                    x, y = intersections[i * 9 + j]
                    screen.blit(black_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))
                elif self.game_state[i][j] == 2:
                    x, y = intersections[i * 9 + j]
                    screen.blit(white_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))

        # Draw the pass button
        screen.blit(self.pass_button_image, self.pass_button_rect)
        pygame.display.flip()


def main():
    game_state = GameState()
    is_game_over = False
    current_player = 1
    background = lobby_image
    consecutive_passes = [0, 0]

    while not is_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_game_over = True
            if background == board_image and game_state.pass_button.process_event(event):
                consecutive_passes[current_player - 1] += 1
                if consecutive_passes[0] >= 2 or consecutive_passes[1] >= 2:
                    is_game_over = True
                    background = lobby_image
                if consecutive_passes[0] < 2 and consecutive_passes[1] < 2:
                    current_player = 2 if current_player == 1 else 1

                    if game_state.check_move(x, y, specific_intersections, current_player):
                        consecutive_passes = [0, 0]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if background == lobby_image:
                    for button in buttons:
                        if button.btn_rect.collidepoint(mouse_pos) and button.is_active:
                            if button.image_path in ["img/pvai.png", "img/pvp.png"]:
                                background = board_image  # Switch background to game board
                                screen.blit(background, (0, 0))

                            elif button.image_path == "img/rules.png":
                                background = rules_go_image  # Switch background to rules screen
                                screen.blit(background, (0, 0))

                            elif button.image_path == "img/quit.png":
                                is_game_over = True
                                pygame.quit()
                                quit()
                elif background == rules_go_image:
                    background = lobby_image
                elif background == board_image:
                    closest_intersection = game_state.calculate_closest_intersection(mouse_pos, specific_intersections)

                    if closest_intersection:
                        x, y = closest_intersection
                        if game_state.check_move(x, y, specific_intersections, current_player):
                            if current_player == 1:
                                game_state.place_black_piece(x, y, specific_intersections)
                                print("placed black piece at", x, y, "for player", current_player)
                            else:
                                game_state.place_white_piece(x, y, specific_intersections)
                                print("placed white piece at", x, y, "for player", current_player)

                            # Update the moves history after making a move
                            game_state.add_move_to_history((x, y))

                            # Check for repetition after updating the moves history
                            if game_state.check_repetition():
                                print("Invalid move: Repetition detected")

                            game_state.game_state, territories = game_state.check_liberties_after_move(
                                x, y, current_player, game_state.game_state)
                            current_player = 2 if current_player == 1 else 1


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