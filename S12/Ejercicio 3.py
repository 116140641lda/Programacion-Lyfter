class Goku:

    def __init__(self):
        self.power = "Big Power"
    def get_power(self):
        print(f"Este poder es: {self.power}")


class Gohan(Goku):

    def __init__(self):
        super().__init__()
        self.little_power = "Little Power"
        print ( f"Este poder es: {self.little_power}")


gohan = Gohan()


print(gohan.little_power)
print(gohan.power)
gohan.get_power()
