class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    args: pnum [int] the player's id number
    """
    self.player_num = pnum
    self.lives = 3 # players always start with 3 lives
    self.is_large = False # player always starts small

class Object:
  def __init__(self,pnum=2):
    
    self.height = (x,y)
    self.object_num = pnum 
    self.is_large = True # The object starts off large
    self.stop_movement = True # The object will stop the movement of the player if they collide with it

class Enemy:
  
  def __init__ (self,pnum=3):


    self.size = 0 # The enemy is always small
    self.lose_lives = True # If the player collides with the enemy, the player will lose lives
    self.speed = 0 # The speed of the enemy 


    if Player.lives == 0 :
      print ("Game Over")
