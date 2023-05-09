class Enemy: 
    def __init__(self, id, name, health, max_health):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health

class Boss:
     def __init__(self, id, name, health, max_health):
        self.health = health
        self.id = id
        self.name = name
        self.max_health = max_health

def health():
    Enemy