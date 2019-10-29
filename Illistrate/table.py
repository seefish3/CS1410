import pygame

class Table:

    def __init__( self, x, y, width, height, r, g, b ):
        self.mWidth = width
        self.mHeight = height
        self.x = x
        self.y = y
        self.mColor = ( r, g, b)
        return

    def evolve( self, dt ):

        return

    def draw( self, surface ):
        top = line(start_pos, end_pos, width)
        leg1 = line(start_pos, end_pos, width)
        leg2 = line(start_pos, end_pos, width)
        pygame.draw.line( surface, self.mColor, top, 0 )
        pygame.draw.line( surface, self.mColor, leg1, 0 )
        pygame.draw.line( surface, self.mColor, leg2, 0 )

        return
