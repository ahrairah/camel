from random import randrange


class Player:
    def __init__(self):
        self.canteen = 6
        self.miles_traveled = 0
        self.camel_fatigue = 0
        self.thirst = 0
        self.natives_traveled = -20

    def drink(self):
        if self.canteen > 0:
            self.canteen -= 1
            if self.thirst <= 4:
                self.thirst = 0
            else:
                self.thirst -= 4

            print("""\t\tYou took a sip out of your canteen. \n\t\tThere are {0} left.""".format(self.canteen))

        else:
            print("\t\tYour canteen is empty.")

    def moderate(self):
        self.miles_traveled += randrange(7, 15)
        self.thirst += 1
        self.camel_fatigue += 1
        self.natives_traveled += randrange(5, 20)

    def full_speed(self):
        self.miles_traveled += randrange(10, 20)
        self.thirst += 1
        self.camel_fatigue += randrange(1, 3)
        self.natives_traveled += randrange(5, 20)

    def rest(self):
        self.camel_fatigue = 0
        self.natives_traveled += randrange(5, 20)

    def status(self):
        natives_distance = self.miles_traveled - self.natives_traveled
        print("""
        Your canteen has {0} sips left.
        Your thirst is at {1}.
        The fatigue of your camel is at {2}.
        You traveled {3} miles.
        Natives are {4} miles behind you.""".format(self.canteen, self.thirst, self.camel_fatigue,
                                                    self.miles_traveled, natives_distance))
