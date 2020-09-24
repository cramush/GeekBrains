class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала."

    def stop(self):
        return f"{self.name} остановилась."

    def turn_right(self):
        return f"{self.name} повернула направо."

    def turn_left(self):
        return f"{self.name} повернула налево."

    def show_speed(self):
        return f"{self.name} едет со скоростью: {self.speed}"


class TownCar(Car):

    def show_speed(self):
        print(f"{self.name} едет со скоростью: {self.speed}")

        if self.speed > 40:
            return f"{self.name} превысила скорость."
        else:
            return f"{self.name} не привышает скорость."

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"{self.name} превысила скорость на: {self.speed}")

        if self.speed > 60:
            return f"{self.name} превысила скорость."


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} это полицейская машина."
        else:
            return f"{self.name} это не полицейская машина."


town_auto = TownCar(65, "Серый", "Ниссан", False)
print(town_auto.go())
print(town_auto.show_speed())

sport_auto = SportCar(130, "Черный", "Ягуар", False)
print(sport_auto.go())
print(sport_auto.show_speed())

work_car = WorkCar(37, "Желтый", "Газель", False)
print(work_car.go())
print(work_car.show_speed())

police_auto = PoliceCar(70, "Белый", "Ауди", False)
print(police_auto.go())
print(police_auto.show_speed())
