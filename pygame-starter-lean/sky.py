import pygame

class Sky:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mColor = ( 76, 205, 249 )
        return

    def evolve( self, dt ):
        # r = int(self.mColor[ 0 ] + dt * 20)
        # g = int(self.mColor[ 1 ] + dt * 10)
        # b = int(self.mColor[ 2 ] - dt * 10)
        # if r > 255:
        #     r = 255
        # if g > 255:
        #     g = 255
        # if b < 0:
        #     b = 0
        # self.mColor = ( r, g, b )
        return

    def draw( self, surface ):

        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mColor, rect, 0 )
        
        return
