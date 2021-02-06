class Garments:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Общий расход ткани '
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Garments):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c}'


class Jacket(Garments):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_j}'


coat = Coat(3, 5)
jacket = Jacket(6, 8)
print(coat)
print(jacket)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())
print(coat.get_sq_full)
print(jacket.get_sq_full)
