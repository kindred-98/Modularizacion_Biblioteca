from services.inventario_service import InventarioService
from models.biblioteca import Biblioteca
from models.libro import Libro

def pedir_texto(msg):
    while True:
        t = input(msg).strip()
        if t:
            return t
        print("No puede estar vacío.")

def pedir_float(msg):
    while True:
        try:
            v = float(input(msg))
            return v
        except ValueError:
            print("Introduce un número válido.")

def pedir_int(msg):
    while True:
        try:
            v = int(input(msg))
            return v
        except ValueError:
            print("Introduce un entero válido.")

def iniciar_menu():
    biblioteca = Biblioteca("Biblioteca Central")
    servicio = InventarioService(biblioteca)

    biblioteca.agregar_libro(Libro("El Quijote", "Cervantes", 15, 3))
    biblioteca.agregar_libro(Libro("Cien años", "García Márquez", 12.5, 2))
    biblioteca.agregar_libro(Libro("1984", "Orwell", 10, 1))

    opciones = {
        "1": lambda: print(servicio.prestar(pedir_texto("Título: "))),
        "2": lambda: print(servicio.devolver(pedir_texto("Título: "))),
        "3": lambda: print(servicio.comprar(
            pedir_texto("Título: "),
            pedir_texto("Autor: "),
            pedir_float("Precio: "),
            pedir_int("Cantidad: ")
        )),
        "4": lambda: print(servicio.vender(pedir_texto("Título: "))),
        "5": lambda: print("\n".join(servicio.catalogo())),
    }

    while True:
        print("""
=== MENÚ ===
1. Prestar
2. Devolver
3. Comprar
4. Vender
5. Catálogo
0. Salir
""")

        op = input("Opción: ").strip()
        if op == "0":
            print("Hasta luego.")
            break
        if op in opciones:
            opciones[op]()
        else:
            print("Opción inválida.")
