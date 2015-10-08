__author__ = "Mikron"
__version__ = "0.0-dev"

from roll import Roll
dice = [ 6, 6, 20 ]

if __name__ == "__main__":
    
    rolls = Roll(dice)
    
    roll_results = rolls.get_rolls()
    
    for roll in roll_results:
        print("Roll: "+str(roll)+"\n")