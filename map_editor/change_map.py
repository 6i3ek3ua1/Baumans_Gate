from create_map import CreatorMap
import os
import json


class ChangeMap(CreatorMap):
    def __init__(self):
        self.map_list = os.listdir("maps")
        print(f"Список карт: {self.map_list}")
        self.chosen_map = input("Выберите, какую карту желаете изменить (введите название без .txt): ")
        with open("maps\\" + self.chosen_map + ".txt", "r", encoding="utf-8") as f:
            self.json_map = json.load(f)
            self.field = self.json_map["field"]
        print("Выбранная карта: ")
        self.display()
        chose = int(input("1 - добавить новое препятствие\n"
                          "2 - случайное пересоздание карты из базовых препятствий\n"
                          "3 - изменение карты с базовыми препятствиями\n"))
        self.new_symbols = {}
        if chose == 1:
            self.set_new_obstacle()
        elif chose == 2:
            self.set_pr()
        elif chose == 3:
            self.create_base_field()
        print("Полученное поле:")
        self.display()
        self.save_in_file()

    def set_new_obstacle(self):
        flag = 1
        while flag != 0:
            new_sym = input("Введите символ препятствия: ")
            if len(new_sym) != 1:
                new_sym = new_sym[0]
            new_penalty = float(input("Введите, сколько очков перемещения необходимо для преодоления препятствия: "))
            self.new_symbols[new_sym] = new_penalty
            flag = int(input("Символ добавлен\n"
                            "0 - сохранение карты\n"
                            "1 - добавить ещё одно препятствие\n"))
        for key in self.new_symbols.keys():
            self.set_sym_on_field(key)

    def create_base_field(self):
        base_symbols = ['!', '#', '@']
        for sym in base_symbols:
            self.set_sym_on_field(sym)

    def save_in_file(self):
        self.json_map = {'field': self.field, 'new_symbols': self.new_symbols}
        with open(f"maps\\{self.chosen_map}.txt", 'w') as file:
            json.dump(self.json_map, file)
