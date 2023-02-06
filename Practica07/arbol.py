from nodo import Nodo

# Creación de la clase Árbol

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar(self, nodo, val):
        if val < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(val)
            else:
                self.__agregar(nodo.izquierda, val)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(val)
            else:
                self.__agregar(nodo.derecha, val)

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=" ")
            self.__preorden(nodo.izquierda)
            self.__preorden(nodo.derecha)

    # Agregando el método para realizar búsqueda
    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def agregar(self, val):
        self.__agregar(self.raiz, val)

    def preorden(self):
        print("*** ÁRBOL PREORDEN ***")
        self.__preorden(self.raiz)
        print("\n")

    # Haciendo el método público
    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
