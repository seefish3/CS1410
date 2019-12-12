import pygame
import game
import frogger

TITLE = "Frogger"
CELL_SIZE = 50
NUM_ROW = 12
NUM_COL = 14
WINDOW_HEIGHT = CELL_SIZE * NUM_ROW
WINDOW_WIDTH  = CELL_SIZE * NUM_COL
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):
        super().__init__( title, width, height, frame_rate )
        self.game = frogger.Frogger( CELL_SIZE, NUM_ROW, NUM_COL, width, height )


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        if pygame.K_DOWN in keys:
            self.game.down()

        if pygame.K_UP in keys:
            self.game.up()

        if pygame.K_LEFT in keys:
            self.game.left()

        if pygame.K_RIGHT in keys:
            self.game.right()

        self.game.evolve( dt )

    def paint( self, surface ):
        self.game.draw( surface )

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )

if __name__ == "__main__":
    main( )
