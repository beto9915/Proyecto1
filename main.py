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
        else:
            nombre=input("Ingrese el nombre del producto: ")
            if nombre in self.inventario.values().nombre:
                print("nombre ya registrado...")
                print("\npresione ENTER para continuar...")
                input()
            else:
                categoria=input("Ingrese categoria: ")
                precio=float(input("Ingrese el precio: "))
                stock=int(input("Ingrese el stock disponible"))
        self.inventario[codigo]=Producto(codigo, nombre, categoria, precio, stock)
        print("Producto registrado con exito! "*3)
