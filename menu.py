from field import Field
from bot import Bot


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
        self.units = self.field.buy_unit()
        self.field.display()
        self.game_process(self.units, self.bot, self.field)

    def game_process(self, units, bot, field):
        count = 0
        while True:
            print("Ваши бойцы:\n")
            for i in range(0, len(units)):
                print(f"Имя {units[i].name}")
                print(f"Здоровье: {units[i].params['hp']}")
                print(f"Номер по порядку: {i}")
                print(f"wr_sym = {units[i].write_sym}")

            print("\nБойцы врага\n")
            for item in bot.units:
                print(f'Имя {item.name}')
                print(f"Здоровье: {item.params['hp']}")


            chose = int(input("Выберите, за какого юнита будет совершено действие: "))
            units[chose].game(field, bot)

            print("----------Ход противника!-----------\n")
            alive = bot.if_die(field)
            if alive == 1:
                check_agr = bot.check_around(units, count, field)
                if check_agr != 0:
                    bot.move_around(count, field, check_agr[0], check_agr[1])
                    count -= 1
                else:
                    bot.move(field, count)
                count += 1
                if count > len(bot.units)-1:
                    count = 0
                field.display()
                print("ВАШИ БОЙЦЫ:\n")
                for i in range(0, len(units)):
                    print(f"Имя {units[i].name}")
                    print(f"Здоровье: {units[i].params['hp']}")
                    print(f"Номер по порядку: {i}\n")

                print("\nБОЙЦЫ ВРАГА:\n")
                for item in bot.units:
                    print(f'Имя {item.name}')
                    print(f"Здоровье: {item.params['hp']}\n")

            print("----------Ваш ход!-----------\n")

            if len(bot.units) == 0:
                print("---------------Вы победили------------------\n"
                      "\tвеликолепная доблесть")
                break

            for item in units:
                if item.params['hp'] <= 0:
                    item.die(field)
                    units.remove(item)

            if len(units) == 0:
                print("---------------Вы проиграли------------------\n"
                      "\tбессмысленная жертва")
                break
