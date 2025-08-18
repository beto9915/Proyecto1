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
            if nombre in self.inventario.values().nombre:
                print("nombre ya registrado...")
                print("\npresione ENTER para continuar...")
                input()
                return
            else:
                categoria=input("Ingrese categoria: ")
                precio=float(input("Ingrese el precio: "))
                stock=int(input("Ingrese el stock disponible"))
        self.inventario[codigo]=Producto(codigo, nombre, categoria, precio, stock)
        print("Producto registrado con exito! "*3)
    def actualizar_producto(self):
        codigo=input("Ingrese el codigo de producto a buscar: ")
        if codigo in self.inventario.keys():
            stock=int(input("Ingrese nuevo stock: "))
            precio=float(input("Ingrese nuevo precio: "))
            self.inventario[codigo][stock]=stock
            self.inventario[codigo][precio]=precio
            print("Producto actualizado con exito! "*3)
        else:
            print("producto no encontrado...")
            return
    def eliminar_producto(self):
        pass
