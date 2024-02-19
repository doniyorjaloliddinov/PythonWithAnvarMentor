
class Person:
    __cuantity_of_people = 0
    def __init__(self, name, b_place, b_year, skin_color="light"):
        self.name = name
        self.b_place = b_place
        self.b_year = b_year
        self.__skin_color = skin_color
        Person.__cuantity_of_people +=1
        
    def get_skin_color(self):
        return self.__skin_color

    def get_info(self):
        return f"Hello my name is {self.name}!"

    @classmethod
    def get_cuantity_of_people(cls):
        return cls.__cuantity_of_people