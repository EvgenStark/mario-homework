import pygame
from map import Board
from pprint import pprint
from user import Player


def open_level(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        level_map = [line.strip() for line in f]
    max_width = max(map(len, level_map))
    container = list(map(lambda x: x.ljust(max_width, '.'), level_map))
    container = list(list(i) for i in container)
    return container


player = Player()
board = Board()
maps = open_level('levels/map.txt')
camera = (0, 0)

width, height = 12, 12
TILE = 50

pygame.init()
screen = pygame.display.set_mode((600, 600))
map_screen = pygame.Surface((500, 500))
pygame.display.set_caption("MARIO")

for i in range(len(maps)):
    for j in range(len(maps[i])):
        if maps[i][j] == '@':
            player.x = i
            player.y = j
            camera = (i, j)
            maps[i][j] = '.'
        board.replace(i, j, maps[i][j])
image_board = list(list(j for j in i) for i in board.container)
board.replace(player.x, player.y, '@')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player.x - 1 < 0 and board.container[player.y][9] != '#':
                    board.replace(player.x, player.y, '.')
                    board.replace(9, player.y, '@')
                    player.x = 9
                    image_board = list([i[-1]] + i[:-1] for i in image_board)
                elif player.x > 0:
                    if board.container[player.y][player.x - 1] != "#":
                        player.left()
                        image_board = list([i[-1]] + i[:-1] for i in image_board)
                        board.replace(player.x + 1, player.y, '.')
                        board.replace(player.x, player.y, '@')
            if event.key == pygame.K_RIGHT:
                if player.x + 1 > 9 and board.container[player.y][0] != '#':
                    board.replace(player.x, player.y, '.')
                    board.replace(0, player.y, '@')
                    player.x = 0
                    image_board = list(i[1:] + [i[0]] for i in image_board)
                elif player.x < 9:
                    if board.container[player.y][player.x + 1] != "#":
                        player.right()
                        image_board = list(i[1:] + [i[0]] for i in image_board)
                        board.replace(player.x - 1, player.y, '.')
                        board.replace(player.x, player.y, '@')
            if event.key == pygame.K_UP:
                if player.y - 1 < 0 and board.container[player.y][9] != '#':
                    board.replace(player.x, player.y, '.')
                    board.replace(player.x, 9, '@')
                    player.y = 9
                    image_board = [image_board[-1]] + image_board[:-1]
                elif player.y > 0:
                    if board.container[player.y - 1][player.x] != "#":
                        player.top()
                        image_board = [image_board[-1]] + image_board[:-1]
                        board.replace(player.x, player.y + 1, '.')
                        board.replace(player.x, player.y, '@')
            if event.key == pygame.K_DOWN:
                if player.y + 1 > 9 and board.container[player.y][0] != '#':
                    board.replace(player.x, player.y, '.')
                    board.replace(player.x, 0, '@')
                    player.y = 0
                    image_board = image_board[1:] + [image_board[0]]
                elif player.y < 9:
                    if board.container[player.y + 1][player.x] != "#":
                        player.bottom()
                        image_board = image_board[1:] + [image_board[0]]
                        board.replace(player.x, player.y - 1, '.')
                        board.replace(player.x, player.y, '@')

    screen.fill((0, 0, 0))
    for i in range(len(image_board)):
        for j in range(len(image_board[i])):
            if image_board[i][j] == '#':
                image = pygame.image.load('data/box.png').convert()
                map_screen.blit(image, (50 * j, 50 * i))
            if image_board[i][j] == '.':
                image = pygame.image.load('data/grass.png').convert()
                map_screen.blit(image, (50 * j, 50 * i))
    mario = pygame.image.load('data/mar.png').convert_alpha()
    map_screen.blit(mario, (215, 205))
    screen.blit(map_screen, (50, 50))
    pygame.display.flip()
pygame.quit()
