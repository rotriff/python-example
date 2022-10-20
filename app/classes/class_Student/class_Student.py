class Student:
    first_name: str = None
    last_name: str = None
    group: str = None
    average_mark: int = None

    def __init__(self, first_name: str, last_name: str, group: str, average_mark: int):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.average_mark = average_mark

    def get_scholarship(self):
        if self.average_mark == 5:
            return f'{self.first_name} {self.last_name} get 100 UAH'
        else:
            return f'{self.first_name} {self.last_name} get 80 UAH'


class Aspirant(Student):
    scientific_work: int = None

    def __init__(self, first_name: str, last_name: str, group: str, average_mark: int, scientific_work: int):
        super().__init__(first_name, last_name, group, average_mark)
        self.scientific_work = scientific_work

    def get_scholarship(self):
        if self.average_mark == 5:
            return f'{self.first_name} {self.last_name} get 200 UAH'
        else:
            return f'{self.first_name} {self.last_name} get 180 UAH'


if __name__ == '__main__':
    volodya = Student("Vova", "Taran", "IAN-409", 5)
    john = Student("John", "Kennedy", "FEB-303", 4)
    billy = Aspirant("William", "Butcher", "IKIT-510", 5, 1)
    marvin = Aspirant("Marvin", "Milk", "IAET-616", 4, 2)
    students_list = [volodya, john, billy, marvin]
    for student in students_list:
        print(student.get_scholarship())


