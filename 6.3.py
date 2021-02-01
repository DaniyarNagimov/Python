
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


pos = Position('Питер', 'Паркер', 'Человек - Паук', 1656480, 56483216)
print(pos.get_full_name())
print(pos.position)
print(pos.get_total_income())
