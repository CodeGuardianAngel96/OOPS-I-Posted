'''
    Create a class Automobile with an attribute color with default value “black”. 
    It contains instance variables name,mileage,max_speed.  
    Class vehicle is inherited by both classes lorry and bus. 
    These classes doesn’t contain any properties of their own.
    Color: White, Vehicle name: ashokleyland load, Speed: 180, Mileage: 12
    Color: White, Vehicle name: scania AC, Speed: 240, Mileage: 18
'''

class Automobile:

    def __init__(self, name, color = 'black', mileage, maxSpeed):

        self.name = name
        self.mileage = mileage
        self.maxSpeed = maxSpeed
        self.color = color
    
    def display(self):
        
        print(self.name)
        print(self.mileage)
        print(self.maxSpeed)
        print(self.color)

class Lorry(Automobile):

    def __init__(self):
        super().__init__()

class Bus(Automobile):

    super().__init__()



if __name__ == "__main__":

    l = Lorry('Ashoka Leyland', 'White', 12, 240)
    l.display()