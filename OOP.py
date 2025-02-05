class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
        
class race_car(vehicle):
    pass

obj=race_car("bob jr",1000,10000)
print(obj.name)
print(obj.speed)
print(obj.mileage)