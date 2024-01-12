import pygame
from constants import RED, ABS_WHITE, BLUE, SQUARE_SIZE
from damier import Damier

class Game:
    def __init__(self, WINS):
        self._init()
        self.WINS = WINS

    def update(self):
        self.damier.draw(self.WINS)
        self.draw_valid_move(self.valid_move)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.damier = Damier() 
        self.turn = RED
        self.valid_move = {}

    

    def reset(self):
        self._init()
        
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        pion = self.damier.get_pion(row, col)
        if pion != 0 and pion.color == self.turn:
            self.selected = pion
            self.valid_move = self.damier.get_valid_move(pion)
            return True


    def _move(self, row, col):
        pion = self.damier.get_pion(row, col)
        if self.selected and pion == 0 and (row, col) in self.valid_move:
            self.damier.move(self.selected, row, col)
        else:
            return False
        return True
    

    def draw_valid_move(self, move):
        for m in move:
            row, col = m
            pygame.draw.circle(self.WINS, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
        
    
    def turn_player(self):
        if self.turn == RED :
            self.turn = ABS_WHITE
        else:
            self.turn = RED