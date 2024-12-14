class Dog:
    name = None
    age = None
    isHappy = None


    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy ", self.isHappy)

dog1 = Dog() # звернення до класу Dog
dog1.set_data("Skuf", 16, True)

# dog1.name = "Skuf"
# dog1.age = 16
# dog1.isHappy = True

dog2 = Dog()
dog2.name = "Bobik"
dog2.age = 5
dog2.isHappy = False


# print(dog1.name)
# print(dog2.name)

dog1.get_data()
dog2.get_data()
