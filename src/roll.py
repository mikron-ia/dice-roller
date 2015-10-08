import random

class Roll:
    def __init__(self, dice):
        self.dice = dice
        self.rolls = self.roll_all()
        
    def roll_all(self):
        rolls = []
        for die in self.dice:
            rolls.append(self.roll(die))
        return rolls
        
    def roll(self, die):
        return random.randint(1, die)
    
    def get_rolls(self):
        return self.rolls