import time

class GameEngine:

    def __init__(self):
        self.score = 0
        self.level = 1
        self.start_time = time.time()

    def add_score(self, points):
        self.score += points

    def next_level(self):
        self.level += 1

    def get_time_taken(self):
        return int(time.time() - self.start_time)