import pygame

class Mountain:

    def __init__( self, outline ):
        self.mOutline = outline
        self.mColor = ( 148, 86, 164 )
        return

    def evolve( self, dt ):
        return

    def draw( self, surface ):
        pygame.draw.polygon( surface, self.mColor, self.mOutline, 0 )
        pygame.draw.polygon( surface, (0,0,0), self.mOutline, 1 )
        return
