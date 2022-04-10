
import random as rd
# Soldier


from re import S
from xml.sax import SAXNotRecognizedException, SAXReaderNotAvailable


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage #Quita a la vida el daño marcado, no lo devuelve, solo modifica.
        pass 
    pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength): #ojo con el orden de los atributos
        super().__init__(health, strength) #Aqui sin name porque class Solider no tiene name
        self.name = name
        pass
    
    def receiveDamage(self, damage):
        self.health -= damage #Quita a la vida el daño marcado, no lo devuelve, solo modifica.
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")

    def battleCry(self):
        return "Odin Owns You All!"

    def attack(self):
        return self.strength
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage #Quita a la vida el daño marcado, no lo devuelve, solo modifica.
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died in combat")
    pass

# War


class War():
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    #Aqui empiezan los metodos
    def addViking(self, viking): # Definimos un viking
        self.vikingArmy.append(viking)
        return

    def addSaxon(self, saxon): # Definimos un viking
        self.saxonArmy.append(saxon)
        return
    

    def vikingAttack(self):
        #rd.choice(self.saxonArmy) = d #Este es el defensor
        #rd.choice(self.vikingArmy) = a #Este es el atacante
        #Hay que hacer un receive Damage al random saxon con la strenght(attack) del random viking
        #(defensor).receiveDamage(daño del viking) , daño es el correspondiente al del vikingo
        damage_dealt = (rd.choice(self.saxonArmy)).receiveDamage((rd.choice(self.vikingArmy).attack())) #Hay que meterlo aqui, ya que hay que restar bajas, no se puede meter en el return
        if rd.choice(self.saxonArmy).health <=0:
            self.saxonArmy.remove(rd.choice(self.saxonArmy))
        return damage_dealt 
    
    def saxonAttack(self):
        damage_dealt = (rd.choice(self.vikingArmy)).receiveDamage((rd.choice(self.saxonArmy).attack()))
        if rd.choice(self.vikingArmy).health <=0:
            self.vikingArmy.remove(rd.choice(self.vikingArmy))
        return damage_dealt 
           
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
