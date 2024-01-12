import pygame
from constants import WHITE, BLACK, SQUARE_SIZE, GREY, RED, CROWN, NOIR, BLANC



# Load images
# white_piece_image = pygame.image.load('white_dame.png')
# black_piece_image = pygame.image.load('black_dame.png')
class Pion:
    PADDING = 9
    OUTLINE = 2
    def __init__(self, row, col,  color,):
        self.row = row
        self.col = col
        self.color = color
         #self.image = black_piece_image if color == black else white_piece_image
        self.king = False    
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        

    def make_king(self):
        self.king = True

    def draw(self, WINS):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(WINS, GREY, (self.x, self.y), radius + self.OUTLINE)
        
        if self.color == RED:    
            #pygame.draw.circle(WINS, self.color, (self.x, self.y), radius)
            WINS.blit(NOIR, (self.x - NOIR.get_width() // 2, self.y - NOIR.get_height() // 2))
        else :
            WINS.blit(BLANC, (self.x - BLANC.get_width() // 2, self.y - BLANC.get_height() // 2))


       
       
        if self.king:
            WINS.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
            

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()




        
    
    def __repr__(self):
        return str(self.color)