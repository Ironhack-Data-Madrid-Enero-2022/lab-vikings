
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage= damage
        self.health= self.health - self.damage
        pass

# Viking

class Viking(Soldier):
    def __init__(self,name,health,strenght):
        super().__init__(health,strenght)
        self.name=name
    def receiveDamage(self,damage):
        self.health=self.health- damage
        if (self.health-damage) >0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return"Odin Owns You All!"
        






# Saxon


class Saxon(Soldier):
    def __init__(self,health,strenght):
        super().__init__(health,strenght)
    def receiveDamage(self, damage):
        self.health=self.health- damage
        if (self.health) >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War

import random
class War():
    
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)
        

    def addSaxon(self, Saxon):
     
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        vkk = random.choice(self.vikingArmy)
        sxx = random.choice(self.saxonArmy)
        dmg = sxx.receiveDamage(vkk.attack())
        if (sxx.health) <=  0:
            self.saxonArmy.remove(sxx)
        return dmg

    def saxonAttack(self):
        vkk = random.choice(self.vikingArmy)
        sxx = random.choice(self.saxonArmy)
        dmg = vkk.receiveDamage(sxx.attack())
        if (vkk.health) <=  0:
            self.vikingArmy.remove(vkk)
        return dmg
    
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        else:
            return f"Vikings and Saxons are still in the thick of battle."
           


