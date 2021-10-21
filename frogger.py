import pygame

# this example game draws 3 concentric circles on top of a single color background
# the circles move down every time frame
# the user can control the circles by:
# - clicking the left mouse button to relocate them
# - holding the UP key to move them up
# - pressing the A key to move them to the left of the window
# - holding the A key to gradually move them to the right
class Frogger:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height

        # object colors
        self.mBackColor = ( 192, 47, 75 )
        self.mFrogColor = ( 229, 217, 189 )
        self.mRoadColor = ( 2, 2, 2 )
        self.mCarColor = ( 186, 28, 33 )
        self.mDozerColor = ( 136, 21, 24 )

       

      
        
        return

    
    def actOnPressA( self ):
        
        return


    def actOnHoldA( self ):
        
        return

    
    def actOnHoldUP( self ):
        
        return

    
    def actOnLeftClick( self, x, y ):
        
        return

    
    def evolve( self, dt ):
        
        return

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mBackColor, rect, 0 )

  

        
        
        return
