__author__ = 'srey'
import pygame
from pygame.locals import *

grid = [[0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]]
resolution = (160, 160)
cell_margin = 14
cell_colors = (255, 255, 255), (0, 0, 0)
player_character = "@"
player_color = (255, 0, 0)
player_size = 20
current_position = [0, 1]

def main():
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    screen.fill(cell_colors[1])
    player = pygame.font.Font(None, player_size).render(player_character,
                                                        False, player_color)
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key = event.key
                if key == K_UP:
                    move(0, -1)
                elif key == K_RIGHT:
                    move(1, 0)
                elif key == K_DOWN:
                    move(0, 1)
                elif key == K_LEFT:
                    move(-1, 0)
            elif event.type == QUIT:
                return
        draw_maze(screen)
        draw_player(player, screen)
        pygame.display.update()

def draw_maze(screen):
    for row in xrange(len(grid)):
        for column in xrange(len(grid[0])):
            screen.fill(cell_colors[grid[column][row]],
                        get_cell_rect((row, column), screen))

def get_cell_rect(coordinates, screen):
    row, column = coordinates
    cell_width = screen.get_width() / len(grid)
    adjusted_width = cell_width - cell_margin
    return pygame.Rect(row * cell_width + cell_margin / 2,
                       column * cell_width + cell_margin / 2,
                       adjusted_width, adjusted_width)

def draw_player(player, screen):
    rect = player.get_rect()
    rect.center = get_cell_rect(current_position, screen).center
    screen.blit(player, rect)

def move(dx, dy):
    x, y = current_position
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and \
       grid[ny][nx]:
        current_position[0] = nx
        current_position[1] = ny

if __name__ == "__main__":
    main()
    pygame.quit()