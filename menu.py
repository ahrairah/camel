import sys
from player import Player
from random import randrange


class Menu:
    # Displays a menu and responds to choices

    def __init__(self):
        self.player = Player()
        self.choices = {
            "A": self.drink,
            "B": self.moderate,
            "C": self.full_speed,
            "D": self.rest,
            "E": self.status,
            "Q": self.quit
        }

    def display_menu(self):
        print("""
        Your choices:

        A: Drink from your canteen
        B: Travel at a moderate speed
        C: Travel at full speed
        D: Take a rest
        E: Show your current status
        Q: Quit the game
        """)

    def run(self):
        print("""
        Welcome to camel game.
        You have stolen a camel, the natives try to
        hunt you down. Your target is to get 200 miles
        through the desert, to escape them.""")

        while True:
            self.display_menu()
            choice = input("\tYour choice?\n").upper()
            action = self.choices.get(choice)
            if action:
                action()
                self.handler()
            else:
                print("{0} is not a valid choice".format(choice))

    def drink(self):
        self.player.drink()

    def moderate(self):
        self.player.moderate()
        print("""
        The camel likes this speed.
        """)

    def full_speed(self):
        self.player.full_speed()
        print("""
        You traveled at full speed.""")

    def rest(self):
        self.player.rest()
        print("""
        You took a rest. Your camel is now good to go.""")

    def status(self):
        self.player.status()

    def quit(self):
        print("""
        Thank you for playing.""")
        sys.exit(0)

    def handler(self):
        if self.player.thirst >= 8:
            print("\tYou died of dehydration.\n")
            sys.exit(0)

        elif self.player.camel_fatigue >= 6:
            print("\tYou ran your camel to death, you monster!\n")
            sys.exit(0)

        elif self.player.miles_traveled <= self.player.natives_traveled:
            print("\tThe natives captured and beheaded you.\n")
            sys.exit(0)

        elif self.player.miles_traveled >= 200:
            print("\tCongratulations, you escaped the natives.\n")
            sys.exit(0)

        else:
            self.status()


if __name__ == "__main__":
    Menu().run()
