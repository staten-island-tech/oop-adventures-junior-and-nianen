class User:
    def __init__(self, id, name, health, max_health):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health

class Fire(User):
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id, name, health, max_health)
        self.moves = moves

class Water(User):
    def __init__(self, id, name, moves, health, max_health):
        super().__init__(id, name, health, max_health)
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