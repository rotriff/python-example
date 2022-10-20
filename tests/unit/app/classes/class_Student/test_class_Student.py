import pytest
from app.classes.class_Student.class_Student import Student
from app.classes.class_Student.class_Student import Aspirant

volodya = Student("Vova", "Taran", "IAN-409", 5)
john = Student("John", "Kennedy", "FEB-303", 4)
billy = Aspirant("William", "Butcher", "IKIT-510", 5, 1)
marvin = Aspirant("Marvin", "Milk", "IAET-616", 4, 2)


@pytest.mark.parametrize(
    "student, get", [(volodya, "Vova Taran get 100 UAH"),
                     (john, "John Kennedy get 80 UAH"),
                     (billy, "William Butcher get 200 UAH"),
                     (marvin, "Marvin Milk get 180 UAH")]
)
def test_get_scholarship(student: Student, get: str):
    assert get == student.get_scholarship()


