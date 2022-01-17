from vikingsClasses import War, Viking, Saxon
import random as rd
import re
# We are going to generate 2 armies, that are going to fight each other,
# Let's create a list with the names of the viking army,
#first let's ask the player how many vikings are going to fight,
a = input('How many vikings are going to fight? ')
a = re.sub(' ','', a)

while type(a) != int:
    if re.findall('[a-z ,]', a) == []:
        a = int(a)
    else:
        a = input('That was not a number. How many vikings are going to fight? ')
        a = re.sub(' ','', a)

Names = []
for count in range(a):
    Names.append(input('What is your name Soldier?  '))

atack = [i for i in range(5,40, 5)]
health = [i for i in range(200,700, 50)]

# Let's create a war,
guerra = War()

# Now, the armies,
for Name in Names:
    vikingo = Viking(Name, rd.choice(health), rd.choice(atack))
    guerra.addViking(vikingo)
    sajon = Saxon(rd.choice(health), rd.choice(atack))
    guerra.addSaxon(sajon)

# Let's ask the player to guess the winer,
string = input('Who do you think is going to win? ')
if re.match('(?i).+k.+', string) == None: # We search for a k in the string, as long as there is a k we will consider the choice to be: VIKIGNS
    Saxon_win = True
else:
    Saxon_win = False

# LET THE WAR BEGIN!
whoattacks = ['V','S']
while guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    if rd.choice(whoattacks) == 'V': # then the viking attack
        atac = guerra.vikingAttack()
        if "has died" in atac:
            print(atac)
    else:
        atac = guerra.saxonAttack()
        if "has died" in atac:
            print(atac)
result_war = guerra.showStatus() 
if "Vikings" in result_war:
    if Saxon_win == True:
        print('You suck and Vikings won the War')
    else:
        print('Vikins, obviously, won the war! May Odin be with you!!! Sköl!')
else:
    if Saxon_win == True:
        print('You were right, vikings lost this time, but you suck for not trusting them.')
    else:
        print('Vikings lost the battle, they are vikings though so they won in the game of life.')