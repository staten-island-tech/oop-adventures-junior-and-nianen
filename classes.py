class User:
    def __init__(self, id, name, health, max_health, energy, max_energy):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health
        self.energy = energy
        self.max_energy = max_energy


class Fire(User):
    def __init__(self, id, name, moves, health, max_health, energy, max_energy):
        super().__init__(id, name, health, max_health, energy, max_energy)
        self.moves = moves


class Water(User):
    def __init__(self, id, name, moves, health, max_health, energy, max_energy):
        super().__init__(id, name, health, max_health, energy, max_energy)
        self.moves = moves


class Enemy:
    def __init__(self, id, name, health, max_health, damage):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health
        self.damage = damage


class Boss:
    def __init__(self, id, name, health, max_health, damage):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health
        self.damage = damage
