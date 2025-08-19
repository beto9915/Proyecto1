class Ordenar:
    @staticmethod
    def ordenar(productos, clave="codigo"):
        if not productos:
            print("No hay productos registrados")
            return []

        lista_productos = [{"codigo": cod, **vars(datos)} for cod, datos in productos.items()]

        def quicksort(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[len(lista)//2][clave]
            menores = [x for x in lista if x[clave] < pivote]
            iguales = [x for x in lista if x[clave] == pivote]
            mayores = [x for x in lista if x[clave] > pivote]
            return quicksort(menores) + iguales + quicksort(mayores)

        return quicksort(lista_productos)

class Buscar:
    @staticmethod
    def productos(productos, codigo=None, nombre=None, categoria=None):
        if not productos:
            print("No hay productos registrados")
            return []

        resultados = []
        lista_productos = [{"codigo": cod, **vars(datos)} for cod, datos in productos.items()]

        for producto in lista_productos:
            if codigo and producto["codigo"] == codigo:
                resultados.append(producto)
                continue
            if nombre and nombre.upper() in producto["nombre"].upper():
                resultados.append(producto)
                continue
            if categoria and categoria.upper() in producto["categoria"].upper():
                resultados.append(producto)
                continue

        if not resultados:
            print("No se encontró ninguna coincidencia")
        return resultados


class Program:
    @staticmethod
    def main():
        entrada=Entrada()
        opcion = 0
        inv = Inventario()
        while opcion != 5:
            print("=" * 45 + "MENU HIPER PAIZ" + "=" * 45)
            print("1. Registrar producto")
            print("2. Enlistar productos registrados")
            print("3. Buscar producto")
            print("4. Actualizar y eliminar")
            print("5. Salir")
            try:
                opcion = entrada.entrada_usuario("Seleccione: ", tipo=int)
                match opcion:
                    case 1:
                        inv.registrar_producto()
                    case 2:
                        if not inv.inventario:
                            print("No hay productos registrados")
                        else:
                            productos_ordenados=Ordenar.por_codigo(inv.inventario)
                            print("\n* * * Inventario: * * *")
                            for prod_dict in productos_ordenados:
                                p=Producto(**prod_dict)
                                p.mostrar_producto()
                        pass
                    case 3:
                        print("Como desea buscar el producto?")
                        print("1. Por codigo")
                        print("2. Por nombre")
                        print("3. Por categoria")
                        print("4. Regresar")
                        tipo=entrada.entrada_usuario("Seleccione: ", tipo=int)
                        resultados=[]
                        if tipo==1:
                            codigo=entrada.entrada_usuario("Codigo: ", tipo=str)
                            resultados=Buscar.productos(inv.inventario, codigo=codigo)
                        elif tipo==2:
                            nombre=entrada.entrada_usuario("Nombre: ", tipo=str)
                            resultados=Buscar.productos(inv.inventario, nombre=nombre)
                        elif tipo==3:
                            categoria=entrada.entrada_usuario("Categoria: ", tipo=str)
                            resultados=Buscar.productos(inv.inventario, categoria=categoria)
                        elif tipo==4:
                            print("Regresando")
                            return
                        else:
                            print("Opcion invalida")
                        if resultados:
                            print("\nResultados de la busqueda")
                            for prod_dict in resultados:
                                p=Producto(**prod_dict)
                                p.mostrar_producto()

                        pass
                    case 4:
                        aux = int(input("""Desea:
                            1. Actualizar
                            2. Eliminar
                            Seleccione: """))
                        if aux == 1:
                            inv.actualizar_producto()
                        elif aux == 2:
                            inv.eliminar_producto()
                        else:
                            print("Opcion no valida...")
                    case 5:
                        print("Gracias por usar sistema de Hiper Paiz!")
            except ValueError:
                print("La opcion debe ser un numero entero")
class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock
    def mostrar_producto(self):
        print(f"Codigo de producto: {self.codigo}, Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Stock: {self.stock}\n")
        print("="*45)
class Inventario:

    def __init__(self):
        self.inventario={}
    def registrar_producto(self):
        entrada = Entrada()
        codigo=entrada.entrada_usuario("Ingrese codigo: (o escriba 'salir' o presione '0' para regresar): ", tipo=str)
        if codigo==None:
            return
        codigo=codigo.upper()
        if codigo in self.inventario.keys():
            print("codigo ya registrado...")
            print("\npresione ENTER para continuar..")
            input()
            return
        else:
            nombre=entrada.entrada_usuario("Ingrese nombre: (o escriba 'salir' o presione '0' para regresar): ", tipo=str)
            if nombre==None:
                return
            nombre=nombre.upper()
            if any(prod.nombre==nombre for prod in self.inventario.values()):
                print("nombre ya registrado...")
                print("\npresione ENTER para continuar...")
                input()
                return
            else:
                categoria=entrada.entrada_usuario("Ingrese la categoria (o escriba 'salir' o presione '0' para regresar): ", tipo=str)
                if categoria==None:
                    return
                categoria=categoria.upper()
                precio=entrada.entrada_usuario("Ingrese el precio: (o escriba 'salir' o presione '0' para regresar): ", tipo=float)
                stock=entrada.entrada_usuario("Ingrese el stock disponible (o escriba 'salir' o presione '0' para regresar): ", tipo=int)
        self.inventario[codigo]=Producto(codigo, nombre, categoria, precio, stock)
        print("Producto registrado con exito! "*3)
        print("\npresione ENTER para continuar...")
        input()
    def actualizar_producto(self):
        entrada=Entrada()
        codigo=entrada.entrada_usuario("Ingrese el codigo a actualizar (o escriba 'salir' o presione '0' para regresar): ", tipo=str)
        if codigo==None:
            return
        codigo=codigo.upper()
        if codigo in self.inventario.keys():
            stock=entrada.entrada_usuario("Ingrese el nuevo stock (o escriba 'salir' o presione '0' para regresar): ", tipo=int)
            precio=entrada.entrada_usuario("Ingrese el nuevo precio (o escriba 'salir' o presione '0' para regresar): ", tipo=float)
            self.inventario[codigo].stock=stock
            self.inventario[codigo].precio=precio
            print("Producto actualizado con exito! "*3)
            print("\npresione ENTER para continuar...")
            input()
        else:
            print("producto no encontrado...")
            print("\npresione ENTER para continuar...")
            input()
            return
    def eliminar_producto(self):
        entrada=Entrada()
        codigo=entrada.entrada_usuario("Ingrese el codigo del producto a eliminar (o escriba 'salir' o presione '0' para regresar): ", tipo=str)
        if codigo==None:
            return
        codigo=codigo.upper()
        if codigo in self.inventario.keys():
            print(f"Esta seguro de eliminar el producto: {self.inventario[codigo].nombre}? (Y/N)")
            respuesta=input("Seleccione: ").upper()
            if respuesta=="Y":
                del self.inventario[codigo]
                print("Producto eliminado con exito!...")
                print("\npresione ENTER para continuar...")
                input()
            else:
                print("Producto no eliminado...")
                print("\npresione ENTER para continuar...")
                input()
        else:
            print("Codigo no encontrado, intente de nuevo...")
            print("\npresione ENTER para continuar...")
            input()
            return
class Entrada:
    @staticmethod
    def entrada_usuario(prompt, tipo=str, permitir_salir=True):
        while True:
            valor = input(prompt).strip()

            if permitir_salir and (valor.lower() == "salir" or valor == "0"):
                return None
            try:
                if tipo == int:
                    return int(valor)
                elif tipo == float:
                    return float(valor)
                else:
                    return valor
            except ValueError:
                print(f"Entrada inválida. Se esperaba {tipo.__name__}.")

Program.main()