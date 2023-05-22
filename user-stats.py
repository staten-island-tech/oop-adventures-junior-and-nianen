class User:
    def __init__(self, id, name, health, max_health):
        self.id = id
        self.name = name
        self.health = health
        self.max_health = max_health

    def __repr__(self): 
        return "max_health:% s and the health:% s" % (self.max_health, self.health) 
    
user_health = User(200, )
