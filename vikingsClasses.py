
# Soldier


class Soldier():
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health>0:
            return (f"{self.name} has received {self.damage} points of damage")
        else:
            return  (f"{self.name} has died in act of combat")
    def battleCry(self):
        return (f"Odin Owns You All!")

# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health>0:
            return (f"A Saxon has received {self.damage} points of damage")
        else:
                return  (f"A Saxon has died in combat")
    
# War
import random as rd

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.addviking = viking
        self.vikingArmy.append(self.addviking)

    def addSaxon(self, saxon):
        self.addsaxon = saxon
        self.saxonArmy.append(self.addsaxon)

    def vikingAttack(self):
        self.sax = rd.choice(self.saxonArmy)
        self.vik = rd.choice(self.vikingArmy)

        self.damage_sx = self.sax.receiveDamage(vik)
        return self.damage_sx

    def saxonAttack(self):
        self.damage_vk = self.vik.receiveDamage()
        return self.damage_vk      

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return (f"Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            return (f"Saxons have fought for their lives and survive another day..")
        else:
            return (f"Vikings and Saxons are still in the thick of battle.")