class Facebook():
    def __init__(self, name, email, b_year, current_year=2024):
        self.name = name
        self.email  = email
        self.b_year = b_year
        self.current_year = current_year

    def get_name(self):
        return self.name.capitalize()
    
    def get_mail(self):
        return self.email
    
    def b_year(self):
        return self.b_year

    def get_age(self):
        return f"{self.current_year - self.b_year}"

    def get_full_info(self):
        return f"{self.get_name()} is {self.get_age()} years old. He's email adress: {self.get_mail()}" 

jhon = Facebook("khan", "email.mail@com", 2003,2023)
sammy = Facebook('sammy', "sammy@gmail.com",2003)
print(jhon.get_full_info())
print(sammy.get_full_info())

        
