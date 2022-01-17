
import random as rd
# Soldier


class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, Damage):
        self.health -= Damage
    

# Viking


class Viking(Soldier):
    def __init__(self, name,  health, strength):
        super().__init__(health, strength)
        self.name = name

    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    
    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    
    def __init__(self,  health, strength):
        super().__init__(health, strength)
    
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    pass

# War


class War():
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        pass

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

        
    def vikingAttack(self):
        vik = rd.choice(self.vikingArmy)
        sax = rd.choice(self.saxonArmy)
        atac = sax.receiveDamage(vik.attack())
        if "has died" in atac:
            self.saxonArmy.remove(sax)
        return atac

    def saxonAttack(self):
        vik = rd.choice(self.vikingArmy)
        sax = rd.choice(self.saxonArmy)
        atac = vik.receiveDamage(sax.attack())
        if "has died" in atac:
            self.vikingArmy.remove(vik)
        return atac

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) != 0 and len(self.vikingArmy) != 0:
            return "Vikings and Saxons are still in the thick of battle."

    pass