from units.archer import Archer
from units.swordsman import Swordsman
from units.horseman import Horseman
from units.wizard import Wizard
from units.warriorwizard import WarriorWizard


class Shop:
    def __init__(self):
        self.budget = int(input("Введите бюджет закупки: "))
        self.units = []
        self.count_of_units = 0
        print("Стоимости солдат:\n"
              "ТИП: \n"
              "Мечник - 10\n"
              "Солдаты этого типа: мечник, топорщик, копьеносец\n"
              "ТИП: \n"
              "Лучник - 12\n"
              "Солдаты этого типа: дл. лук, кор. лук, лучник\n"
              "ТИП: \n"
              "Всадник - 15\n"
              "Солдаты этого типа: всадник, рыцарь, кирасир\n"
              "Колдун - 17\n"
              "Маг-воин - 20\n")

    def buy_unit(self, field, user):
        if self.budget < 10:
            raise ValueError("Дай денек")
        while self.budget >= 10 and self.count_of_units <= 3:
            type = input("Введите тип солдата: ")
            if type == "Мечник":
                name = input("Введите имя солдата: ")
                unit = Swordsman(name)
                self.units.append(unit)
                self.budget -= 10
                field.set_unit(unit, unit.write_sym)
                self.count_of_units += 1
            elif type == "Лучник":
                if self.budget >= 12:
                    name = input("Введите имя солдата: ")
                    unit = Archer(name)
                    self.units.append(unit)
                    self.budget -= 12
                    field.set_unit(unit, unit.write_sym)
                    self.count_of_units += 1
                else:
                    print("Недостаточно денег")
            elif type == "Всадник":
                if self.budget >= 15:
                    name = input("Введите имя солдата: ")
                    unit = Horseman(name)
                    self.units.append(unit)
                    self.budget -= 15
                    field.set_unit(unit, unit.write_sym)
                    self.count_of_units += 1
                else:
                    print("Недостаточно денег")
            elif type == "Колдун":
                if self.budget >= 17:
                    name = input("Введите имя солдата: ")
                    unit = Wizard(name)
                    self.units.append(unit)
                    self.budget -= 17
                    field.set_unit(unit, unit.write_sym)
                    self.count_of_units += 1
                else:
                    print("Недостаточно денег")
            elif type == "Маг-воин":
                if self.budget >= 20:
                    name = input("Введите имя солдата: ")
                    unit = WarriorWizard(name)
                    self.units.append(unit)
                    self.budget -= 20
                    field.set_unit(unit, unit.write_sym)
                    self.count_of_units += 1
                else:
                    print("Недостаточно денег")
        self.add_new_unit(user, field)
        return self.units

    def add_new_unit(self, user, field):
        if user.new_unit != 0:
            if self.count_of_units <= 3:
                choise = int(input(f"Желаете ли добавить нового юнита {user.new_unit.name} на поле?\n"
                                   f"0 - да\n"
                                   f"1 - нет\n"))
                if choise == 0:
                    self.units.append(user.new_unit)
                    field.set_unit(user.new_unit, user.new_unit.write_sym)
