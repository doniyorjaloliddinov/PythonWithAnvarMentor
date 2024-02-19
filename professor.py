from person import Person

class Professor(Person):
    def __init__(self, name, b_place, b_year,professor):
        super().__init__(name, b_place, b_year)
        self.professor = professor 

    def get_info(self):
        greating = super().get_info()

        return greating + f"\nI'm {self.professor}"
    
    def get_age(self, year):
        return f"You are {year - self.b_year} old!"