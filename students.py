class Student:
    __cuantity_of_students = 0
 
    def __init__(self, name, b_year,gender, grade=1):
        self.name = name
        self.b_year = b_year
        self.grade = grade
        self.subjects = []
        self.__gender = gender
        Student.__cuantity_of_students +=1

    def __repr__(self) -> str:
        return f"{self.name.title()} is {self.grade} grade"
    
    def __eq__(self,grade) -> bool:
        return self.grade == grade

    def get_gender(self):
        return self.__gender
    
    def register_to_subject(self, subject):
        self.subjects.append(subject)
        for sub in self.subjects:  
            return sub 

    def remove_subject(self,removing_subject):
        if removing_subject in self.subjects:
            self.subjects.remove(removing_subject)
            result = print(f"{removing_subject} is removed!")
        else:
            result = print(f"{removing_subject} is not Found!")

    @classmethod
    def get_cuantity_of_students(cls):
        return cls.__cuantity_of_students