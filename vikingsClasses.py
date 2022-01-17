
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


class War():  ### NOTA Para esta clase me salen 25 errores. Por las descripciones de los errores; no soy capaz de encontrar los errores.
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
        vka = rd.choice(self.VikingArmy) # We select randomly a viking
        saa = rd.choice(self.saxonArmy)
        rda = saa.receiveDamage(vka.strenght) # Received damaged by a Saxon depends on Viking strength.
        if saa.health <= 0: #If died we remove a Saxon
            saxonArmy.remove(saa)
        else:
            pass
        return [rda, vka.strenght]
    def saxonAttack(self): # This function is simislar to the previous function.
        vka = rd.choice(self.VikingArmy)
        saa = rd.choice(self.saxonArmy)
        rda = vka.receiveDamage(saa.strenght)
        if vka.health <= 0:
            VikingArmy.remove(vka)
        else:
            pass
        return [rda, saa.strenght]
    def showStatus(self):
        if len(saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(VikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif lenlen(saxonArmy) >= 1 and len(VikingArmy) >= 1:
            "Vikings and Saxons are still in the thick of battle."






