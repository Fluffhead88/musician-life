
import random


class Musician:

    def __init__(self, name):
        self.name = name
        self.instrument = []
        self.practice_time = random.choice(range(10))
        self.pay = 0
        self.venue = []

    def get_guitar(self):
        if self.practice_time <= 2:
            self.instrument = None
            self.pay = 0
        elif self.practice_time <= 6:
            self.instrument = "Gibson Les Paul"
            self.pay = 150
        elif self.practice_time > 6:
            self.instrument = "PRS Custom 24"
            self.pay = 500
            return self.instrument, self.pay

    def get_venue(self):
        if self.pay < 150:
            self.venue = None
        elif self.pay <= 499:
            self.venue = "bar gig"
        elif self.pay >= 500:
            self.venue = "the local auditorium"
        return self.venue

    def practice(self):
        if self.practice_time <= 2:
            print(f"{self.name} didn't get called for a gig this weekend.\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")
        elif self.practice_time <= 6:
            print(f"{self.name} has to play a {self.venue} this weekend with his {self.instrument}.\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")
        else:
            print(f"{self.name} gets to play {self.venue} this weekend with his {self.instrument}!\n")
            print(f"{self.name} will make ${int(self.pay)} this weekend.\n")






    def identify(self):
        print (f"\n{self.name} is a local musician. The hours he spends practicing each week, \ndetermines the weekend gig he gets to play.\n")

    def get_practice_time(self):
        print(f"{self.name} practiced for {self.practice_time} hours this week.")

    #def __str__(self):
        #return f"DEBUG: {self.name}, {self.instrument}, {self.practice_time}, {self.gig_pay}

zach = Musician("Zach")

zach.identify()
zach.get_guitar()
zach.get_practice_time()
zach.get_venue()
zach.practice()
