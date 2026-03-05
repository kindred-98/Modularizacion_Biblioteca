"""
Módulo biblioteca
-----------------

Define la clase Biblioteca, que gestiona un catálogo de libros y
opera sobre ellos (agregar, buscar, prestar, vender, etc.).
"""

from .libro import Libro


class Biblioteca:
    """
    Representa una biblioteca con un catálogo de libros y registro de ingresos.

    Atributos
    ---------
    nombre : str
        Nombre de la biblioteca.
    catalogo : list[Libro]
        Lista de libros disponibles.
    ingresos : float
        Total acumulado por ventas.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo: list[Libro] = []
        self.ingresos = 0.0

    def agregar_libro(self, libro: Libro) -> None:
        """Agrega un libro al catálogo."""
        self.catalogo.append(libro)

    def buscar_libro(self, titulo: str) -> Libro | None:
        """Busca un libro por título (insensible a mayúsculas)."""
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo: str) -> bool:
        """Marca un libro como prestado si está disponible."""
        libro = self.buscar_libro(titulo)
        if libro and not libro.prestado:
            libro.prestado = True
            return True
        return False

    def devolver_libro(self, titulo: str) -> bool:
        """Devuelve un libro previamente prestado."""
        libro = self.buscar_libro(titulo)
        if libro and libro.prestado:
            libro.prestado = False
            return True
        return False

    def comprar_libro(self, titulo: str, autor: str, precio: float, cantidad: int = 1) -> None:
        """Añade stock o crea un nuevo libro."""
        existente = self.buscar_libro(titulo)
        if existente:
            existente.cantidad += cantidad
        else:
            self.agregar_libro(Libro(titulo, autor, precio, cantidad))

    def vender_libro(self, titulo: str) -> bool:
        """Vende un libro si hay stock y no está prestado."""
        libro = self.buscar_libro(titulo)
        if libro and libro.cantidad > 0 and not libro.prestado:
            libro.cantidad -= 1
            self.ingresos += libro.precio
            return True
        return False

    def obtener_catalogo(self) -> list[Libro]:
        """Devuelve la lista de libros del catálogo."""
        return self.catalogo
