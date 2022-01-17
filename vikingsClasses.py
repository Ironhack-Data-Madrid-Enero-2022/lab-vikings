
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
        self.damage=damage
        self.health=self.health-self.damage
        if (self.health) >0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return"Odin Owns You All!"
        pass 


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
            pass

# War
import random
class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Sajon=random.choice(self.saxonArmy)
        Vikingo=random.choice(self.vikingArmy)
        damage= Sajon.receiveDamage(Vikingo.attack())
        if Sajon.health<=0:
            self.saxonArmy.remove(Sajon)
        return damage
    def saxonAttack(self):
        Sajon=random.choice(self.saxonArmy)
        Vikingo=random.choice(self.vikingArmy)
        damage= Vikingo.receiveDamage(Sajon.attack())
        if Vikingo.health<=0:
            self.vikingArmy.remove(Vikingo)
        return damage

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."
        