import turtle as t
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def drawCircle(self):
        t.circle(self.radius)

c = Circle(50)
c.drawCircle()
