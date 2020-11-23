class Car():
    def __init__(self):
        self.make = input("make of dream car")
        self.model = input("model of dream car")
        self.year = input("year of dream car")
        self.color = input("color of dream car")
        self.engine = Engine()
        self.body_style = input("body style of dream car")
        self.top_speed = 0
        
    def drive(self):
        if self.engine.cyl == 8:
            self.top_speed = 120
        elif self.engine.cyl == 6:
            self.top_speed =100
        else:
            self.top_speed = 65
        print("this car can drive ")
        print("its top speed is "+top_speed)

class Engine():
    def __init__(self):
        self.cyl = input("how many cylinders in your engine")
        self.cyl_alignment = input("configuration of your engine")
        self.fuel_type = input("gass or deisel")

def main():
    my_dream_car = Car()
    my_dream_car.drive()
    
    your_car = Car()
    your_car.drive()

    
main()
