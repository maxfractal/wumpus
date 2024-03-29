class Weapon:
    def __str__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
    
    def __str__(self):
        return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

    def __str__(self):
        return self.name
    
class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. "  "Somewhat more dangerous than a rock."
        self.damage = 10

    def __str__(self):
        return self.name
    
class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " "but still has some fight left in it."
        self.damage = 20

    def __str__(self):
        return self.name