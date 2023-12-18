import pygame
import socket
import json

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 3737
srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_socket.connect((HOST, PORT))

Screen_Width = 1000
Screen_Height = 1000

Black = (0, 0, 0)
White = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
clock = pygame.time.Clock()


#bkg and pieces

def display_main_menu():
    bg_imagine = pygame.image.load('../img/lobby.png')
    screen.blit(bg_imagine, (0, 0))

def display_game():
    bg_imagine = pygame.image.load('../img/board.png')
    screen.blit(bg_imagine, (0, 0))

def display_pieces(matrix, buttons):
    for i in range(len(buttons)):
        if matrix[i] == 1:
            buttons[i].image = pygame.image.load('../img/black.png')
        elif matrix[i] == 2:
            buttons[i].image = pygame.image.load('../img/white.png')
        screen.blit(buttons[i].image, buttons[i].btn_rect)

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

    def draw(self):
        screen.blit(self.image, self.btn_rect)

# Creating buttons for the main menu
BTN_SIZE = 62
X_OFFSET = 200
Y_OFFSET = 185
x_offset = 5
y_offset = 70  # Adjust the vertical spacing between buttons

buttons = []
button_names = ["pvp.png", "pvai.png", "rules.png", "quit.png"]
num_buttons = len(button_names)
button_height = BTN_SIZE + y_offset

for i, button_name in enumerate(button_names):
    rect = pygame.Rect(X_OFFSET, Y_OFFSET + i * button_height, BTN_SIZE, BTN_SIZE)
    button = Button(rect, f"img/{button_name}")
    buttons.append(button)

# Game loop
is_game_over = False
matrix = [0] * 81

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True

    screen.fill(Black)
    display_main_menu()

    for button in buttons:
        button.draw()

    for button in buttons:
        button.process_event(event)
        if button.is_pressed:
            if button.image_path == "img/pvai.png" or button.image_path == "img/pvp.png":
                # Send specific message indicating the PvP or PvAI button was pressed
                client.sendall(b'pvp_button_pressed' if button.image_path == "img/pvp.png" else b'pvai_button_pressed')
            elif button.image_path == "img/quit.png":
                is_game_over = True
                pygame.quit()
                quit()
            elif button.image_path == "img/rules.png":
                # Send a message indicating the Rules button was pressed
                client.sendall(b'rules_button_pressed')

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
client.close()