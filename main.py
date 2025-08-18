def Ordenar(productos, clave="codigo"):
    lista_productos=[{"codigo":cod,**datos} for cod, datos in productos.items()]
    def ordenador(lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[len(lista)][clave]
        primeros = [x for x in lista if x["codigo"] < pivote]
        centro = [x for x in lista if x["codigo"] == pivote]
        ultimos = [x for x in lista if x["codigo"] > pivote]
        return ordenador(primeros) + centro + ordenador(ultimos)
    return ordenador(lista_productos)


def Buscar_Producto(productos,codigo=None,nombre=None,categoria=None):
    resultados=[]
    lista_productos=[
        {"codigo":cod,**datos} for cod, datos in productos.items()
    ]
    for producto in lista_productos:
        if codigo and producto["codigo"]==codigo:
            resultados.append(producto)
            continue
        if nombre and nombre.lower() in producto["nombre"].lower():
            resultados.append(producto)
            continue
        if categoria and categoria.lower() in producto["categoria"].lower():
            resultados.append(producto)
            continue
    return resultados
