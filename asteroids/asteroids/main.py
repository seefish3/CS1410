import pygame
import game
import example
import asteroids

TITLE = "Asteroids"
WINDOW_WIDTH  = 700
WINDOW_HEIGHT = 600
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )

        self.game = asteroids.Asteroids( width, height )
        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):

        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        if pygame.K_a in newkeys:
            self.game.actOnPressA( )
        elif pygame.K_a in keys:
            self.game.actOnHoldA( )

        if pygame.K_UP in keys:
            self.game.actOnHoldUP( )

        if 1 in newbuttons:
            self.game.actOnLeftClick()

        self.game.evolve( dt )

        return

    def paint( self, surface ):
        # Draw the current state of the game instance
        self.game.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
