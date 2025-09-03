# Copyright Gary Roberson 2024

import random

class Dice:
    def __init__(self, num_dice=2):
        self.num_dice = num_dice
        self.last_roll = []
        self.doubles_count = 0
    
    def roll(self):
        """Roll the dice and return the results"""
        self.last_roll = [random.randint(1, 6) for _ in range(self.num_dice)]
        
        # Check for doubles
        if len(self.last_roll) == 2 and self.last_roll[0] == self.last_roll[1]:
            self.doubles_count += 1
        else:
            self.doubles_count = 0
            
        return self.last_roll
    
    def get_total(self):
        """Get the total value of the last roll"""
        return sum(self.last_roll)
    
    def is_doubles(self):
        """Check if the last roll was doubles"""
        return len(self.last_roll) == 2 and self.last_roll[0] == self.last_roll[1]
    
    def get_doubles_count(self):
        """Get the number of consecutive doubles rolled"""
        return self.doubles_count
    
    def reset_doubles_count(self):
        """Reset the doubles counter"""
        self.doubles_count = 0