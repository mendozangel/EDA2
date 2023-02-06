from arbol import Arbol

# Cración del árbol
a = Arbol(8)
a.agregar(3)
a.agregar(10)
a.agregar(1)
a.agregar(6)
a.agregar(14)
a.agregar(4)
a.agregar(7)
a.agregar(13)

# Llamada al método Preorden
a.preorden()

# Realizar la búsqueda de un nodo
busqueda = int(input("Ingresa un valor para buscar en el árbol: "))
k = a.buscar(busqueda)
if k is None:
    print(f"{busqueda} no existe.\n")
else:
    print(f"{busqueda} sí existe.\n")
