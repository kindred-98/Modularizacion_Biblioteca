"""
Modelo de dominio Libro.
"""

from .libro_schema import LibroSchema


class Libro:
    """
    Representa un libro dentro del catálogo.
    """

    def __init__(self, titulo: str, autor: str, precio: float, cantidad: int = 1):
        # Validación automática con Pydantic
        data = LibroSchema(
            titulo=titulo,
            autor=autor,
            precio=precio,
            cantidad=cantidad
        )

        self.titulo = data.titulo
        self.autor = data.autor
        self.precio = data.precio
        self.cantidad = data.cantidad
        self.prestado = False

    def __str__(self):
        estado = "PRESTADO" if self.prestado else "DISPONIBLE"
        return f"[{estado}] '{self.titulo}' de {self.autor} — ${self.precio:.2f} ({self.cantidad} unid.)"

 