# Clase vertice
class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

# Clase grafo
class Grafo:
    vertices = {}

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice" " " + key + " "  "Sus vecinos son " +
                str(self.vertices[key].vecinos))

# Clase Controladora
class Controladora:
    def main(self):
        g = Grafo() # Creación de un objeto 'g' de la clase Grafo.
        # Se crea un objeto 'a' de la clase Vertice, un vertice.
        a = Vertice("A")
        # Se agrega el vertice a al grafo.
        g.agregarVertice(a)

        # Esta estructura de repeticion es para agregar
        # todos los vertices y no hacerlo uno a uno.
        for i in range(ord('A'), ord('K')):
            g.agregarVertice(Vertice(chr(i)))

        # Se declara una arista que contiene las aristas del grafo.
        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DR', 'DH', 'EH', 'FG', 'FI', 'FG', 'GJ']
        #edges = ['CE', 'DC', 'FA', 'GJ', 'lI', 'AK', 'NE', 'FA', 'JM', 'KE', 'AH']
        #edges = ['BA', 'AC', 'DE', 'HA', 'KI', 'KE', 'IH', 'EF', 'FI', 'DE', 'AC']
        #edges = ['KD', 'JI', 'NF', 'CH', 'FI', 'GA', 'HG', 'FH', 'BE', 'EI', 'GF']

        # Se agregan las aristas del grafo
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        # Se imprime el grafo, como lista de adyacencia.
        g.imprimeGrafo()

# Creación de un objeto de la clase controladora y llamada a la función main
obj = Controladora()
obj.main()
