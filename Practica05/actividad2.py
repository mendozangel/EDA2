class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = list()
        self.distancia = 9999
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

# Clase grafo
class Grafo:
    vertices = {}

    def bfs(self, vert):
        vert.distancia = 0
        vert.color = 'gris'
        vert.pred = -1
        q = list()
        q.append(vert.nombre)

        while len(q) > 0:

            u = q.pop()
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gris'
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    q.append(v)
            self.vertices[u].color = 'black'

     # Agregar vertice
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    # Agregar arista
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

    # Impresión del grafo
    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice" " " + key + " "  "Sus vecinos son " +
                  str(self.vertices[key].vecinos))
            print("La distancia de A a" " " + key +
                  " " "es: "+str(self.vertices[key].distancia))


# Clase Controladora
class Controladora:
    def main(self):
        # Se crea un objeto 'g' de la clase Grafo, el grafo.
        g = Grafo()
        # Se crea un objeto 'a' de la clase Vertice, un vertice.
        a = Vertice("A")

        # Se agrega el vertice a al grafo.
        g.agregarVertice(a)

        # La estructura de repeticion es para agregar todos los vertices e ir
        # haciendo uno a uno.
        for i in range(ord('A'), ord('K')):
            g.agregarVertice(Vertice(chr(i)))

        # Se declara una arista que contiene las aristas del grafo
        #edges = ['AB', 'AE', 'BG', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
        # Agrega un grafo propuesto
        edges =['AB', 'CE', 'DF', 'GI', 'EJ', 'KH', 'KA', 'FI', 'JF', 'KC', 'GA']

        # Se declaran las aristas del grafo
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        g.bfs(a)
        g.imprimeGrafo()

obj = Controladora()
obj.main()