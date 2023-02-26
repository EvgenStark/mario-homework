class Board:
    def __init__(self):
        self.count_x = 10
        self.count_y = 10
        self.tile = 50
        self.container = list(list(0 for i in range(10)) for i in range(10))

    def replace(self, x, y, value):
        self.container[y][x] = value

    def location(self):
        return self.container