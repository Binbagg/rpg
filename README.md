from collections.abc import ItemsView
import random
import os
import time

#CamelCase for classes
#camelCase for vars
#snake_case for functions in classes



def clear():
  os.system("clear")

def draw(): 
  print("X════════════════════════════════════X")

class CharacterBase: # baseplate for all characters, they can attack and have properties
  def __init__(self, health:int, name:str, strength:int, fortitude:int) -> None:
    self.name = name
    self.strength = strength
    self.fortitude = fortitude

    self.health = health
    self.max_health = self.health
    self.weapon = fist
    self.inventory = InventoryManager() # GIVES CHARACTER A INVENTORY
