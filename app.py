from collections.abc import ItemsView
import random
import os
import time

#CamelCase for classes
#camelCase for vars
#snake_case for functions in classes


#CURRENT PROBLEMS, CHARACTERBASE IS USED TO GENERATE ENEMIES, BUT THAT MEANS ENEMIES 
#CAN HAVE statusCheck(self), THIS COULD BE USED FOR A COOL SPELL THOUGH

#class to do: InventoryManager, defs: drop, add, equip, sort, list
#cool idea, if every characterbase has a inventory then we can add a steal function

#TODO, REVISITI WEAPONSBASE(), MAKE CLASS THAT IS FOR EVERY ITEM INGAME THEN
#MAKE SUBSEQUENT CLASS TYPES like weaponsbase() should be rn inheriting item() class

#enemy stun attack debounce not work

def clear():
  os.system("cls") # just clears text on terminal screen
 
def draw(): #draws a neat little line, good for organization and display
  print("X════════════════════════════════════X")

class CharacterBase: # baseplate for all characters, they can attack and have properties
  def __init__(self, health:int, name:str, strength:int, fortitude:int) -> None:
    self.name = name
    self.strength = strength
    self.fortitude = fortitude
    self.health = health
    self.weapon = fist
    self.inventory = InventoryManager() # GIVES CHARACTER A INVENTORY
    self.blocking = False
    self.stun = 0
    
  def attack(self, enemy) -> None:
    if enemy.blocking:
      enemy.health -= self.weapon.damage * (3 - (enemy.fortitude / 100))
      enemy.blocking = False
      print(f"{enemy.name} blocked and took {self.weapon.damage * (3 - (enemy.fortitude / 100))} damage")
    else:
      if self.stun > 0:
          self.stun -= 1
          print(f"{self.name}'s attack is canceled!")
      else:
          enemy.health -= self.weapon.damage * self.strength
          print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {self.weapon.damage * self.strength}") 


  
  def block(self) -> None:
    if self.stun > 0:
      self.stun -= 1
    self.blocking = True
    

  def status_check(self) -> None:
    print("1. Stats")
    print("2. Map")

    statusChoice = input(": ")
    if statusChoice == "1":
          clear()
          print(self.name)
          draw()
          print(f"Health is {self.health}")
          print(f"Fortitude is {self.fortitude}")
          print(f"Strength is {self.strength}")
          print(f"Stun is {self.stun}")
          draw()
    elif statusChoice == "2":
       clear()
       print("1. Player Location")
       print("2. Input Location")

       mapChoice = input(": ")
       if mapChoice == "1":
          clear()
          map.display_player()
       elif mapChoice == "2":
          clear()
          print("Enter x")
          x = input(": ")
          clear()
          print("Enter y")
          y = input(": ")
          clear()
          draw()
          map.display_location(int(x),int(y))
       else:
          clear()
          print("Invalid")
          self.status_check()

    else:
       clear()
       print("Invalid")
       self.status_check()
       
       



class EnemyBase(CharacterBase):

  def __init__(self, health:int, name:str, strength:int, fortitude:int) -> None:
    super().__init__(health, name, strength, fortitude)
    self.stunAttackDebounce = 0

  def stun_attack(self, enemy) -> None:

    if self.stunAttackDebounce > 0:
      self.stunAttackDebounce -= 1
      self.attack(enemy)
    else:
      if enemy.blocking:
        enemy.health -= self.weapon.damage * (3 - (enemy.fortitude / 100))
        enemy.blocking = False
        print(f"{enemy.name} blocked and took {self.weapon.damage * (3 - (enemy.fortitude / 100))} damage")
      else:
        if self.stun > 0:
            self.stun -= 1
            print(f"{self.name}'s attack is canceled!")
        else:
            enemy.health -= self.weapon.damage * self.strength
            print(f"{self.name} attacked {enemy.name} with {self.weapon.name} for {self.weapon.damage * self.strength} and stunned them for 2 turns!") 
            enemy.stun = 2
            self.stunAttackDebounce = 2

class EnemyManager: # IMPLEMENT IFS TO DECIDE WHICH ATTACK IS BEST, BASICALLY ENEMY AI
  def __init__(self,player ,enemy ) -> None:
    self.player = player
    self.enemy = enemy
    self.enemy_turn()


  def enemy_turn(self) -> None:

    if self.enemy.health > 140:
      self.enemy.stun_attack(self.player)
    else:
      self.enemy.attack(self.player)
        
class ItemBase:

  def __init__(self, name:str, category:str, description:str) -> None:
    self.name = name
    self.category = category
    self.description = description

class WeaponBase(ItemBase): # inherits properties from itembase cause weapons are items

  def __init__(self, name:str, category:str, description:str, damage:int) -> None:
    super().__init__(name, category, description)
    self.damage = damage  #adds damage property, so you can make a potion but not need to add dmg

class BiomeManager: #idea is to use this to set custom properties for battle scenes and spawns
  def __init__(self):
    self.enemy_chance = 0
    self.biome_behaviors = {
        "f": self.set_forest,
        "m": self.set_mountain,
        "t": self.set_tavern,
        "g": self.set_grass,
    }

  def convert_biome(self, biomeToConvert):
    if biomeToConvert == "f":
      return "Forest"
    if biomeToConvert == "m":
      return "Mountain"
    if biomeToConvert == "t":
      return "Tavern"
    if biomeToConvert == "g":
      return "Grass"
    
  def interact_with_biome(self, biome):
    if biome in self.biome_behaviors:
        self.biome_behaviors[biome]()
    else:
      print("Error, invalid biome")

  def set_forest(self):
    self.enemy_chance = 30
    print(f"You are in a forest, there is a {self.enemy_chance}% chance of an enemy spawn")

  def set_grass(self):
    self.enemy_chance = 20
    print(f"You are in a grass, there is a {self.enemy_chance}% chance of an enemy spawn")
  
  def set_mountain(self):
    self.enemy_chance = 70
    print(f"You are in a mountain, there is a {self.enemy_chance}% chance of an enemy spawn")
    
  def set_tavern(self):
    self.enemy_chance = 0
    print(f"You are in a tavern, there is a {self.enemy_chance}% chance of an enemy spawn")

class IdleManager:


  def __init__(self) -> None:
    self.turn = 0
    pass

  def handle_input(self):

    print(f"Current location is {map.x,map.y}")
    draw()
    
    print("W A S D: To Move")
    draw()
    print("1. Status")
    draw()


    choice = input(": ")

    if choice.upper() == "W":
        map.y -= 1
        map.explore_tile()
    elif choice.upper() == 'S':
        map.y += 1
        map.explore_tile()
    elif choice.upper() == 'A':
        map.x -= 1
        map.explore_tile()
    elif choice.upper() == 'D':
        map.x += 1
        map.explore_tile()
    else:
        clear()
        self.handle_input()
        print("Invalid Input")


  def idle_action(self):

    self.turn += 1

    playerBiome.interact_with_biome(map.tiles[(map.x,map.y)])
    
    if random.randint(0,100) <= playerBiome.enemy_chance:
      clear()
      BattleSequence(player, EnemyGenerator().generate_Enemy())

    self.handle_input()
 
class BattleSequence:     
  def __init__(self, player, enemy): 
    self.player = player
    self.enemy = enemy
    self.skip_enemy_attack = False # this determines if a move takes a turn or not
    self.start_battle()


  def start_battle(self):
    print("You encounter a " + self.enemy.name + "!")
 
    
    while self.player.health > 0 and self.enemy.health > 0:
        draw()
        print(f"{self.player.name} health: {self.player.health}")
        print(f"{self.enemy.name} health: {self.enemy.health}")
        draw()
        self.player_action()

        if self.skip_enemy_attack:
            self.skip_enemy_attack = False
            continue   

        EnemyManager(self.player,self.enemy)
         

        if self.enemy.health <= 0:
          if self.player.health <= 0:
            print("You both died, game over.")
            quit()
          else: 
            clear()
            
            print("You defeated the " + self.enemy.name + "!")
            draw()
            return
            
        if self.player.health <= 0:
            draw()
            print("You were defeated!")
            quit()
       
          
            
  def player_action(self):
    print("Choose your action")
    print(f"1. Attack {self.player.stun}")
    print("2. Block") 
    print("3. Nothing")
    print("4. Status")
    choice = input(": ")
    
    if choice == "1":
      clear()
      player.attack(self.enemy)
    elif choice == "2":
      clear()
      player.block()
    elif choice == "3":  
      clear()
      pass
    elif choice == "4":
      clear()
      player.status_check()
      input("Continue: ")
      self.skip_enemy_attack = True
      clear()
    else:
      
      clear()
      print("Invalid action")
      self.skip_enemy_attack = True
      pass

class MapManager: #MAP LIST TENDS TO GET VERY VERY LONG DURING LATE GAME STAGE, TRY REDUCE BIOME NAMES
  
  def __init__(self) -> None:
    self.x = 1
    self.y = 1

    self.tiles = {(0, 0): "f", (1, 0): "f", (2, 0): "f", 
          (0, 1): "f", (1, 1): "t", (2, 1): "f", 
          (0, 2): "f", (1, 2): "f", (2, 2): "f", 
    } 

  def explore_tile(self):
    
      if (self.x, self.y) not in self.tiles: # CHECKS IF TILE EXPLORING IS IN TILE LIST (explored)
          self.tiles[(self.x,self.y)] = self.generate_tile()

      else:
        pass

  def display_location(self,x,y):
      view_range = 2
     
      min_y = y - view_range
      max_y = y + view_range
      min_x = x - view_range
      max_x = x + view_range

      for y in range(min_y, max_y + 1): #accounts for index 0

          for x in range(min_x, max_x + 1):
        
              if (x, y) == (self.x, self.y):
                  print("P", end=" ") 
              else:
                  print(self.tiles.get((x, y), "?"), end=" ") #get function for error/missing tiles
          print()  
      draw()

      
     

  def display_player(self): 
        
        # if pos = 0,0 we need to find bottom left corner = -2,-2
        view_range = 2
        min_y = self.y - view_range
        max_y = self.y + view_range
        min_x = self.x - view_range
        max_x = self.x + view_range
        
        
        for y in range(min_y, max_y + 1): #accounts for index 0

            for x in range(min_x, max_x + 1):
          
                if (x, y) == (self.x, self.y):
                    print("P", end=" ") 
                else:
                    print(self.tiles.get((x, y), "?"), end=" ") #get function for error/missing tiles
            print()  
        draw()
      

  def generate_tile(self):
      return random.choice(["g", "f", "m"])
  #f = forest
  #g = grass                                          #IMPORTANT INDEX
  #m = mountain
  #t = tavern

class EnemyGenerator: #THIS CODE NEEDS TO BE IMPROVED TO HAVE ACTUAL RANDOM GENERATION, NOT JUST PREDEFINED
      
  

      def __init__(self):
        pass
      
      
      def generate_Enemy(self):
        return EnemyBase(200, "Goblin", 5, 10)

class InventoryManager:
  
  def __init__(self):
    self.inventory = []

  def add_item(self, item):
    self.inventory.append(item) 

  def drop_item(self, item):
    self.inventory.remove(item)

  def equip_item(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      player.weapon = item
      print(f"You equipped {item.name}.")
    else:
      print("Item not found in inventory.")

 # def list_inventory(self):
    

  def sort_inventory(self):
    pass
  #  self.inventory.sort(key=lambda x: x.name)

def inputFunction(option1, option2, option3):

      choice = input(": ")
      
      if choice == option1:
        return option1
      elif choice == option2:
        return option2
      elif choice == option3:
        return option3
      else:
        return "ERROR" 

fist = WeaponBase(name="Fist", category="Weapon", description="A fist", damage=5)
gameStarted = True
 # MAYBE USE FOR STATUS BASED EFFECTS
print("╔═════════════════════════════════════════════════════╗")
print("║         Welcome to the Kingdom of Aloria            ║")
print("║                                                     ║")
print("║                                                     ║")
print("║            What is your name Traveler?              ║")
print("╚═════════════════════════════════════════════════════╝")
player = CharacterBase(health=375,name=input(": "),strength=10, fortitude=10)
playerBiome = BiomeManager()   #CREATING CLASESS FOR PLAYER, ONLY
map = MapManager()
clear()
gameStarted = True

while gameStarted: 
    # FOR DICT VALUE OF TILE, print(map.tiles[(map.x,map.y)])
    #map.tiles[(map.x,map.y)]

    IdleManager().idle_action()


    clear()





















