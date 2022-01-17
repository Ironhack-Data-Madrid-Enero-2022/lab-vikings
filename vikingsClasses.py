
# Soldier


from xml.sax import SAXException


class Soldier():
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self,damage):
        self.damage = damage
        self.health = self.health - self.damage
        pass
    
 # Viking

class Viking(Soldier):
    def __init__(self,name,health,strenght):
        super().__init__(health,strenght)
        self.name = name

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if (self.health) > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"

class Saxon(Soldier):
    def __init__(self,health,strenght):
        super().__init__(health,strenght)
    
    def receiveDamage(self, damage):
        self.health=self.health- damage
        if (self.health) >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    

import random as rd

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
            
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
              
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):

        vikk = rd.choice(self.vikingArmy)
        saxx = rd.choice(self.saxonArmy)
        dmg = saxx.receiveDamage(vikk.attack())
        if saxx.health <=0:
            self.saxonArmy.remove(saxx)
        return dmg
            
    def saxonAttack(self):
        vikk = rd.choice(self.vikingArmy)
        saxx = rd.choice(self.saxonArmy)
        dmg = vikk.receiveDamage(saxx.attack())
        if vikk.health <=0:
            self.vikingArmy.remove(vikk)
        return dmg

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive   another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."