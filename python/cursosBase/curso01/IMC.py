class IMC(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = float(weight)
        self.height = float(height)

    def show_imc(self):
        imc = self.weight/(self.height**2)
        self.imc = imc
        print(self.imc)