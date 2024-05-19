import random
from unit import Unit, Horseman, Sworder, Archer


class Field:
    def __init__(self):
        self.field = [['*' for i in range(15)] for i in range(15)]
        self.set_pr()

    def set_pr(self):
        for i in range(1, 14):
            for j in range(15):
                if random.randint(0, 8) == 1:
                    self.field[i][j] = random.choice(['@', '#', '!'])

    def set_unit(self, unit, wr_sym):
        unit.mem_x = int(input("Введите координату старта: "))
        self.field[0][unit.mem_x] = wr_sym
        unit.coord = [0, unit.mem_x]

    def set_bot_unit(self, wr_sym, unit):
        unit.mem_x = 3
        unit.mem_y = 14
        self.field[14][3] = wr_sym
        unit.coord = [14, 3]

    def set_new_coords(self, x, y, wr_sym, unit):
        if x >= 0 and y >= 0:
            unit.coord = [y, x]
            self.field[y][x] = wr_sym
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        else:
            print('Не выходите за границы карты')

    def buy_unit(self):
        budget = int(input("Введите бюджет закупки: "))
        count_of_units = 0
        units = []
        print("Стоимости солдат:\n"
              "ТИП: \n"
              "Мечник - 10\n"
              "Солдаты этого типа: мечник, топорщик, копьеносец\n"
              "ТИП: \n"
              "Лучник - 12\n"
              "Солдаты этого типа: дл. лук, кор. лук, лучник\n"
              "ТИП: \n"
              "Всадник - 10\n"
              "Солдаты этого типа: всадник, рыцарь, кирасир\n")
        if budget < 10:
            raise ValueError("Дай денек")
        while budget >= 10 and count_of_units <= 3:
            type = input("Введите тип солдата: ")
            if type == "Мечник":
                name = input("Введите имя солдата: ")
                unit = Sworder(name)
                units.append(unit)
                budget -= 10
                self.set_unit(unit, unit.write_sym)
            elif type == "Лучник":
                if budget >= 12:
                    name = input("Введите имя солдата: ")
                    unit = Archer(name)
                    units.append(unit)
                    budget -= 12
                    self.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
            elif type == "Всадник":
                if budget >= 15:
                    name = input("Введите имя солдата: ")
                    unit = Horseman(name)
                    units.append(unit)
                    budget -= 15
                    self.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
        return units

    def display(self):
        for row in self.field:
            print(' '.join(row))
