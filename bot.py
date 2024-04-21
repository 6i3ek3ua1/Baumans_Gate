from unit import Unit


class Bot:
    def __init__(self):
        self.units = [Unit("Мечник1")]

    def create_bot_unit(self, difficulty, field):
        if difficulty == 1:
            unit1 = Unit("Лучник1")
            self.units.append(unit1)
        elif difficulty == 2:
            unit1 = Unit("Лучник1")
            self.units.append(unit1)
            unit2 = Unit("Всадник1")
            self.units.append(unit2)
        elif difficulty != 0:
            raise ValueError("Такой сложности нет")
        for item in self.units:
            field.set_bot_unit(item.name, item)

    def move(self, field, name):
        coords = self.units[name].coord
        if field.field[coords[0]-1][coords[1]] == '*':
            field.set_new_coords(coords[1], coords[0]-1, self.units[name].name, self.units[name])
        else:
            ind = 1
            while field.field[coords[0]-ind][coords[1]] != '*':
                ind += 1
            field.set_new_coords(coords[1], coords[0]-ind, self.units[name].name, self.units[name])

    def check_around(self, units, name, field):
        min_range = 1000
        tow_enemy = 0
        for item in units:
            enemy_coord = item.coord
            diff_x = abs(self.units[name].coord[1] - enemy_coord[1])
            diff_y = abs(self.units[name].coord[0] - enemy_coord[0])
            prosp_range = round((diff_x ** 2 + diff_y ** 2) ** 0.5)
            if prosp_range < min_range:
                min_range = prosp_range
                tow_enemy = item
        if min_range <= 5:
            return (tow_enemy, min_range)
        else:
            return 0

    def move_around(self, name, field, tow_enemy, min_range):
        if min_range > self.units[name].params['attack_range']:
            if self.units[name].coord[1] == tow_enemy.coord[1]:
                self.move(field, name)
            if field.field[self.units[name].coord[0]][tow_enemy.coord[1]] == '*':
                field.set_new_coords(tow_enemy.coord[1], self.units[name].coord[0], self.units[name].name, self.units[name])
            else:
                self.move(field, name)
        else:
            self.units[name].attack(tow_enemy)
            print(f"Ваш боец {tow_enemy.name} был атакован!!!")

    def if_die(self, field):
        for item in self.units:
            if item.params['hp'] <= 0:
                print(f'боец врага {item.name} убит')
                field.field[item.coord[0]][item.coord[1]] = 'D'
                self.units.remove(item)
                return 0
            else:
                return 1