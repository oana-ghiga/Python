import pygame

Screen_Width = 1000
Screen_Height = 1000

Black = (0, 0, 0)
White = (255, 255, 255)

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
def place_black_piece(x, y):
    screen.blit(black_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))
    print(f"Player 1 placed a piece at {x, y}")
def place_white_piece(x, y):
    screen.blit(white_piece_image, (x - PIECE_SIZE // 2, y - PIECE_SIZE // 2))
    print(f"Player 2 placed a piece at {x, y}")


# Create a list of grid intersections
grid_intersections = []
for i in range(9):
    for j in range(9):
        x = X_OFFSET + i * CELL_WIDTH
        y = Y_OFFSET + j * CELL_HEIGHT
        grid_intersections.append((x, y))
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


# Game loop
is_game_over = False
current_player = 1  # Player 1 starts the game
background = lobby_image  # Set lobby image as initial background

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(f"Mouse position at {mouse_pos}")
            if background == lobby_image:
                for button in buttons:
                    if button.btn_rect.collidepoint(mouse_pos) and button.is_active:
                        if button.image_path in ["img/pvai.png", "img/pvp.png"]:
                            background = board_image  # Switch background to game board
                        elif button.image_path == "img/rules.png":
                            background = rules_go_image  # Switch background to rules screen
                        elif button.image_path == "img/quit.png":
                            is_game_over = True
                            pygame.quit()
                            quit()
            elif background == rules_go_image:
                background = lobby_image
            elif background == board_image:
                # Calculate the closest grid intersection to the mouse click
                closest_intersection = calculate_closest_intersection(mouse_pos, grid_intersections)
                if closest_intersection:
                    x, y = closest_intersection
                    # Place black.png at the closest intersection for Player 1
                    if current_player == 1:
                        print(f"first player")
                        place_black_piece(x, y)
                        print(f"Player 1 placed a piece at {x, y}")
                        current_player = 2
                    else:
                        print(f"second player")
                        place_white_piece(x, y)
                        print(f"Player 2 placed a piece at {x, y}")
                        current_player = 1

    screen.fill(Black)

    # Display the background image
    screen.blit(background, (0, 0))

    # Display and handle button clicks only in the lobby
    if background == lobby_image:
        for button in buttons:
            button.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()