import pygame

class Door:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (112, 95, 54)
        return

    def evolve( self, dt ):

        return

    def draw( self, surface ):

        rect = pygame.Rect( int ( 50 ), int ( 500 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mColor, rect, 0 )

        return
