from students import Student

class Subjects(Student):
    def __init__(self, name, b_year, gender, grade=1):
        super().__init__(name, b_year, gender, grade)
        self.students = []

    def add_student(self):
        self.students.append(self.name)
    
    def __repr__(self) -> str:
        return f"{self.name} was born in {self.b_year} and its {self.get_gender()}"

    def __getitem__(self, index):
        return self.students[index]
    
    def __setitem__(self, index, value):
        self.students[index] = value
        return self.students

    def __len__(self):
        return len(self.students)
