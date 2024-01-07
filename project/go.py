import pygame
import numpy as np

Screen_Width = 1000
Screen_Height = 1000
BOARD_SIZE = 850

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

# def place_black_piece(x, y, intersections, game_state):
#     closest_intersection = calculate_closest_intersection((x, y), intersections)
#     if closest_intersection:
#         row = intersections.index(closest_intersection) // 9
#         col = intersections.index(closest_intersection) % 9
#         if game_state[row][col] == 0:
#             screen.blit(black_piece_image, (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
#             game_state[row][col] = 1  # Set 1 for black piece
#             add_board_state(game_state)  # Add the current game state to previous_states
#             print(f"Player 1 placed a piece at {closest_intersection}")
#         else:
#             print("Invalid position for Player 1")
#     else:
#         print("Invalid position for Player 1")
#
# def place_white_piece(x, y, intersections, game_state):
#     closest_intersection = calculate_closest_intersection((x, y), intersections)
#     if closest_intersection:
#         row = intersections.index(closest_intersection) // 9
#         col = intersections.index(closest_intersection) % 9
#         if game_state[row][col] == 0:
#             screen.blit(white_piece_image, (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
#             game_state[row][col] = 2  # Set 2 for white piece
#             add_board_state(game_state)  # Add the current game state to previous_states
#             print(f"Player 2 placed a piece at {closest_intersection}")
#         else:
#             print("Invalid position for Player 2")
#     else:
#         print("Invalid position for Player 2")

def add_board_state(game_state):
    previous_states.append(np.array(game_state))

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

class Group:
    def __init__(self, point, color, liberties):
        self.color = color
        if isinstance(point, list):
            self.points = point
        else:
            self.points = [point]
        self.liberties = liberties

    @property
    def num_liberty(self):
        return len(self.liberties)

    def add_stones(self, pointlist):
        self.points.extend(pointlist)

    def remove_liberty(self, point):
        self.liberties.remove(point)

    def __str__(self):
        return '%s - stones: [%s]; liberties: [%s]' % (
            self.color,
            ', '.join([str(point) for point in self.points]),
            ', '.join([str(point) for point in self.liberties])
        )

    def __repr__(self):
        return str(self)

def neighbors(point):
    neighboring = [(point[0] - 1, point[1]),
                   (point[0] + 1, point[1]),
                   (point[0], point[1] - 1),
                   (point[0], point[1] + 1)]
    return [point for point in neighboring if 0 < point[0] < BOARD_SIZE and 0 < point[1] < BOARD_SIZE]


def cal_liberty(points, board):
    liberties = [point for point in neighbors(points)
                 if not board.stonedict.get_groups('BLACK', point) and not board.stonedict.get_groups('WHITE', point)]
    return set(liberties)
class PointDict:
    def __init__(self):
        self.d = {'BLACK': {}, 'WHITE': {}}

    def get_groups(self, color, point):
        if point not in self.d[color]:
            self.d[color][point] = []
        return self.d[color][point]

    def set_groups(self, color, point, groups):
        self.d[color][point] = groups

    def remove_point(self, color, point):
        if point in self.d[color]:
            del self.d[color][point]

    def get_items(self, color):
        return self.d[color].items()

class CheckMove(object):
    def __init__(self, next_color=1):
        self.winner = None
        self.next = next_color
        self.legal_actions = []
        self.end_by_no_legal_actions = False
        self.counter_move = 0
        self.libertydict = PointDict()
        self.stonedict = PointDict()
        self.groups = {1: [], 2: []}
        self.endangered_groups = []
        self.removed_groups = []

    def create_group(self, point, color):
        ll = []
        group = Group(point, color, ll)
        self.groups[color].append(group)
        if len(group.liberties) <= 1:
            self.endangered_groups.append(group)
        if color in self.stonedict:
            if point in self.stonedict[color]:
                self.stonedict[color][point].append(group)
            else:
                self.stonedict[color][point] = [group]
        else:
            self.stonedict[color] = {point: [group]}
        for liberty in group.liberties:
            if color in self.libertydict:
                if liberty in self.libertydict[color]:
                    self.libertydict[color][liberty].append(group)
                else:
                    self.libertydict[color][liberty] = [group]
            else:
                self.libertydict[color] = {liberty: [group]}
        return group

    def remove_group(self, group):
        color = group.color
        self.groups[color].remove(group)
        if group in self.endangered_groups:
            self.endangered_groups.remove(group)
        for point in group.points:
            self.get_groups(color, point).remove(group)
        for liberty in group.liberties:
            self.get_groups(color, liberty).remove(group)
    def get_groups(self, color, point):
        return [group for group in self.stonedict[color][point] if point in group.points]
    def merge_groups(self, group_list, point):

        color = group_list[0].color
        new_group = Group(point, color, set())

        all_liberties = set()
        for group in group_list:
            new_group.add_stones(group.points)
            all_liberties |= group.liberties
            self.remove_group(group)

        new_group.add_stones([point])
        all_liberties |= cal_liberty(point, self)

        new_group.liberties = all_liberties

        for p in new_group.points:
            self.get_groups(color, p).append(new_group)

        for liberty in all_liberties:
            belonging_groups = self.get_groups(color, liberty)
            if new_group not in belonging_groups:
                belonging_groups.append(new_group)
        return new_group

    def _get_legal_actions(self):
        if self.winner:
            return []

        endangered_lbt_self = set()
        endangered_lbt_opponent = set()
        for group in self.endangered_groups:
            if group.color == self.next:
                endangered_lbt_self |= group.liberties
            else:
                endangered_lbt_opponent |= group.liberties

        if endangered_lbt_opponent:
            return list(endangered_lbt_opponent)

        legal_actions = []
        if endangered_lbt_self:
            if len(endangered_lbt_self) > 1:
                legal_actions = list(endangered_lbt_self)
            elif len(endangered_lbt_self) == 1:
                legal_actions = list(endangered_lbt_self)
        else:
            opponent = None  # Initialize opponent
            if self.next == 'BLACK':
                opponent = 'WHITE'
            elif self.next == 'WHITE':
                opponent = 'BLACK'
            legal_actions = set()
            if opponent:
                for group in self.groups[opponent]:
                    legal_actions |= group.liberties
            legal_actions = list(legal_actions)

        legal_actions_filtered = []
        for action in legal_actions:
            if len(cal_liberty(action, self)) > 0:
                legal_actions_filtered.append(action)
            else:
                connected_self_groups = [
                    self.get_groups(self.next, p)[0]
                    for p in neighbors(action)
                    if self.get_groups(self.next, p)
                ]
                for self_group in connected_self_groups:
                    if len(self_group.liberties) > 1:
                        legal_actions_filtered.append(action)
                        break

        return legal_actions_filtered

    def shorten_liberty_for_groups(self, point, color):
        opponent = 'WHITE' if color == 'BLACK' else 'BLACK'

        for group in self.libertydict.get_groups(opponent, point):
            group.remove_liberty(point)
            if group.color != color:
                if len(group.liberties) == 0:
                    self.removed_groups.append(group)
                    self.winner = opponent
                elif len(group.liberties) == 1:
                    self.endangered_groups.append(group)

        self.libertydict.remove_point(opponent, point)

        if not self.winner:
            for group in self.libertydict.get_groups(color, point):
                group.remove_liberty(point)
                if group.color != color:
                    if len(group.liberties) == 0:
                        self.removed_groups.append(group)
                        self.winner = opponent
                    elif len(group.liberties) == 1:
                        self.endangered_groups.append(group)
        self.libertydict.remove_point(color, point)

    def place_piece(x, y, intersections, game_state, player):
        closest_intersection = calculate_closest_intersection((x, y), intersections)
        if closest_intersection:
            row = intersections.index(closest_intersection) // 9
            col = intersections.index(closest_intersection) % 9
            if game_state[row][col] == 0:
                if player == 1:
                    screen.blit(black_piece_image,
                                (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
                    game_state[row][col] = 1  # Set 1 for black piece
                    print(f"Player 1 placed a piece at {closest_intersection}")
                else:
                    screen.blit(white_piece_image,
                                (closest_intersection[0] - PIECE_SIZE // 2, closest_intersection[1] - PIECE_SIZE // 2))
                    game_state[row][col] = 2  # Set 2 for white piece
                    print(f"Player 2 placed a piece at {closest_intersection}")
                add_board_state(game_state)  # Add the current game state to previous_states
            else:
                if player == 1:
                    print("Invalid position for Player 1")
                else:
                    print("Invalid position for Player 2")
        else:
            if player == 1:
                print("Invalid position for Player 1")
            else:
                print("Invalid position for Player 2")

        self=game_state
        point = closest_intersection  # modify as needed
        check_legal = False  # modify as needed

        if check_legal and point not in self.legal_actions:
            print('Error: illegal move, try again.')
            return False

        if self.counter_move > 400:
            print(self)
            raise RuntimeError('More than 400 moves in one game! Board is printed.')

        self_belonging_groups = self.libertydict.get_groups(self.next, point).copy()
        self.shorten_liberty_for_groups(point, self.next)
        self.counter_move += 1

        if self.winner:
            self.next = 'WHITE' if self.next == 'BLACK' else 'BLACK'
            return True

        new_group = self.create_or_merge_group(self_belonging_groups, point)
        self.update_endangered_groups(new_group)

        self.next = 'WHITE' if self.next == 'BLACK' else 'BLACK'
        self.update_legal_actions()

        str_groups = [str(group) for group in self.groups['BLACK']] + [str(group) for group in self.groups['WHITE']]
        print('Next: %s\n%s' % (self.next, '\n'.join(str_groups)))

        return len(self.stonedict.get_groups('BLACK', point)) > 0 or len(self.stonedict.get_groups('WHITE', point)) > 0


def main():
    pass_button_rect = pygame.Rect(X_OFFSET, Y_OFFSET + num_buttons * button_height + 100, 200, 100)
    pass_button_image = pygame.image.load("img/pass.png")
    pass_button_image = pygame.transform.scale(pass_button_image, (200, 100))
    pass_button = PassButton(pass_button_rect, "img/pass.png")
    game_logic = CheckMove()
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

                if consecutive_passes[0] >= 2 or consecutive_passes[1] >= 2:
                    is_game_over = True
                    background = lobby_image
                    print("Both players passed consecutively twice. Game over!")

                if consecutive_passes[0] < 2 and consecutive_passes[1] < 2:
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                    print(f"Current player switched to {current_player}")
                # if game_logic.place_piece(x, y, specific_intersections, game_state, current_player):
                #     consecutive_passes = [0, 0]

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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        closest_intersection = calculate_closest_intersection(mouse_pos, specific_intersections)
                        if closest_intersection:
                            x, y = closest_intersection
                            valid_move = game_logic.place_piece(x, y, specific_intersections, game_state, current_player)
                            if valid_move:
                                render_board(specific_intersections, game_state)
                                if current_player == 1:
                                    current_player = 2
                                else:
                                    current_player = 1
                                # render_board(specific_intersections, game_state)
        # Display and handle button clicks only in the lobby
        if background == lobby_image:
            screen.blit(background, (0, 0))
            for button in buttons:
                button.draw()
        elif background == board_image:
            pass_button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
