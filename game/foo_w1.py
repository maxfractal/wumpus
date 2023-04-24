class Weapon:
    def __str__(self):
        return self.name

class Rock:
    def __init__(self, name, description, damage):
        self.name = "Just Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5

    def __str__(self):
        return self.name
    
class smallRock:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def __str__(self):
        return self.name
    
class Dagger:
    def __init__(self, name):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. "  "Somewhat more dangerous than a rock."
        self.damage = 10

    def __str__(self):
        return self.name
    
class RustySword:
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " "but still has some fight left in it."
        self.damage = 20

    def __str__(self):
        return self.name
    
   # r1 = Rock()
   # r1.name = "Rocky the rock"
    r1 = Rock('Rocky the deadly rock.','A fist-sized rock, suitable for bludgeoning.',5)
    r2 = smallRock('Rocky the small and deadly rock.','A tiny rock, suitable for poisening.',25)

    #d1 = Dagger()
    #d1.name = "Daggert the dagger"

    print(f"{r1.name}")
    print(r1.damage)
    print(r1.description)
    print(f"{r2.name}")
    #print(r1.description)
    #print(d1.name)