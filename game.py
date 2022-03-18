import pygame
from constants import *
from board import Board
from ai import AI
pygame.init()

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("QUIXO AI")
screen.fill(BG_COLOR)
class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1# 1-cross # 2-circle
        self.gamemode = 'ai' # pvp or ai
        self.running  = True
        self.show_lines()
    
    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def show_lines(self):
        screen.fill(BG_COLOR)
        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR,(SQSIZE,0),(SQSIZE, HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HEIGHT),LINE_WIDTH)

        pygame.draw.line(screen, LINE_COLOR,(WIDTH-2*SQSIZE,0),(WIDTH-2*SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR,(WIDTH-3*SQSIZE,0),(WIDTH-3*SQSIZE,HEIGHT),LINE_WIDTH)
        
        #Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-SQSIZE),(WIDTH,HEIGHT-SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-2*SQSIZE),(WIDTH,HEIGHT-2*SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-3*SQSIZE),(WIDTH,HEIGHT-3*SQSIZE),LINE_WIDTH)

    
    def draw_fig(self,row, col):
        if self.player == 1:
            # draw cross
            # desc line 
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE -OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            
            # asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE -OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)


        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)


    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode='ai' if self.gamemode=='pvp' else 'pvp'

    
    def reset(self):
        self.__init__()

    def isover(self):
        return self.board.final_state(show=True)!=0 or self.board.isfull()
