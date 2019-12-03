import pygame

class Walls:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mColor = (124, 114, 185)
        return

    def evolve( self, dt ):
        return

    def draw( self, surface ):

        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mColor, rect, 0 )

        return
