from dz3 import Character

player1 = Character("Vasya", 100, 105, 0)
print(player1)

player2 = Character("Petya", 100, 3, 2)

def main():
    player1 = Character("Vasya", 100, 15, 3)
    player2 = Character("Petya", 100, 12, 2)

    print("Початкові стати гравців:")
    player1.show_stats()
    player2.show_stats()

    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if player2.is_alive():
            player2.attack(player1)

    if player1.is_alive():
        print(f"{player1.name} переміг!")
    else:
        print(f"{player2.name} переміг!")


if __name__ == "__main__":
    main()