class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f"move {self.x}")

    def draw(self):
        print("draw")

point = Point(12,20).draw()
Point(12,20).x
