from Script.Person import Person
from Script.PythonObject import Student


def main():
    student1 = Student('leon', 18)
    student1.watch_movie()
    student1.study('百年孤独')
    student1.high = 50
    print(student1.high)
    person1 = Person('ss', 23, 33)
    Person.printpersondata()
    person1.name = 'leon'
    person1.age = 17
    person1.high = 178
    print(person1.age)
    print(person1.name)
    print(person1.high)


if __name__ == '__main__':
    main()
