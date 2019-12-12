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
        top = pygame.Rect( int ( self.x ), int ( self.x ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mColor, rect, 0 )


        return
