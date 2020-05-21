class woman:
    weight = ""
    iq = ""
    height = ""

    def __init__(self, weight, height, iq):
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        print(self.weight)

    def sleep(self):
        print(self.height)

    def study(self):
        print(self.iq)
