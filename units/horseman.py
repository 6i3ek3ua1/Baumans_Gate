from units.unit import Unit


class Horseman(Unit):
    def __init__(self, name):
        super().__init__(name)
        self.write_sym = "В"

    def set_params(self):
        if self.name == "Рыцарь":
            self.params['hp'] = 40
            self.params['attack'] = 55
            self.params['attack_range'] = 2
            self.params['armor'] = 0
            self.params['cost_walk'] = 5
            self.params['alive'] = 1
            self.write_sym = "Р"
        elif self.name == "Кирасир":
            self.params['hp'] = 60
            self.params['attack'] = 50
            self.params['attack_range'] = 2
            self.params['armor'] = 5
            self.params['cost_walk'] = 5
            self.params['alive'] = 1
            self.write_sym = "К"
        elif self.name == "Всадник":
            self.params['hp'] = 50
            self.params['attack'] = 50
            self.params['attack_range'] = 1
            self.params['armor'] = 10
            self.params['cost_walk'] = 5
            self.params['alive'] = 1
        else:
            raise ValueError("Такого типа юнитов не существует")
