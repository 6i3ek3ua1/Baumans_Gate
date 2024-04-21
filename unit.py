class Unit:
    def __init__(self, name):
        self.params = {}
        self.coord = []
        self.name = name
        self.set_params()
        self.mem_x = 0
        self.mem_y = 0

    def set_params(self):
        if self.name == "Лучник" or self.name == "Лучник1":
            self.params['hp'] = 30
            self.params['attack'] = 50
            self.params['attack_range'] = 5
            self.params['armor'] = 0
            self.params['cost_walk'] = 7
            self.params['alive'] = 1
        elif self.name == "Всадник" or self.name == "Всадник1":
            self.params['hp'] = 60
            self.params['attack'] = 50
            self.params['attack_range'] = 2
            self.params['armor'] = 5
            self.params['cost_walk'] = 10
            self.params['alive'] = 1
        elif self.name == "Мечник" or self.name == "Мечник1":
            self.params['hp'] = 50
            self.params['attack'] = 50
            self.params['attack_range'] = 1
            self.params['armor'] = 10
            self.params['cost_walk'] = 5
            self.params['alive'] = 1
        else:
            raise ValueError("Такого типа юнитов не существует")

    def movement(self, x, y, field):
        if field[self.coord[0]+y][self.coord[1]+x] != '*':
            return 1
        cost = self.params['cost_walk']
        if x == 0:
            if self.coord[0] + y >= 0:
                for i in range(self.coord[0], self.coord[0]+y):
                    if field[i][self.coord[1]] == "@":
                        cost -= 2
                    elif field[i][self.coord[1]] == "#":
                        cost -= 1.5
                    elif field[i][self.coord[1]] == "!":
                        cost -= 1.2
                    else:
                        cost -= 1
                if cost < 0:
                    return 0
                else:
                    return (self.coord[1], self.coord[0] + y, cost)
            else:
                raise IndexError
        elif y == 0:
            if self.coord[1] + x > 0:
                if x > 0:
                    for i in range(self.coord[1], x + self.coord[1]):
                        if field[self.coord[0]][i] == "@":
                            cost -= 2
                        elif field[self.coord[0]][i] == "#":
                            cost -= 1.5
                        elif field[self.coord[0]][i] == "!":
                            cost -= 1.2
                        else:
                            cost -= 1
                    if cost < 0:
                        return 0
                    else:
                        return (self.coord[1] + x, self.coord[0], cost)
                else:
                    for i in range(self.coord[1] + x, self.coord[1]):
                        if field[self.coord[0]][i] == "@":
                            cost -= 2
                        elif field[self.coord[0]][i] == "#":
                            cost -= 1.5
                        elif field[self.coord[0]][i] == "!":
                            cost -= 1.2
                        else:
                            cost -= 1
                    if cost < 0:
                        return 0
                    else:
                        return (self.coord[1] + x, self.coord[0], cost)
            else:
                raise IndexError

    def gamemove(self, field):
        if self.params['hp'] != 0:
            chose = input("Движение будет осуществляться по координате X или по координате Y: ")
            if chose == "X":
                coord_x = int(input("Введите смещение по оси Х: "))
                coord_y = 0
            else:
                coord_y = int(input("Введите смещение по оси Y: "))
                coord_x = 0
            try:
                new_coords = self.movement(coord_x, coord_y, field.field)
                if new_coords == 0:
                    print("Недостаточно очков для перемещения")
                elif new_coords == 1:
                    print("Юнит не может стоят здесь")
                else:
                    field.set_new_coords(new_coords[0], new_coords[1], self.name, self)
                    print(new_coords)
                field.display()
            except IndexError:
                print('Не выходите за карту')

    def game(self, field, bot):
        if self.params['hp'] != 0:
            enemy = self.check_attack(bot)
            if enemy != 0:
                chose_att = input(f"Внимание, боец врага {enemy.name} в зоне поражения\n"
                                      f"желаете атаковать?: ")
                if chose_att == "да":
                    self.attack(enemy)
                    print(f"Вражеский боец {enemy.name} был атакован")
                    field.display()
                else:
                    self.gamemove(field)
            else:
                self.gamemove(field)

    def check_attack(self, bot):
        enemy_units = bot.units
        pr_range_min = 1000
        tow_enemy_unit = 0
        for item in enemy_units:
            diff_x = abs(self.coord[1] - item.coord[1])
            diff_y = abs(self.coord[0] - item.coord[0])
            prosp_range = round((diff_x**2+diff_y**2)**0.5)
            if prosp_range < pr_range_min:
                pr_range_min = prosp_range
                tow_enemy_unit = item
        if pr_range_min <= self.params['attack_range']:
            return tow_enemy_unit
        else:
            return 0

    def attack(self, enemy_unit):
        if enemy_unit.params['armor'] > 0:
            enemy_unit.params['armor'] -= self.params['attack']
        else:
            enemy_unit.params['hp'] -= self.params['attack']

    def die(self, field):
        field.field[self.coord[0]][self.coord[1]] = 'D'
