from field import Field
from bot import Bot
from shop import Shop


class GameMenu:
    def __init__(self):
        self.field = Field()
        print("Добро пожаловать в город, путник. Время защищать!")
        self.field.display()
        print("Введите уровень сложности:\n"
              "0 - лёгкий\n"
              "1 - средний\n"
              "2 - ...ладно\n")
        self.diff = int(input())
        self.bot = Bot()
        self.bot.create_bot_unit(self.diff, self.field)
        self.shop = Shop()
        self.units = self.shop.buy_unit(self.field)
        self.field.display()
        self.game_process()

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


            chose = int(input("Выберите, за какого юнита будет совершено действие: "))
            self.units[chose].game(self.field, self.bot)

            print("----------Ход противника!-----------\n")
            alive = self.bot.if_die(self.field)
            if alive == 1:
                check_agr = self.bot.check_around(self.units, count, self.field)
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

            print("----------Ваш ход!-----------\n")

            if len(self.bot.units) == 0:
                print("---------------Вы победили------------------\n"
                      "\tвеликолепная доблесть")
                break

            for item in self.units:
                if item.params['hp'] <= 0:
                    item.die(self.field)
                    self.units.remove(item)

            if len(self.units) == 0:
                print("---------------Вы проиграли------------------\n"
                      "\tбессмысленная жертва")
                break
