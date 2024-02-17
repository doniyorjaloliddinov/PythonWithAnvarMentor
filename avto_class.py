class Avto:

    def __init__(self,model, color, transmission, price):
        self.model = model 
        self.color = color
        self.transmission = transmission
        self.price = price
        self.km = 10

    def get_info(self):
        return f"{self.model} is {self.color}. It's {self.price}$. Transmission: {self.transmission}"
    
    def update_km(self,update):
        self.km += update

class Avto_saloon:

    def __init__(self, name,adress):
        self.name = name
        self.adress = adress 
        self.all_cars = []

    def add_avto(self, avto):
        self.all_cars.append(avto)

    def get_all_cars_info(self):
        # for all_car in self.all_cars:
        #     return all_car
        return [avto.get_info() for avto in self.all_cars]
    

avto1 = Avto("mustang", "green", "auto", 20000)
avto2 = Avto("masserati", "steal", "auto", 35000)
avto_salon = Avto_saloon("Mega Motors", "Yunusabad str")
# print(avto1.get_info())
# print(avto2.model)
# avto1.update_km(100)
# print(avto1.km)
# avto_salon.add_avto(avto1.get_info())
# # avto_salon.add_avto(avto2.model)
# print(avto_salon.all_cars)
# print(avto_salon.get_all_cars_info())

print(dir(avto2))