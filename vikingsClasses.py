
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
        if self.health > 0:
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
        if self.health > 0:
            return (f"A Saxon has received {self.damage} points of damage")
        else:
            return  (f"A Saxon has died in combat")
    
# War
import random 

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
        self.sax = random.choice(self.saxonArmy)
        self.vik = random.choice(self.vikingArmy)
        self.damageSax = self.sax.receiveDamage(self.vik.attack())
        if self.sax.health <= 0:
            self.saxonArmy.remove(self.sax)
        return self.damageSax 

    def saxonAttack(self):
        self.sax = random.choice(self.saxonArmy)
        self.vik = random.choice(self.vikingArmy)
        self.damageVik = self.vik.receiveDamage(self.sax.attack())
        if self.vik.health <= 0:
            self.vikingArmy.remove(self.vik)
        return self.damageVik    

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return (f"Vikings have won the war of the century!")
        elif len(self.vikingArmy) == 0:
            return (f"Saxons have fought for their lives and survive another day...")
        else:
            len(self.saxonArmy)>0 and len(self.vikingArmy)>0
            return (f"Vikings and Saxons are still in the thick of battle.")