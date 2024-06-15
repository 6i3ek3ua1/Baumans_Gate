import pickle
from field import Field
from bot import Bot
from shop import Shop
from user import User
from town.town import Town


class GameMenu:
    def __init__(self):
        print("Добро пожаловать в город, путник. Время защищать!\n")
        choose = int(input("Желаете авторизоваться или создать нового пользователя?\n"
                           "0 - авторизоваться\n"
                           "1 - зарегестрироваться\n"))
        if choose == 0:
            name = input("Введите логин\n")
            password = input("Введите пароль\n")
            with open(f"users\\{name}.pickle", "rb") as file:
                self.user = pickle.load(file)
                if self.user.password == password:
                    self.town = Town(self.user)
                    self.field = Field()
                    self.field.display()
                    print("Введите уровень сложности:\n"
                          "0 - лёгкий\n"
                          "1 - средний\n"
                          "2 - ...ладно\n")
                    self.diff = input()
                    self.bot = Bot()
                    self.bot.create_bot_unit(self.diff, self.field)
                    self.shop = Shop()
                    self.units = self.shop.buy_unit(self.field, self.user)
                    self.field.display()
                    self.user.getting_buffs(self.units)
                    self.user.save()
                    self.result = 0
                else:
                    print("Пароль неверный\n")
        else:
            name = input("Введите логин\n")
            password = input("Введите пароль\n")
            self.user = User(name, password)
            self.user.wallet['wood'] = 20
            self.user.wallet['rock'] = 20
            self.town = Town(self.user)
            self.field = Field()
            self.field.display()
            print("Введите уровень сложности:\n"
                  "0 - лёгкий\n"
                  "1 - средний\n"
                  "2 - ...ладно\n")
            self.diff = input()
            self.bot = Bot()
            self.bot.create_bot_unit(self.diff, self.field)
            self.shop = Shop()
            self.units = self.shop.buy_unit(self.field, self.user)
            self.field.display()
            self.user.getting_buffs(self.units)
            self.user.save()
            self.result = 0

    def game_process(self):
        count = 0
        while True:
            print("Ваши бойцы:\n")
            for i in range(0, len(self.units)):
                print(f"Имя {self.units[i].name}")
                print(f"Здоровье: {self.units[i].params['hp']}")
                print(f"Номер по порядку: {i}")
                print(f"wr_sym = {self.units[i].write_sym}")

            print("\nБойцы врага\n")
            for item in self.bot.units:
                print(f'Имя {item.name}')
                print(f"Здоровье: {item.params['hp']}")
                print(f"Броня: {item.params['armor']}")


            chose = int(input("Выберите, за какого юнита будет совершено действие: "))
            self.costing = self.units[chose].game(self.field, self.bot)

            print("----------Ход противника!-----------\n")
            alive = self.bot.if_die(self.field)
            if count > len(self.bot.units) - 1:
                count = 0
            if alive == 1:
                check_agr = self.bot.check_around(self.units, count)
                if check_agr != 0:
                    self.bot.move_around(count, self.field, check_agr[0], check_agr[1])
                    count -= 1
                else:
                    self.bot.move(self.field, count)
                count += 1
                if count > len(self.bot.units)-1:
                    count = 0
                print("ВАШИ БОЙЦЫ:\n")
                for i in range(0, len(self.units)):
                    print(f"Имя {self.units[i].name}")
                    print(f"Здоровье: {self.units[i].params['hp']}")
                    print(f"Номер по порядку: {i}\n")

                print("\nБОЙЦЫ ВРАГА:\n")
                for item in self.bot.units:
                    print(f'Имя {item.name}')
                    print(f"Здоровье: {item.params['hp']}\n")

            self.field.display()

            print("----------Ваш ход!-----------\n")

            if len(self.bot.units) == 0:
                self.result = "---------------Вы победили------------------\nвеликолепная доблесть"
                print(self.result)
                break

            for item in self.units:
                if item.params['hp'] <= 0:
                    item.die(self.field)
                    self.units.remove(item)

            if len(self.units) == 0:
                self.result = "---------------Вы проиграли------------------\nбессмысленная жертва"
                print(self.result)
                break

    def test_cost(self):
        chose = int(input("Выберите, за какого юнита будет совершено действие: "))
        self.costing = self.units[chose].game(self.field, self.bot)

    def test_attack(self):
        chose = int(input("Выберите, за какого юнита будет совершено действие: "))
        self.costing = self.units[chose].game(self.field, self.bot)

    def test_death(self):
        chose = int(input("Выберите, за какого юнита будет совершено действие: "))
        self.costing = self.units[chose].game(self.field, self.bot)
        chose = int(input("Выберите, за какого юнита будет совершено действие: "))
        self.costing = self.units[chose].game(self.field, self.bot)
        alive = self.bot.if_die(self.field)
        self.field.display()
        return alive
