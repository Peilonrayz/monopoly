import json


class Location:
    def __init__(self, group, name):
        self.group = group
        self.name = name
        self.id = None

    def __repr__(self):
        return "{}({})".format(self.group, self.name)


class Card(Location):
    def __init__(self, name):
        super().__init__("Card", name)


class Corner(Location):
    def __init__(self, name):
        super().__init__("Corner", name)


class Tax(Location):
    def __init__(self, name, tax):
        self.tax = tax
        super().__init__("Tax", name)


class Property(Location):
    def __init__(self, group, name, cost, mortgage, rent):
        self.cost = cost
        self.mortgage = mortgage
        self._rent = rent
        super().__init__(group, name)

    def rent(self, game_state):
        return self._rent[0]


class House(Property):
    def __init__(self, group, name, cost, mortgage, upgrade, rent):
        self.upgrade_cost = upgrade
        super().__init__(group, name, cost, mortgage, rent)


class Station(Property):
    def __init__(self, name, cost, mortgage, rent):
        super().__init__("Station", name, cost, mortgage, rent)


class Utility(Property):
    def __init__(self, name, cost, mortgage, rent):
        super().__init__("Utility", name, cost, mortgage, rent)


def read_game_data():
    with open("game_data.json") as f:
        return json.load(f)


def setup_ids(game, names, color):
    names = iter(names)
    houses = [
        House(group, name, *prices)
        for group, name, prices in zip(color, names, game["houses"])
    ]
    stations = [Station(name, *prices) for prices, name in zip(game["stations"], names)]
    utilities = [
        Utility(name, *prices) for prices, name in zip(game["utilities"], names)
    ]
    taxes = [Tax(name, tax) for tax, name in zip(game["tax"], names)]
    cards = [Card(name) for _, name in zip(range(2), names)]
    corners = [Corner(name) for _, name in zip(range(4), names)]
    return tuple(houses + stations + utilities + taxes + cards + corners)


def setup_game():
    game = read_game_data()
    ids = setup_ids(
        game["game"], game["localisation"]["British"], game["color"]["Brown"]
    )
    board = tuple(ids[id_] for id_ in game["game"]["board"])
    for i, item in enumerate(ids):
        item.id = i
    return ids, board


setup_game()
