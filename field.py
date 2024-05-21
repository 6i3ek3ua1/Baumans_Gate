import random


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

    def set_bot_unit(self, wr_sym, unit, x):
        unit.mem_x = x
        unit.mem_y = 14
        self.field[14][x] = wr_sym
        unit.coord = [14, x]

    def set_new_coords(self, x, y, wr_sym, unit):
        if x >= 0 and y >= 0:
            unit.coord = [y, x]
            self.field[y][x] = wr_sym
            self.field[unit.mem_y][unit.mem_x] = "*"
            unit.mem_x = x
            unit.mem_y = y
        else:
            print('Не выходите за границы карты')

    def display(self):
        for row in self.field:
            print(' '.join(row))
