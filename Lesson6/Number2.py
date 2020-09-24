class Road:
    def __init__(self, _length, _width):
        self.length = _length
        self.width = _width
        print(f"Длина: {self.length} \nШирина: {self.width}")


    def Roadmass(self):
        weight = 25
        thickness = 5
        mass = self.length * self.width * weight * thickness / 1000
        print(f"Необходимая масса: {mass}")


road = Road(20, 5000)
road.Roadmass()
