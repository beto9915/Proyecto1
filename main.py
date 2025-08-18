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

class Program:
    opcion=0
    while opcion!=5:
        print("="*45+"MENU HIPER PAIZ"+"="*45)
        print("1. Registrar producto")
        print("2. Enlistar productos registrados")
        print("3. Buscar producto")
        print("4. Actualizar y eliminar")
        print("5. Salir")
        try:
            opcion=int(input("Seleccione: "))
            match opcion:
                case 1:
                    Inventario.registrar_producto()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    aux=int(input("""Desea:
                    1. Actualizar
                    2. Eliminar"""))
                    if aux==1:
                        Inventario.actualizar_producto()
                    elif aux==2:
                        Inventario.eliminar_producto()
                    else:
                        print("Opcion no valida...")
                        return
                case 5:
                    print("Gracias por usar sistema de Hiper Paiz!")
        except ValueError:
            print("La opcion debe ser un numero entero")