import random
class Player:
    def __init__(self, name):
        self.name = name
        self.opened_characteristics = {
            "profession": True,  # Профессия видна изначально
            "biology": False,
            "health": False,
            "phobia": False,
            "baggage": False,
            "hobby": False,
            "fact": False
        }
        self.votes = 0
        self.profession = random.choice([f"Профессия N{i}" for i in range(1,7)])
        self.biology = random.choice([f"Биология N{i}" for i in range(1,7)])
        self.health = random.choice([f"Здоровье N{i}" for i in range(1,7)])
        self.phobia = random.choice([f"Фобия N{i}" for i in range(1,7)])
        self.baggage = random.choice([f"Багаж N{i}" for i in range(1,7)])
        self.hobby = random.choice([f"Хобби N{i}" for i in range(1,7)])
        self.fact = random.choice([f"Факт N{i}" for i in range(1,7)])
        self.details_visible = {
            "profession": True,  # Профессия видна изначально
            "biology": False,
            "health": False,
            "phobia": False,
            "baggage": False,
            "hobby": False,
            "fact": False
        }
        self.last_opened = set()  # Помечаем, что изначально ничего не открыто, кроме профессии

    def vote_against(self):
        self.votes += 1

    def reset_votes(self):
        self.votes = 0
    def open_characteristics(self):
        self.opened_characteristics = {
            "profession": True,
            "biology": True,
            "health": True,
            "phobia": True,
            "baggage": True,
            "hobby": True,
            "fact": True
        }