from units.unit import NewUnit


class Building:
    def __init__(self):
        self.status = 0
        self.cost_wood = 10
        self.cost_rock = 5
        self.level = 1
        self.max_level = 3
        self.parameter = ''

    def buying(self, user):
        if self.cost_wood <= user.wallet['wood'] and self.cost_rock <= user.wallet['rock']:
            self.status = 1
            user.wallet['wood'] -= self.cost_wood
            user.wallet['rock'] -= self.cost_rock
        else:
            print('Не хватает братишк((')

class DoctorHouse(Building):
    def __init__(self):
        super().__init__()
        self.boost = 5
        self.name = 'Дом лекаря'
        self.parameter = 'hp'

    def visiting(self, user):
        if self.status == 1:
            print("Вы посетили домик лекаря\n"
                  "Cтоимость улучшения: 10 камней, 10 деревьев\n")
            chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                       "1 - улучшить постройку\n"))
            if chose_to_boost > 0 and self.level < self.max_level:
                self.level += 1
                self.boost += 5
                user.wallet['rock'] -= 10
                user.wallet['wood'] -= 10
            else:
                print(f"Характеристики здания:\n"
                      f"название -  {self.name}\n"
                      f"уровень - {self.level}\n"
                      f"буст здоровья - {self.boost}\n")


class Forge(Building):
    def __init__(self):
        super().__init__()
        self.boost = 5
        self.name = 'Кузница'
        self.parameter = 'attack'

    def visiting(self, user):
        if self.status == 1:
            print("Вы посетили кузницу\n"
                  "Cтоимость улучшения: 10 камней, 10 деревьев\n")
            chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                       "1 - улучшить постройку\n"))
            if chose_to_boost > 0 and self.level < self.max_level:
                self.level += 1
                self.boost += 5
                user.wallet['rock'] -= 10
                user.wallet['wood'] -= 10
            else:
                print(f"Характеристики здания:\n"
                      f"название -  {self.name}\n"
                      f"уровень - {self.level}\n"
                      f"буст атаки - {self.boost}\n")


class Arsenal(Building):
    def __init__(self):
        super().__init__()
        self.boost = 5
        self.name = 'Арсенал'
        self.parameter = 'armor'

    def visiting(self, user):
        if self.status == 1:
            print("Вы посетили арсенал\n"
                  "Cтоимость улучшения: 10 камней, 10 деревьев\n")
            chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                       "1 - улучшить постройку\n"))
            if chose_to_boost > 0 and self.level < self.max_level:
                self.level += 1
                self.boost += 5
                user.wallet['rock'] -= 10
                user.wallet['wood'] -= 10
            else:
                print(f"Характеристики здания:\n"
                      f"название -  {self.name}\n"
                      f"уровень - {self.level}\n"
                      f"буст брони - {self.boost}\n")


class Tavern(Building):
    def __init__(self):
        super().__init__()
        self.boost = 1
        self.name = 'Таверна'
        self.parameter = 'cost_walk'

    def visiting(self, user):
        if self.status == 1:
            print("Вы посетили таверну\n"
                  "Cтоимость улучшения: 10 камней, 10 деревьев\n")
            chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                       "1 - улучшить постройку\n"))
            if chose_to_boost > 0 and self.level < self.max_level:
                self.level += 1
                self.boost += 1
                user.wallet['rock'] -= 10
                user.wallet['wood'] -= 10
            else:
                print(f"Характеристики здания:\n"
                      f"название -  {self.name}\n"
                      f"уровень - {self.level}\n"
                      f"буст ходьбы - {self.boost}\n")


class Market(Building):
    def __init__(self):
        super().__init__()
        self.parameter = 0
        self.name = "Рынок"

    def visiting(self, user):
        if self.status == 1:
            print("Вы посетили рынок\n"
                  "Желаете совершить обмен?\n")
            chose = int(input("0 - Обменять камень на дерево (курс 1 к 2)\n"
                              "1 - Обменять дерево на камень (курс 2 к 1)\n"))
            if chose == 0:
                rock1 = int(input("Сколько камня желаете обменять?\n"))
                user.wallet['rock'] -= rock1
                user.wallet['wood'] += rock1*2
            else:
                wood1 = int(input("Сколько дерева желаете обменять?\n"))
                user.wallet['wood'] -= wood1
                user.wallet['rock'] += wood1 / 2


class Workshop(Building):
    def __init__(self):
        super().__init__()
        self.tax = 5
        self.parameter = 0
        self.name = "Мастерская"

    def pay_tax(self, user):
        if self.status == 1:
            user.wallet['rock'] += self.tax
            user.wallet['wood'] += self.tax

    def visiting(self, user):
        print(self.name)
        print("Вы посетили таверну\n"
              "Cтоимость постройки: 10 камней, 10 деревьев\n")
        chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                   "1 - улучшить постройку\n"))
        if chose_to_boost > 0 and self.level < self.max_level:
            self.level += 1
            user.wallet['rock'] -= 10
            user.wallet['wood'] -= 10
            self.tax += 5
        else:
            print(f"Характеристики здания:\n"
                  f"название - {self.name}\n"
                  f"количество зданий - {self.level}\n")


class Academy(Building):
    def __init__(self):
        super().__init__()
        self.new_unit = 0
        self.parameter = 0
        self.name = "Академия"

    def visiting(self, user):
        print("Вы посетили академию\n"
              "Cтоимость создания юнита: 10 камней, 10 деревьев\n")
        chose_to_boost = int(input("0 - просмотреть характеристики\n"
                                   "1 - создать юнита\n"))
        if chose_to_boost > 0:
            print("Введите параметры: ")
            name = input("Имя: ")
            self.new_unit = NewUnit(name)
            attack = int(input("Атака: "))
            hp = int(input("Здоровье: "))
            cost_walk = int(input("Очки передвижения: "))
            attack_range = int(input("Радиус атаки: "))
            armor = int(input("Броня: "))
            self.new_unit.params = {'hp': hp, 'attack': attack, 'attack_range': attack_range, 'armor': armor,
                                    'cost_walk': cost_walk, 'alive': 1}
            self.new_unit.write_sym = input("Введите как он будет обозначаться на поле")
            user.wallet['rock'] -= 10
            user.wallet['wood'] -= 10
        else:
            print(f"Характеристики здания:\n"
                  f"название -  {self.name}\n"
                  f"новый юнит - {self.new_unit}\n")
