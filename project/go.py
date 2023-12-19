import pygame

Screen_Width = 1000
Screen_Height = 1000

Black = (0, 0, 0)
White = (255, 255, 255)

game_state = [[0 for _ in range(9)] for _ in range(9)]
previous_states = []

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
def place_black_piece(x, y, intersections, game_state):
    closest_intersection = calculate_closest_intersection((x, y), intersections)
    if closest_intersection:
        row = intersections.index(closest_intersection) // 9
        col = intersections.index(closest_intersection) % 9
        if game_state[row][col] == 0:
            screen.blit(black_piece_image, (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
            game_state[row][col] = 1
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
            screen.blit(white_piece_image, (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
            game_state[row][col] = 2
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

def calculate_closest_intersection(mouse_pos, intersections):
    # Find the closest grid intersection to the mouse position
    min_distance = 20
    closest_intersection = None
    for intersection in intersections:
        x, y = intersection
        distance = ((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_intersection = intersection
    return closest_intersection

def render_board(intersections, game_state):
    for i, row in enumerate(game_state):
        for j, val in enumerate(row):
            if val == 1:
                screen.blit(black_piece_image, (intersections[i * 9 + j][0] - PIECE_SIZE // 2, intersections[i * 9 + j][1] - PIECE_SIZE // 2))
            elif val == 2:
                screen.blit(white_piece_image, (intersections[i * 9 + j][0] - PIECE_SIZE // 2, intersections[i * 9 + j][1] - PIECE_SIZE // 2))

def check_move(x, y, intersections, game_state, current_player):
    closest_intersection = calculate_closest_intersection((x, y), intersections)
    if closest_intersection:
        row = intersections.index(closest_intersection) // 9
        col = intersections.index(closest_intersection) % 9
        if game_state[row][col] == 0:
            return True
        else:
            print("Invalid position - Already occupied")
            return False
    elif check_repetition(game_state):
        print("Invalid move - Board state repeated")
        return False
    elif closest_intersection:
        row = intersections.index(closest_intersection) // 9
        col = intersections.index(closest_intersection) % 9
        if not check_liberties(row, col, game_state):
            print("Invalid move - No liberties")
            return False
        else:
            return True
    else:
        print("Invalid position - Outside the board")
        return False

def check_repetition(game_state):
    current_state = tuple(map(tuple, game_state))
    if current_state in previous_states:
        return True
    return False

def add_board_state(game_state):
    # Convert the 2D game state to a tuple and add it to the list
    previous_states.append(tuple(map(tuple, game_state)))

def check_liberties(row, col, game_state, visited=None):
    if visited is None:
        visited = set()

    if (row, col) in visited:
        return False

    visited.add((row, col))
    adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    liberties = False

    for r, c in adjacent_positions:
        if 0 <= r < len(game_state) and 0 <= c < len(game_state[0]):
            if game_state[r][c] == 0:
                liberties = True
                break  # If an empty adjacent position is found, the stone has liberties
            elif game_state[r][c] == game_state[row][col]:
                liberties = liberties or check_liberties(r, c, game_state, visited)

    return liberties


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
                    is_game_over = True
                    background = lobby_image
                    print("Both players passed consecutively twice. Game over!")

                # Switch player if both players haven't passed consecutively twice
                if consecutive_passes[0] < 2 and consecutive_passes[1] < 2:
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                    print(f"Current player switched to {current_player}")

                # Reset the consecutive pass count for the current player if they made a move
                if check_move(x, y, specific_intersections, game_state, current_player):
                    consecutive_passes = [0,0]

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(f"Mouse position at {mouse_pos}")
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
                    screen.blit(pass_button_image, pass_button_rect)
                    pygame.display.flip()
                    closest_intersection = calculate_closest_intersection(mouse_pos, specific_intersections)
                    if closest_intersection:
                        x, y = closest_intersection
                        valid_move = check_move(x, y, specific_intersections, game_state, current_player)
                        if valid_move:
                            if current_player == 1:
                                place_black_piece(x, y, specific_intersections, game_state)
                                current_player = 2
                            else:
                                place_white_piece(x, y, specific_intersections, game_state)
                                current_player = 1
                            render_board(specific_intersections, game_state)

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