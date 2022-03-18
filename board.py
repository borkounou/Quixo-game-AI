from constants import *
import numpy as np
import pygame
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("QUIXO AI")
screen.fill(BG_COLOR)
class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares # [squares]
        self.mark_sqrs = 0

    def final_state(self, show=False):
        '''
        @return 0 if there is  no win yet
        @return 1 if player 1 wins
        @return 2 if player 2 wins
        '''
        #Vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col]== self.squares[3][col]==self.squares[4][col]!=0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] ==2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE//2, 20)
                    fPos = (col * SQSIZE + SQSIZE//2, HEIGHT-20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        #Horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2]== self.squares[row][3]==self.squares[row][4]!=0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] ==2 else CROSS_COLOR
                    iPos = ( 20, row * SQSIZE + SQSIZE//2)
                    fPos = (WIDTH-20, row * SQSIZE + SQSIZE//2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]
        
        # Desc diagonal 
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2]==self.squares[3][3] ==self.squares[4][4] !=0:
            if show:
                    color = CIRC_COLOR if self.squares[2][2] ==2 else CROSS_COLOR
                    iPos = ( 20,20)
                    fPos = (WIDTH-20, HEIGHT-20)
            return  self.squares[2][2]

        # Asc diagonal 

        if self.squares[4][0] == self.squares[3][1] == self.squares[2][2]==self.squares[1][3] ==self.squares[0][4] !=0:
            if show:
                    color = CIRC_COLOR if self.squares[2][2] ==2 else CROSS_COLOR
                    iPos = (20,HEIGHT-20)
                    fPos = (WIDTH-20, 20)
            return  self.squares[2][2]
        
        # no win yet
        return 0
        

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.mark_sqrs += 1 # to be check 

    
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

 
    def get_empty_sqrs(self):
        empty_sqrs = list()
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))

        return empty_sqrs


    
    def isfull(self):
        return self.mark_sqrs ==25
    

    def isempty(self):
        return self.mark_sqrs == 0
