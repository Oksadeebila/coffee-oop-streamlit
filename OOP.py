class Coffee: 
    def __init__(self, width, length, thick, mass):
        self.width = width
        self.length = length
        self.thick = thick
        self.mass = mass
    def calculate_volume(self): 
        volume = (22/7) * (self.width * self.length * self.thick)/6
        return volume 
    def calculate_density(self): 
        v = self.calculate_volume()
        density = self.mass/v
        return density 

