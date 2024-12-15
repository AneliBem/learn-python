class Dog:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = "Bob", age = 1, isHappy = True): # після '=' значення за замовчуванням
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name, age = 1, isHappy = True):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy ", self.isHappy)

dog1 = Dog(age = 2) # звернення до класу Dog
dog2 = Dog("Bobik", 5, False)
