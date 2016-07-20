class UnimplementedException(Exception):
    """We didn't implement this"""


class Animal(object):
    def __init__(self):
        self.number_legs = 0

    def HasLegs(self):
        if self.number_legs > 0:
            return True
        else:
            return False

    def CanFly(self):
        raise UnimplementedException("Unimplemented")

    def Sound(self):
        raise UnimplementedException('Unimplemented')

class Horse(Animal):
    def __init__(self):
        self.number_legs = 4

    def canFly(self):
        return False

    def Sound(self):
        return 'Neigh'

class Bird(Animal):
    def __init__(self):
        self.number_legs = 2

    def canFly(self):
        return True

class Canary(Bird):
    def Sound(self):
        return 'Chirp'

def main():
    animals = []
    horse = Horse()
    animals.append(horse)
    canary = Canary()
    animals.append(canary)
    print canary.CanFly()
    for animal in animals:
        print animal.__class__.__name__ + ' says ' + animal.Sound() + ' and has ' + str(animals.number_legs) + ' and HasLegs() returns ' + str(animal.HasLegs())

if __name__ == '__main__':
    main()
