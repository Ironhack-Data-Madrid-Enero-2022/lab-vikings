
# Soldier


class Soldier:
    def __init__(self,health,strength):
         self.health = health
         self.strength = strength   
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health = self.health - damage
# Viking


class Viking:
    def __init__(self,name,health,strenght):
        self.name = name
        self.health = health
        self.strenght = strength
    def attack(self)




# Saxon


class Saxon:
    pass

# War


class War:
    pass