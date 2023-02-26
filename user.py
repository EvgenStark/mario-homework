class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

    def top(self):
        self.y -= 1

    def bottom(self):
        self.y += 1

    def position(self):
        return self.x, self.y