class Card:
    def __init__(self, name, energy, card_type, description, picture):
        self.name = name
        self.energy = energy
        self.type = card_type
        self.description = description
        self.picture = picture

    def __str__(self):
        return f"{self.name}: {self.description}"

    def activate(self, actor, goal):
        pass

    @staticmethod
    def attack(damage, attacker, goal):
        damage = attacker.attack(damage)
        goal.receive_attack(damage)

    @staticmethod
    def block(block_points, actor):
        actor.block(block_points)

    @staticmethod
    def add_strength(strength, actor):
        actor.add_strength(strength)