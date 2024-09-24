from dz3 import Character
from paladin import Paladin

player1 = Character("Vasya", 100, 12,0)
print(player1)

player2 = Paladin("Petya", 110, 3,10, 'undead')
player2.show_stats()

player1.attack(player2)
player2.attack(player1)

print(f"\n{player1}\n{player2}\n")