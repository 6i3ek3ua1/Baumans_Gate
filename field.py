import random
from unit import Unit


class Field:
    def __init__(self):
        self.field = [['*' for i in range(15)] for i in range(15)]
        self.set_pr()

    def set_pr(self):
        for i in range(1, 14):
            for j in range(15):
                if random.randint(0, 8) == 1:
                    self.field[i][j] = random.choice(['@', '#', '!'])

    def set_unit(self, name, unit):
        if name == "Мечник":
            unit.mem_x = int(input("Введите координату старта: "))
            self.field[0][unit.mem_x] = "0"
            unit.coord = [0, unit.mem_x]
        elif name == "Лучник":
            unit.mem_x = int(input("Введите координату старта: "))
            self.field[0][unit.mem_x] = "1"
            unit.coord = [0, unit.mem_x]
        elif name == "Всадник":
            unit.mem_x = int(input("Введите координату старта: "))
            self.field[0][unit.mem_x] = "2"
            unit.coord = [0, unit.mem_x]

    def set_bot_unit(self, name, unit):
        if name == "Мечник1":
            unit.mem_x = 3
            unit.mem_y = 14
            self.field[14][3] = "S"
            unit.coord = [14, 3]
        elif name == "Лучник1":
            unit.mem_x = 7
            unit.mem_y = 14
            self.field[14][7] = "A"
            unit.coord = [14, 7]
        elif name == "Всадник1":
            unit.mem_x = 11
            unit.mem_y = 14
            self.field[14][11] = "H"
            unit.coord = [14, 11]

    def set_new_coords(self, x, y, name, unit):
        if name == "Мечник":
            unit.coord = [y, x]
            self.field[y][x] = "0"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        elif name == "Лучник":
            unit.coord = [y, x]
            self.field[y][x] = "1"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        elif name == "Всадник":
            unit.coord = [y, x]
            self.field[y][x] = "2"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        elif name == "Мечник1":
            unit.coord = [y, x]
            self.field[y][x] = "S"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        elif name == "Лучник1":
            unit.coord = [y, x]
            self.field[y][x] = "A"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        elif name == "Всадник1":
            unit.coord = [y, x]
            self.field[y][x] = "H"
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y

    def buy_unit(self):
        budget = int(input("Введите бюджет закупки: "))
        count_of_units = 0
        units = []
        print("Стоимости солдат:\n"
              "Мечник - 10\n"
              "Лучник - 12\n"
              "Всадник - 15\n")
        if budget < 10:
            raise ValueError("Дай денек")
        while budget >= 10 and count_of_units <= 3:
            name = input("Введите имя солдата: ")
            if name == "Мечник":
                unit = Unit(name)
                units.append(unit)
                budget -= 10
                self.set_unit(name, unit)
            elif name == "Лучник":
                if budget >= 12:
                    unit = Unit(name)
                    units.append(unit)
                    budget -= 12
                    self.set_unit(name, unit)
                else:
                    print("Недостаточно денег")
            elif name == "Всадник":
                if budget >= 15:
                    unit = Unit(name)
                    units.append(unit)
                    budget -= 15
                    self.set_unit(name, unit)
                else:
                    print("Недостаточно денег")
        return units

    def display(self):
        for row in self.field:
            print(' '.join(row))
