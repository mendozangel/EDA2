from nodo import Nodo

class ArbolB:
    def __init__(self, gMin):
        self.t = gMin
        self.raiz = None

    def bTreeCreate(self):
        if (self.raiz == None):
            self.raiz = Nodo(self.t)
        return self.raiz

    def bTreeSplitShild(self, x, i):
        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t-1

        for j in range(1, self.t):
            z.llaves[j] = y.llaves[j+self.t]
            y.llaves[j+self.t] = None

        if y.hoja == 0:
            for j in range(1, self.t+1):
                z.hijos[j] = y.hijos[j+self.t]
                y.hijos[j+self.t] = None
        y.n = self.t-1

        for j in range(x.n+1, i, -1):
            x.hijos[j+1] = x.hijos[j]
            
        x.hijos[i+1] = z

        for j in range(x.n, i-1, -1):
            x.llaves[j+1] = x.llaves[j]
        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n+1

    def bTreeInsertNonFull(self, x, k):
        i = x.n
        if x.hoja == 1:
            while (i >= 1) and (k < x.llaves[i]):
                x.llaves[i+1] = x.llaves[i]
                i = i-1
            x.llaves[i+1] = k
            x.n = x.n+1
        else:
            while (i >= 1) and (k < x.llaves[i]):
                i = i-1
            i = i+1
            if x.hijos[i].n == 2*self.t-1:
                self.bTreeSplitShild(x, i)
                if k > x.llaves[i]:
                    i = i+1
            self.bTreeInsertNonFull(x.hijos[i], k)

    def bTreeInsert(self, nodo, k):
        r = self.raiz
        if r.n == 2*self.t-1:
            s = Nodo(self.t)
            self.raiz = s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            self.bTreeSplitShild(s, 1)
            self.bTreeInsertNonFull(s, k)
        else:
            self.bTreeInsertNonFull(r, k)

    def imprimeNodo(self, nodo):
        for i in range(1, 2+self.t, 1):
            if (nodo.llaves[i] != None):
                print(nodo.llaves[i])
