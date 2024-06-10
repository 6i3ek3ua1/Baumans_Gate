import pickle
from town.building import DoctorHouse, Arsenal, Forge, Market, Tavern, Workshop, Academy


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.wallet = {}
        self.buildings = {'doctor_house': DoctorHouse(), 'forge': Forge(), 'arsenal': Arsenal(), 'market': Market(),
                          'tavern': Tavern(), 'workshop': Workshop(), 'academy': Academy()}
        self.new_unit = 0

    def buy_doctors_house(self):
        self.buildings['doctor_house'].buying(self)

    def buy_forge(self):
        self.buildings['forge'].buying(self)

    def buy_arsenal(self):
        self.buildings['arsenal'].buying(self)

    def buy_tavern(self):
        self.buildings['tavern'].buying(self)

    def buy_market(self):
        self.buildings['market'].buying(self)

    def buy_workshop(self):
        if self.buildings['workshop'].status == 0:
            self.buildings['workshop'].buying(self)
        else:
            self.buildings['workshop'].upgrade(self)

    def buy_academy(self):
        self.buildings['academy'].buying(self)

    def getting_buffs(self, units):
        for unit in units:
            for item in self.buildings.values():
                if item.status == 1 and item.parameter != 0:
                    unit.params[item.parameter] += item.boost

    def save(self):
        self.new_unit = self.buildings['academy'].new_unit
        with open(f'users\\{self.name}.pickle', 'wb') as f:
            pickle.dump(self, f)
