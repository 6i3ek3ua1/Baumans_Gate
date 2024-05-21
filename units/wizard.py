from units.unit import Unit


class Wizard(Unit):
    def __init__(self, name):
        super().__init__(name)
        self.write_sym = "W"
        self.spell1 = {'attack_range_min': 5, 'attack_range_max': 7, 'damage': 50, 'name': 'земляной прорыв'}
        self.spell2 = {'attack_range_min': 4, 'attack_range_max': 8, 'damage': 30, 'name': 'водный удар'}
        self.spell3 = {'attack_range_min': 6, 'attack_range_max': 6, 'damage': 80, 'name': 'огненный шар'}
        self.all_spells = [self.spell1, self.spell2, self.spell3]

    def set_params(self):
        if self.name == "Колдун":
            self.params['hp'] = 40
            self.params['attack'] = 0
            self.params['attack_range'] = 0
            self.params['armor'] = 0
            self.params['cost_walk'] = 5
            self.params['alive'] = 1
        else:
            raise ValueError("Такого типа юнитов не существует")

    def check_attack(self, bot):
        enemy_units = bot.units
        pr_range_min = 1000
        tow_enemy_unit = 0
        spell_list = []
        for spell in self.all_spells:
            for item in enemy_units:
                diff_x = abs(self.coord[1] - item.coord[1])
                diff_y = abs(self.coord[0] - item.coord[0])
                prosp_range = round((diff_x**2+diff_y**2)**0.5)
                if prosp_range < pr_range_min:
                    pr_range_min = prosp_range
                    tow_enemy_unit = item
            if pr_range_min <= spell['attack_range_max']:
                if pr_range_min >= spell['attack_range_min']:
                    spell_list.append(spell)
        if len(spell_list) != 0:
            return (tow_enemy_unit, spell_list)
        else:
            return 0

    def game(self, field, bot):
        if self.params['hp'] != 0:
            enemy = self.check_attack(bot)
            if enemy != 0:
                chose_att = input(f"Внимание, боец врага {enemy[0].name} в зоне поражения\n"
                                      f"желаете атаковать?: ")
                if chose_att == "да":
                    self.mage_attack(enemy[0], enemy[1])
                    print(f"Вражеский боец {enemy[0].name} был атакован")
                    field.display()
                else:
                    self.gamemove(field)
            else:
                self.gamemove(field)

    def mage_attack(self, enemy, number_of_spell):
        print("Выберите заклинание из списка, которым можете атаковать:\n")
        for i in range(0, len(number_of_spell)):
            print(f"{i+1}, {number_of_spell[i]['name']}, (атака - {number_of_spell[i]['damage']})\n")
        chosen_spell = int(input())
        if enemy.params['armor'] > 0:
            enemy.params['armor'] -= number_of_spell[chosen_spell-1]['damage']
        else:
            enemy.params['hp'] -= number_of_spell[chosen_spell-1]['damage']
