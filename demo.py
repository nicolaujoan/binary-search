# BÚSQUEDA BINARIA
# hacemos una función busqueda_binaria() que recibe un array y un elemento
# si el elemento está en la lista, devuelve su posición.
# se mantiene el rastro de en que parte del array hay que buscar

def busqueda_binaria(lista, elemento):

    # ordenamos la lista por si acaso (sino la busqueda binaria no funciona)
    lista.sort()

    # indican en que parte de la lista buscarás
    menor = 0
    mayor = len(lista) - 1

    # mientras no se reduzca la busqueda a un solo elemento 
    while menor <= mayor:
        # elemento del medio de la lista
        medio = (menor + mayor) // 2
        # elemento estimado
        estimado = lista[medio]
        # elemento estimado coincide con el elemento a buscar
        if estimado == elemento:
            return medio
        # reducimos los limites de busqueda
        if estimado > elemento:
            mayor = medio - 1
        else:
            menor = medio + 1
    # elemento no esta en la lista
    return None


