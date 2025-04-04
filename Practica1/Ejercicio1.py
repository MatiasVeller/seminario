# Ejercicio1

def opcion1(invetario):
    print("AGREGAR UN NUEVO PRODUCTO")
    nombre = str(input("Ingrese el nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad inicial del producto: "))
    if nombre in inventario:        
        inventario[nombre] += cantidad
        print("Stock del producto actualizado!")
    else:        
        inventario[nombre] = cantidad
        print("Producto ingresado correctamente!")

def opcion2(invetario):
    print("ELIMINAR PRODUCTO")
    nombre = str(input("Ingrese el nombre del producto que quiere eliminar: "))
    if nombre in inventario:
        del inventario[nombre]
        print("Se elimino el producto ingresado!")
    else:
        print("El producto ingresado no forma parte del inventario")

def opcion3(invetario):
    print("MOSTRAR EL INVENTARIO")
    if not inventario:
        print("Inventario vacio")
    else:
        for pos in inventario:
            print(f"Nombre: {pos}")
            print(f"Cantidad: {inventario.get(pos)}")

inventario = {}

while True:
    print ("1: Agregar nuevo producto")
    print ("2: Eliminar un producto")
    print ("3: Mostrar el inventario actual")
    print("4: Salir del programa")
    print()
    opcion = input("Ingrese una opcion (1,2,3,4): ")
    print()
    if opcion.isdigit():
        opcion_check = int(opcion)        
        if opcion_check == 1:
            opcion1(inventario)
        elif opcion_check == 2:
            opcion2(inventario)
        elif opcion_check == 3:
            opcion3(inventario)
        elif opcion_check == 4:
            print("Finalizando programa...")
            break
        print()
    else: print("Opcion invalida")