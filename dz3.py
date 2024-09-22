class Character:
    def __init__(self, name, health, damage, defence):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def show_stats(self):
        print(self)

    def __str__(self):
        return f"-- {self.name} --\nЗдоров'я: {self.health}\n" \
               f"Шкода: {self.damage}\nЗахист: {self.defence}"

    def take_damage(self, damage):
        actual_damage = max(damage - self.defence, 0)
        self.health = max(self.health - actual_damage, 0)

    def attack(self, target):
        print(f"{self.name} атакує {target.name} і завдає {self.damage} шкоди!")
        target.take_damage(self.damage)
        print(f"У {target.name} залишилося {target.health} здоров'я.\n")

    def is_alive(self):
        return self.health > 0