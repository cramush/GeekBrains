class Cell:
    def __init__(self, quantity):
        if type(quantity) is not int:
            raise ValueError
        if quantity <= 0:
            raise ValueError("Ячеек в клетке должно бытыть больше 0.")
        self.quantity_count = quantity


    def __add__(self, other):
        if type(other) is not Cell:
            raise ValueError

        return Cell(self.quantity_count + other.quantity_count)


    def __sub__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_al_count = self.quantity_count - other.quantity_count

        return Cell(new_al_count)


    def __mul__(self, other):
        if type(other) is not Cell:
            raise ValueError

        return Cell(self.quantity_count * other.quantity_count)


    def __truediv__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_al_count = self.quantity_count // other.quantity_count
        if new_al_count == 0:
            raise ValueError("После деления не осталось ячеек.")

        return Cell(new_al_count)


    def make_order(self, cells_in_row):
        res = ""
        num = self.quantity_count
        while num > cells_in_row:
            res = res + "*" * cells_in_row + "\n"
            num -= cells_in_row
        res = res + "*" * num

        return res


cells1 = Cell(10)
print(cells1.make_order(30))
cells2 = Cell(60)
print(cells2.make_order(4))
k = Cell(11)
a = cells1 - cells2 + k
print(a.make_order(5))
print(a.quantity_count)
a = cells2 * cells1
print(a.quantity_count)
a = a / k
print(a.quantity_count)
