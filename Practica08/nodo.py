class Nodo:
    def __init__(self, t):
        self.hijos = list()
        self.llaves = list()
        self.hoja = 1
        self.n = 0
        for k in range(2*t):
            self.llaves.append([None])
        for k in range(2*t+1):
            self.hijos.append([None])
