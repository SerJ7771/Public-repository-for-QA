class Cats:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getgender(self):
        return self.gender

    def getage(self):
        return self.age

from cat import Cats

cat_1 = Cats('Барон', 'мальчик', '2 года')

print('Имя -', cat_1.name)
print('Пол -', cat_1.gender)
print('Возраст -', cat_1.age)
print()

cat_2 = Cats('Сэм', 'мальчик', '2 года')

print('Имя -', cat_2.name)
print('Пол -', cat_2.gender)
print('Возраст -', cat_2.age)