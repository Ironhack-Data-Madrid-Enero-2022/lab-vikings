
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"


    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War
import random as rd

class War:
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
        dmg = sx.receiveDamage(vk.attack())
        if sx.health < int(dmg):
            self.saxonArmy.remove(sx)
        return f"result of calling {sx.receiveDamage(vk.attack())} of a {sx}"

    def saxonAttack(self):
        sx = rd.choice(self.saxonArmy)
        vk = rd.choice(self.vikingArmy)
        dmg = vk.receiveDamage(sx.attack())
        if vk.health < int(dmg):
            self.vikingArmy.remove(vk)
        return f"result of calling {vk.receiveDamage(sx.attack())} of a {vk}"

    def showStatus():
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
        






    

    
