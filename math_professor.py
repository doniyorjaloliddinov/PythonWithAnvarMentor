from professor import Professor

class MathProfessor(Professor):
    def __init__(self, name, b_place, b_year, professor, math):
        super().__init__(name, b_place, b_year, professor)

    def get_info(self):
        message = super().get_info()

        return message + f" of math!"
    
    def ban_user(self):
        return F"{self.name} is banned!"