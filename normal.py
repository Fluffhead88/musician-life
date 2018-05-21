import random


class Musician:

    def __init__(self, name):
        self.name = name
        self.instrument = []
        self.practice_time = random.choice(range(10))
        self.pay = []
        self.venue = []

    def get_guitar(self):
        if self.practice_time <= 2:
            self.instrument = None
        if self.practice_time <= 6:
            self.instrument = "Gibson Les Paul"
        if self.practice_time > 6:
            self.instrument = "PRS Custom"
            return self.instrument

    def venue(self):
        if self.pay < 150:
            self.venue = None
        if self.pay <= 1199:
            self.venue = "bar gig"
        else:
            self.venue = "Madison Square Garden"
            return self.venue

    def practice(self):
        if self.practice_time <= 2:
            self.pay = 0
            print(f"{self.name} didn't get called for a gig this weekend.\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")
        elif self.practice_time <= 6:
            self.pay = 150
            print(f"{self.name} has to play the {self.venue} this weekend with his {self.instrument}.\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")
        else:
            self.pay = 1200
            print(f"{self.name} gets to play {self.venue} this weekend with his {self.instrument}!\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")
            return self.pay





    def identify(self):
        print (f"\n{self.name} is a local musician. The hours he spends practicing each week, \ndetermines the weekend gig he gets to play.\n")

    def get_practice_time(self):
        print(f"{self.name} practiced for {self.practice_time} hours this week.")

    """def __str__(self):
        return f"DEBUG: {self.name}, {self.instrument}, {self.practice_time}, {self.gig_pay}"""

zach = Musician("Zach")


zach.get_guitar()
zach.identify()
zach.get_practice_time()
zach.practice()
#zach.venue()
