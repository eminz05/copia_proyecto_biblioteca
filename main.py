import funciones as fn
import sys

# libro = {}
# socios = {}

libros=fn.cargar_libros()
socios=fn.cargar_socios()

while True:
        print("BIBLIOTECA VECINAL")
        print("1. Agregar libro.")
        print("2. Actualizar libro.")
        print("3. Eliminar libro.")
        print("4. Listar un libro.")
        print("5. Registrar préstamo.")
        print("6. Registrar devolución.")
        print("7. Registrar socio.")
        print("8. Eliminar socio")
        print("9. Salir del programa")
        
        try:
            opc = int(input("Ingrese a la opción que desea ingresar 1-9: "))
        except ValueError:
            print("Debe ingresar una opción válida.")
            continue

        if opc == 1:
            fn.agregar_libro(libros) 
        elif opc == 2:
            fn.actualizar_libro(libros)
        elif opc == 3:
            fn.eliminar_libro(libros)
        elif opc == 4:
            fn.listar_libro(libros)
        elif opc == 5:
            fn.registrar_prestamo(libros,socios)
        elif opc == 6:
            fn.registrar_devolucion(libros,socios)
        elif opc == 7:
            fn.registrar_socio(socios)
        elif opc == 8:
            fn.eliminar_socio(socios)
        elif opc == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Ingrese una opción del 1 al 9.")