# 用class定義類別
class Cat():
    pass

a_cat = Cat()
another_cat = Cat()

# 屬性
class Cat():
    pass
a_cat = Cat()
print(a_cat)

a_cat.age = 3
a_cat.name = "May"
a_cat.nemesis = another_cat
print(a_cat.age)
print(a_cat.name)
print(a_cat.nemesis)
a_cat.nemesis.name = "Tom"
print(a_cat.nemesis.name)

# 初始化
class Cat():
    def __init__(self, name):
        self.name = name
furball = Cat("Furball")
print(furball.name)
print("Our lastest addition: ", furball.name)

# 從父類別繼承
class Car():
    pass
class Yugo(Car):
    pass
print(issubclass(Yugo, Car))
give_me_a_car = Car()
give_me_a_yugo = Yugo()
print(isinstance(give_me_a_car, Car))

class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    pass
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# 覆寫方法
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Dr." + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")
print(person.name)
print(doctor.name)
print(lawyer.name)

# 添加方法
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()

# 使用super取得父類別的幫助
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
bob = EmailPerson("Bob Frapples", "bob@frapples.com")
print(bob.name)
print(bob.email)
