import pygame
from pions import Pion
from constants import BLACK, ROWS, COLS, WHITE, SQUARE_SIZE, ABS_WHITE, RED


# Create piece instances
# white_piece = Pion( white_piece_image)
# black_piece = Pion(black_piece_image)

class Damier:
    def __init__(self):
        self.damier = []
        self.red_left = self.abs_white_left = 12
        self.red_king = self.abs_white_king = 0
        self.create_damier()
        

    def draw_cubes(self, WINS):
        WINS.fill(BLACK)
        for row in range (ROWS):
            for col in range (row % 2, COLS, 2):
                pygame.draw.rect(WINS, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE ))
    
    def move(self, pion, row, col):
        #echanger le pions entre sa position de depart et sa position d'arriver
        self.damier[pion.row][pion.col], self.damier[row][col] = self.damier[row][col], self.damier[pion.row][pion.col]
        pion.move(row, col)

        if row == ROWS or row == 0:
            pion.make_king()
            if pion.col == ABS_WHITE:
                self.abs_white_king += 1
            else:
                self.red_king += 1

    def get_pion(self, row, col):
        return self.damier[row][col]
            
    def create_damier(self):
        for row in range(ROWS):
            self.damier.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    # Si la case est blanche on l'ajoute a la liste des cases blanches et au nombre de pièces blanches/
                    if row < 3:
                        self.damier[row].append(Pion (row, col, ABS_WHITE))
                    elif row > 4:
                        self.damier[row].append(Pion(row, col, RED))
                    else:
                        self.damier[row].append(0)
                else:
                    self.damier[row].append(0)

    def draw(self, WINS):
        self.draw_cubes(WINS)
        for row in range(ROWS):
            for col in range(COLS):
                pion = self.damier[row][col]
                if pion != 0:
                    pion.draw(WINS)



    def get_valid_move(self, pion):
        move ={}
        left = pion.col - 1
        right= pion.col + 1
        row = pion.row 

        if pion.color == RED or pion.king:
            move.update(self._traverse_left(row - 1, max(row - 3, -1), - 1, pion.color, left))
            move.update(self._traverse_right(row - 1, max(row - 3, -1), - 1, pion.color, right))  
        if pion.color ==  ABS_WHITE or pion.king:
            move.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, pion.color, left))
            move.update(self._traverse_right(row + 1, min(row + 3), ROWS,  1, pion.color, right))  
        
        return move  

    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        move = {}
        last = []
        for r in range (start, stop, step):
            if left < 0:
                break

            current = self.damier[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    move[(r, left)] = last + skipped
                else:
                    move[(r, left)] = last 
                  
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS )

                    move.update(self._traverse_left(r + step, row, step, color, left - 1, skipped=last))
                    move.update(self._traverse_right(r + step, row, step, color, left + 1, skipped=last))
                    break
            elif current.color == color:
                break
            else:
                last = [current]
  
            left -= 1
        return move

    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        move = {}
        last = []
        for r in range (start, stop, step):
            if right >= COLS:
                break

            current = self.damier[r][right]   
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    move[(r, right)] = last + skipped
                else:
                    move[(r, right)] = last 
                
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS )

                    move.update(self._traverse_left(r + step, row, step, color, right -  1, skipped=last))
                    move.update(self._traverse_right(r + step, row, step, color, right + 1, skipped=last))
                    break
            elif current.color == color:
                break
            else:
                last = [current]
  
            right += 1

        return move

      