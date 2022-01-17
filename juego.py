from vikingsClasses import Viking, Saxon, War
import random

clase_list = ["Ras", "Sonia", "Ana", "Antonio", "Cesar", "Diego", "Eva", "Isabel", "Jesus", 
            "Juana", "Marc", "Mario", "Pablo", "Ricardo", "Rodrigo", "Sergio", "Molina", "Victor" ]

clase_modificaciones = clase_list.copy()

guerra = War()

for i in range(int(len(clase_list))):
    sajon = Saxon(random.choice(range(1,501)),random.choice(range(1,501)))
    guerra.addSaxon(sajon)

for i in range(int(len(clase_list))):
    nombre = random.choice(clase_modificaciones)
    if nombre == "Rodrigo":
        Rodrigo = Viking("Rodrigo",1000,1000)
        clase_modificaciones.remove("Rodrigo")
        guerra.addViking(Rodrigo)
    else:
        soldado = Viking(nombre,random.choice(range(1,501)),random.choice(range(1,501)))
        clase_modificaciones.remove(nombre)
        guerra.addViking(soldado)

while guerra.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    turno = random.choice([1,2])
    if turno == 1:
        guerra.saxonAttack()
    else:
        guerra.vikingAttack()

print(guerra.showStatus())