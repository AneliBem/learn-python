class Build:
    __city = None # інкапсуляція "__"
    __year = None

    def __init__(self, city, year):
        self.city = city
        self.year = year

    def get_info(self):
        print("city:", self.city, ". year:", self.year, sep="")

class School(Build): # спадкування класу Build
    pupils = None

    def __init__(self, year, city, pupils):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info() # звернення до головного класу "super()"
        print("Pupils:", self.pupils)

class House(Build):
    pass

class Shop(Build):
    pass

school = School("London", 1998, 895)
school.get_info()
house = House("Riga", 2005)
house.get_info()
shop = Shop("Berlin", 2010)