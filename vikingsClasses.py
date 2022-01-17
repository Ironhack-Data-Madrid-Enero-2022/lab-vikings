
# Soldier


class Soldier:


    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health =self.health - self.damage
        pass


# Viking


class Viking (Soldier):
    
     def __init__(self, name, health, strenght):
        super().__init__(health,strenght)
        self.name = name
     def receiveDamage(self, damage):
         self.health = self.health - damage
         if (self.health) >0:
             return f"{self.name} has received {damage} points of damage"
         else:
             return f"{self.name} has died in act of combat"
     def battleCry(self):
         return "Odin Owns You All!"


# Saxon


class Saxon (Soldier):
    def __init__(self, health, strenght):
        super().__init__(health, strenght) 
    def receiveDamage(self, damage):
        self.health =self.health - damage
        if (self.health) >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    
# War


class War:
import random as rd
    def __init__(self):
        vikingArmy = []
        saxonArmy = []
    def addViking(self, Viking):
        self.VikingArmy.append(Viking)
        pass
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        pass
    def vikingAttack(self):
        vka = rd.choice(self.VikingArmy)
        saa = rd.choice(self.saxonArmy)
        rda = saa.receiveDamage(self.VikingArmy)
        if saa.health <= 0:
        




