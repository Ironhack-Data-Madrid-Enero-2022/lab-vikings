######################################################################################################
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        #print("The stregth of the soldier is: " + str(self.strength))
        return self.strength
    
    def receiveDamage(self, damage):
        #print("The soldier received " + str(damage) + "points of damage")
        #print("Current health: " + str(self.health - damage))
        self.health -= int(damage)

####################################################################################################
# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        #self.damage = damage
        #print("The soldier received " + str(damage) + "points of damage")
        #print("Current health: " + str(self.health - damage))
        self.health = self.health - int(damage)
        if self.health > 0:
            return(f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")

    def battleCry(self):
        return("Odin Owns You All!")
  
##########################################################################################################
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.damage = damage
        
        #print("The soldier received " + str(damage) + "points of damage")
        #print("Current health: " + str(self.health - damage))
        self.health -= int(damage)
        if self.health > 0:
            return(f"A Saxon has received {self.damage} points of damage")
        else:
            return("A Saxon has died in combat")
    

#########################################################################################################################
# War

import random as rd

class War:

    #vikingArmy=[] 
    #saxonArmy=[]

    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        sx = rd.choice(self.saxonArmy)
        vk = rd.choice(self.vikingArmy)
        dm = sx.receiveDamage(vk.attack())
        if "has died" in dm:
            self.saxonArmy.remove(sx)

        return(dm)


    def saxonAttack(self):
        sx = rd.choice(self.saxonArmy)
        vk = rd.choice(self.vikingArmy)
        dm = vk.receiveDamage(sx.attack())
        if "has died" in dm:
            self.vikingArmy.remove(vk)

        return(dm)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return("Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            return("Saxons have fought for their lives and survive another day...")
        else:
            return("Vikings and Saxons are still in the thick of battle.")