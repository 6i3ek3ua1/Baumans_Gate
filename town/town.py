class Town:
    def __init__(self, user):
        self.user = user
        print("Добро пожаловать в город!\n"
              "1 - Желаете купить здания\n"
              "2 - Просмотреть построенные в вашем городе здания\n"
              "3 - Выйти на поле боя\n")
        chose = int(input())
        while chose != 3:
            if chose == 1:
                self.buy_buildings()
                print("1 - Желаете купить здания\n"
                      "2 - Просмотреть построенные в вашем городе здания\n"
                      "3 - Выйти на поле боя\n")
                chose = int(input())
            if chose == 2:
                for key, value in self.user.buildings.items():
                    if value.status == 1:
                        print(f"Ваше здание: {key}")
                        visit = int(input("Желаете посетить здание?\n"
                                          "0 - да\n"
                                          "1 - нет\n"))
                        if visit == 0:
                            value.visiting(user)
                print("1 - Желаете купить здания\n"
                      "2 - Просмотреть построенные в вашем городе здания\n"
                      "3 - Выйти на поле боя\n")
                chose = int(input())
        if user.buildings['workshop'].status == 1:
            user.buildings['workshop'].pay_tax(user)

    def buy_buildings(self):
        print(f"Ваш текущий баланс - {self.user.wallet}\n"
              f"Какие здания вы хотите купить?\n"
              f"0 - дом лекаря\n"
              f"1 - арсенал\n"
              f"2 - кузница\n"
              f"3 - таверна\n"
              f"4 - академия\n"
              f"5 - рынок\n"
              f"6 - ремесленная мастерская\n"
              f"стоимость постройки здания - 5 деревьев, 10 камней\n")
        num_buildings = int(input())
        if num_buildings == 0 and self.user.buildings['doctor_house'].status == 0:
            self.user.buy_doctors_house()
        elif num_buildings == 1 and self.user.buildings['arsenal'].status == 0:
            self.user.buy_arsenal()
        elif num_buildings == 2 and self.user.buildings['forge'].status == 0:
            self.user.buy_forge()
        elif num_buildings == 3 and self.user.buildings['tavern'].status == 0:
            self.user.buy_tavern()
        elif num_buildings == 4 and self.user.buildings['academy'].status == 0:
            self.user.buy_academy()
        elif num_buildings == 5 and self.user.buildings['market'].status == 0:
            self.user.buy_market()
        elif num_buildings == 6 and self.user.buildings['workshop'].level < 3:
            self.user.buy_workshop()
