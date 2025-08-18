class Program:
    opcion=0
    while opcion!=5:
        print("="*45+"MENU"+"="*45)
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
