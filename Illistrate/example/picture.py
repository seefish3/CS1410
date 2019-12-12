import sky
import sun
import mountain
import cloud
import small_bird

class Picture:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.mSky = sky.Sky( self.mWidth, self.mHeight )
        self.mSun = sun.Sun( 0.67 * self.mWidth, 0.47 * self.mHeight, (1./8.)*self.mHeight )
        outline = [ ( int(0*self.mWidth), int(1*self.mHeight) ),
                    ( int(0*self.mWidth), int((2/3)*self.mHeight) ),
                    ( int(0.25*self.mWidth), int((5/9)*self.mHeight) ),
                    ( int(0.5*self.mWidth), int((2/3)*self.mHeight) ),
                    ( int((5/6)*self.mWidth), int((4/9)*self.mHeight) ),
                    ( int(1*self.mWidth), int((7/9)*self.mHeight) ),
                    ( int(1*self.mWidth), int(1*self.mHeight) ) ]
        self.mMountain = mountain.Mountain( outline )
        self.mCloud1 = cloud.Cloud( 0.1*self.mWidth, .43*self.mHeight,
                                    0.31*self.mWidth, 0.20*self.mHeight)
        self.mCloud1.darken()
        self.mCloud2 = cloud.Cloud( 0.70*self.mWidth, .10*self.mHeight,
                                    0.16*self.mWidth, 0.10*self.mHeight)
        self.mCloud3 = cloud.Cloud( 0.55*self.mWidth, .40*self.mHeight,
                                    0.40*self.mWidth, 0.10*self.mHeight)
        self.mCloud3.lighten()
        self.mSmallBird1 = small_bird.SmallBird( 0.25*self.mWidth, 0.25*self.mHeight, 0.07*self.mWidth, 0.04*self.mHeight )
        self.mSmallBird2 = small_bird.SmallBird( 0.22*self.mWidth, 0.28*self.mHeight, 0.07*self.mWidth, 0.04*self.mHeight )
        self.mSmallBird2.thicken( )
        self.mSmallBird3 = small_bird.SmallBird( 0.15*self.mWidth, 0.30*self.mHeight, 0.07*self.mWidth, 0.04*self.mHeight )
        return

    def evolve( self, dt ):
        self.mSky.evolve( dt )
        self.mSun.evolve( dt )
        self.mMountain.evolve( dt )
        self.mCloud1.evolve( dt )
        self.mCloud2.evolve( dt )
        self.mCloud3.evolve( dt )
        self.mSmallBird1.evolve( dt )
        self.mSmallBird2.evolve( dt )
        self.mSmallBird3.evolve( dt )
        return

    def draw( self, surface ):
        self.mSky.draw( surface )
        self.mSun.draw( surface )
        self.mCloud3.draw( surface )
        self.mMountain.draw( surface )
        self.mCloud1.draw( surface )
        self.mCloud2.draw( surface )
        self.mSmallBird1.draw( surface )
        self.mSmallBird2.draw( surface )
        self.mSmallBird3.draw( surface )
        return


