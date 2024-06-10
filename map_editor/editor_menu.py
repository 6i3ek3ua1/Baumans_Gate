from map_editor.create_map import CreatorMap
from map_editor.change_map import ChangeMap
import os


class Menu:
    def __init__(self):
        self.edit_process()
        self.status = 1
        self.list_of_maps = []

    def edit_process(self):
        self.list_of_maps = os.listdir('maps')
        print("Добро пожаловать в редактор карт!")
        print(f"Существующие карты: {self.list_of_maps}")
        status = int(input("Выберите:\n"
                           "1 - создать карту\n"
                           "2 - изменить существующую карту\n"
                           "3 - удалить карту\n"
                           "0 - выйти из программы\n"))
        while status != 0:
            if status == 1:
                new_map = CreatorMap()
            elif status == 2:
                new_map = ChangeMap()
            elif status == 3:
                self.delete_map()
            status = int(input("Выберите:\n"
                                "1 - создать карту\n"
                                "2 - изменить существующую карту\n"
                                "3 - удалить карту\n"
                                "0 - выйти из программы\n"))
            self.list_of_maps = os.listdir('maps')
            print(f"Существующие карты: {self.list_of_maps}")

    def delete_map(self):
        name_map_delete = input("Введите название карты, которую хотие удалить: ")
        path = 'maps\\' + name_map_delete + '.txt'
        os.remove(path)
