"""
Módulo libro
------------

Define la clase Libro, que representa un libro dentro del catálogo
de la biblioteca. Contiene atributos básicos y métodos de utilidad.
"""

class Libro:
    """
    Representa un libro con título, autor, precio, cantidad y estado de préstamo.

    Atributos
    ---------
    titulo : str
        Título del libro.
    autor : str
        Autor del libro.
    precio : float
        Precio unitario del libro.
    cantidad : int
        Cantidad disponible en inventario.
    prestado : bool
        Indica si el libro está prestado.
    """

    def __init__(self, titulo: str, autor: str, precio: float, cantidad: int = 1):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.cantidad = cantidad
        self.prestado = False

    def __str__(self) -> str:
        """
        Devuelve una representación legible del libro.

        Returns
        -------
        str
            Cadena con el estado, título, autor, precio y cantidad.
        """
        estado = "PRESTADO" if self.prestado else "DISPONIBLE"
        return f"[{estado}] '{self.titulo}' de {self.autor} — ${self.precio:.2f} ({self.cantidad} unid.)"
