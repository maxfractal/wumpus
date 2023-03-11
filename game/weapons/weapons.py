class Weapon:
    def _str_(self):
        return self.name

class Rock:
    def _init_(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

    def _str_(self):
        return self.name
    
class Dagger:
    def _init_(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. "  "Somewhat more dangerous than a rock."
        self.damage = 10

    def _str_(self):
        return self.name
    
class RustySword:
    def _init_(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " "but still has some fight left in it."
        self.damage = 20

    def _str_(self):
        return self.name