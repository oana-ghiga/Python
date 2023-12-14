import pygame
import socket

HOST = '127.0.0.1'
PORT = 3737
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game Menu")

# some buttons
button_play_comp = pygame.Rect(50, 100, 200, 50)
button_play_player = pygame.Rect(50, 200, 200, 50)
button_rules = pygame.Rect(50, 300, 200, 50)
button_quit = pygame.Rect(50, 400, 200, 50)

#game loop
running = True
while running:
    win.fill((255, 255, 255))  # bkg

    # Draw buttons
    pygame.draw.rect(win, (0, 255, 0), button_play_comp)
    pygame.draw.rect(win, (0, 255, 0), button_play_player)
    pygame.draw.rect(win, (0, 255, 0), button_rules)
    pygame.draw.rect(win, (0, 255, 0), button_quit)

    # Add button text
    font = pygame.font.Font(None, 36)
    text_play_comp = font.render('Play against Computer', True, (0, 0, 0))
    text_play_player = font.render('Play against Player', True, (0, 0, 0))
    text_rules = font.render('Rules', True, (0, 0, 0))
    text_quit = font.render('Quit', True, (0, 0, 0))
    win.blit(text_play_comp, (button_play_comp.x + 10, button_play_comp.y + 10))
    win.blit(text_play_player, (button_play_player.x + 25, button_play_player.y + 10))
    win.blit(text_rules, (button_rules.x + 25, button_rules.y + 10))
    win.blit(text_quit, (button_quit.x + 60, button_quit.y + 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check if buttons are clicked
                mouse_pos = pygame.mouse.get_pos()
                if button_play_comp.collidepoint(mouse_pos):
                    # to add play against ai code
                    pass
                elif button_play_player.collidepoint(mouse_pos):
                    # to add play against another client
                    pass
                elif button_rules.collidepoint(mouse_pos):
                    # show a new screen with rules
                    pass
                elif button_quit.collidepoint(mouse_pos):
                    running = False # exit game

    pygame.display.update()

pygame.quit()
