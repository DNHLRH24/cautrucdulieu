import pygame
from pygame.locals import *

WINDOW_SIZE = 500
BOARD_SIZE = 8
SQUARE_SIZE = WINDOW_SIZE // BOARD_SIZE
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Knight\'s Tour')

def draw_board(board):
    DISPLAY_SURFACE.fill((255, 255, 255))
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j]:
                pygame.draw.rect(DISPLAY_SURFACE, GREEN, (i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if (i + j) % 2 == 0:
                pygame.draw.rect(DISPLAY_SURFACE, (0, 0, 0), (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(DISPLAY_SURFACE, (250, 250, 250), (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.update()

def draw_knight(pos):
    x, y = pos
    pygame.draw.circle(DISPLAY_SURFACE, RED, (int(x * SQUARE_SIZE + SQUARE_SIZE/2), int(y * SQUARE_SIZE + SQUARE_SIZE/2)), SQUARE_SIZE//2 - 10)
    pygame.display.update()
    pygame.time.wait(200)

def valid(pos,board):
    x, y = pos
    if x >= 0 and y >= 0 and x < BOARD_SIZE and y < BOARD_SIZE and board[x][y] is None:
        return True
    return False

def knight_tour_util(x, y, pos, move_number, board, x_moves, y_moves):
    board[x][y] = move_number        
    draw_board(board)
    draw_knight((x, y))

    # terminate when we visit all cells on the board
    if move_number == BOARD_SIZE * BOARD_SIZE:
        return True
    
    for i in range(8):
        new_x = x + x_moves[i]
        new_y = y + y_moves[i]
        if valid((new_x, new_y), board):
            if knight_tour_util(new_x, new_y, pos, move_number+1, board, x_moves, y_moves):
                return True
            else:
                board[new_x][new_y] = None
    # backtrack if no solution was found
    board[x][y] = None    
    draw_board(board)
    pygame.time.wait(50)
    return False

def knight_tour(graph,start_pos):
    x,y  = start_pos
    board = [[None] * BOARD_SIZE for i in range(BOARD_SIZE)]   
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    
    knight_tour_util(x, y, start_pos, 1, board, x_moves, y_moves)

def main():
    graph = {}
    knight_tour(graph,(0,0))
    print('Done')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()
