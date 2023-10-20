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

# 多重繼承 
class Animal():
    def says(self):
        return "I speak!"
class Horse(Animal):
    def says(self):
        return "Neigh!"
class Donkey(Animal):
    def says(self):
        return "Hee-haw!"
class Mule(Donkey, Horse):
    pass
class Hinny(Horse, Donkey):
    pass
print(Mule.mro())
print(Hinny.mro())
print(Mule().says())
print(Hinny().says())

# Mixin
class PrettyMixin():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))
class Thing(PrettyMixin):
    pass
t = Thing()
t.name = "Tom"
t.feature = "handsome"
t.age = "eldritch"
t.dump()

# 自(self)衛
a_car = Car()
a_car.exclaim()
Car.exclaim(a_car)

# 屬性存取
    # 直接存取
class Duck:
    def __init__(self, input_name):
        self.name = input_name
fowl = Duck("Howard")
print(fowl.name)
fowl.name = "Daffy"
print(fowl.name)

# getter與setter
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
don = Duck("Donald")
don.get_name()
don.set_name("Donlad Duck")
print(don.get_name())

# 用來存取屬性的property
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    name = property(get_name, set_name)
don = Duck("Donald")
don.get_name()
don.set_name("Donlad Duck")
print(don.get_name())
don = Duck('Donald')
print(don.name)
don.name = 'Donna'
print(don.name)
    # 加入一些裝飾器，並將方法名稱get_name和set_name改為name:
    # 在getter方法前面加上@property
    # 在setter方法前面加上@name.setter
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
fowl = Duck("Howard")
print(fowl.name)
fowl.name = "Donald"
print(fowl.name)

# 用property來回傳算出來的值
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.radius)
# c.diameter = 20  # AttributeError: can't set attribute

# 修飾名稱來保護隱私
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print("inside the getter")
        return self.__name
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name
fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)
# print(fowl.__name)  # AttributeError: 'Duck' object has no attribute '__name'
print(fowl._Duck__name)

# 類別與物件屬性
class Fruit:
    color = 'red'

blueberry = Fruit()
print(blueberry.color)
blueberry.color = 'blue'
print(blueberry.color)
Fruit.color = 'orange'
print(blueberry.color)
orange = Fruit()
print(orange.color)
