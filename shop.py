from units.archer import Archer
from units.swordsman import Swordsman
from units.horseman import Horseman
from units.wizard import Wizard
from units.warriorwizard import WarriorWizard


class Shop:
    def __init__(self):
        self.budget = int(input("Введите бюджет закупки: "))
        self.units = []
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

    def buy_unit(self, field):
        count_of_units = 0
        if self.budget < 10:
            raise ValueError("Дай денек")
        while self.budget >= 10 and count_of_units <= 3:
            type = input("Введите тип солдата: ")
            if type == "Мечник":
                name = input("Введите имя солдата: ")
                unit = Swordsman(name)
                self.units.append(unit)
                self.budget -= 10
                field.set_unit(unit, unit.write_sym)
            elif type == "Лучник":
                if self.budget >= 12:
                    name = input("Введите имя солдата: ")
                    unit = Archer(name)
                    self.units.append(unit)
                    self.budget -= 12
                    field.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
            elif type == "Всадник":
                if self.budget >= 15:
                    name = input("Введите имя солдата: ")
                    unit = Horseman(name)
                    self.units.append(unit)
                    self.budget -= 15
                    field.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
            elif type == "Колдун":
                if self.budget >= 17:
                    name = input("Введите имя солдата: ")
                    unit = Wizard(name)
                    self.units.append(unit)
                    self.budget -= 17
                    field.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
            elif type == "Маг-воин":
                if self.budget >= 20:
                    name = input("Введите имя солдата: ")
                    unit = WarriorWizard(name)
                    self.units.append(unit)
                    self.budget -= 20
                    field.set_unit(unit, unit.write_sym)
                else:
                    print("Недостаточно денег")
        return self.units
