"""
Interfaz de Menú
----------------

Contiene la interfaz de línea de comandos que interactúa con el usuario.
"""

from services.inventario_service import InventarioService
from models.biblioteca import Biblioteca
from models.libro import Libro


def iniciar_menu():
    """
    Inicia el menú interactivo de la biblioteca.
    """
    biblioteca = Biblioteca("Biblioteca Central")
    servicio = InventarioService(biblioteca)

    # Datos iniciales
    biblioteca.agregar_libro(Libro("El Quijote", "Cervantes", 15.00, 3))
    biblioteca.agregar_libro(Libro("Cien años", "García Márquez", 12.50, 2))
    biblioteca.agregar_libro(Libro("1984", "Orwell", 10.00, 1))

    opciones = {
        "1": lambda: print(servicio.prestar(input("Título: "))),
        "2": lambda: print(servicio.devolver(input("Título: "))),
        "3": lambda: print(servicio.comprar(
            input("Título: "),
            input("Autor: "),
            float(input("Precio: ")),
            int(input("Cantidad: "))
        )),
        "4": lambda: print(servicio.vender(input("Título: "))),
        "5": lambda: print("\n".join(servicio.catalogo()) or "(vacío)"),
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
            print("👋 ¡Hasta luego!")
            break
        elif op in opciones:
            opciones[op]()
        else:
            print("Opción inválida.")
