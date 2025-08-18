class Ordenar:
    @staticmethod
    def por_codigo(productos):
        if not productos:
            print("No hay productos registrados")
            return []

        lista_productos = [{"codigo": cod, **vars(datos)} for cod, datos in productos.items()]

        def ordenador(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[len(lista)//2]["codigo"]
            primeros = [x for x in lista if x["codigo"] < pivote]
            centro   = [x for x in lista if x["codigo"] == pivote]
            ultimos  = [x for x in lista if x["codigo"] > pivote]
            return ordenador(primeros) + centro + ordenador(ultimos)

        return ordenador(lista_productos)



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
            if nombre and nombre.lower() in producto["nombre"].lower():
                resultados.append(producto)
                continue
            if categoria and categoria.lower() in producto["categoria"].lower():
                resultados.append(producto)
                continue

        if not resultados:
            print("No se encontró ninguna coincidencia")
        return resultados


class Program:
    @staticmethod
    def main():
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
                opcion = int(input("Seleccione: "))
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
                        tipo=int(input("Seleccione: "))
                        if tipo==1:
                            codigo=input("Codigo: ")
                            resultados=Buscar.productos(inv.inventario, codigo=codigo)
                        elif tipo==2:
                            nombre=input("Nombre: ")
                            resultados=Buscar.productos(inv.inventario, nombre=nombre)
                        elif tipo==3:
                            categoria=input("Categoria: ")
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
        codigo=input("Ingrese codigo de producto: ")
        if codigo in self.inventario.keys():
            print("codigo ya registrado...")
            print("\npresione ENTER para continuar..")
            input()
            return
        else:
            nombre=input("Ingrese el nombre del producto: ")
            if any(prod.nombre==nombre for prod in self.inventario.values()):
                print("nombre ya registrado...")
                print("\npresione ENTER para continuar...")
                input()
                return
            else:
                categoria=input("Ingrese categoria: ")
                precio=float(input("Ingrese el precio: "))
                stock=int(input("Ingrese el stock disponible: "))
        self.inventario[codigo]=Producto(codigo, nombre, categoria, precio, stock)
        print("Producto registrado con exito! "*3)
        print("\npresione ENTER para continuar...")
        input()
    def actualizar_producto(self):
        codigo=input("Ingrese el codigo de producto a buscar: ")
        if codigo in self.inventario.keys():
            stock=int(input("Ingrese nuevo stock: "))
            precio=float(input("Ingrese nuevo precio: "))
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
        codigo=input("Ingrese codigo de producto a eliminar: ")
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
class entrada:
    def regresar(self):
        pass
Program.main()