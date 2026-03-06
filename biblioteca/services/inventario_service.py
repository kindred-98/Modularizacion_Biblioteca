from pydantic import ValidationError
from models.biblioteca import Biblioteca
from models.libro import Libro

class InventarioService:
    """
    Servicio que conecta la UI con la lógica de negocio.
    """

    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def prestar(self, titulo: str) -> str:
        return self.biblioteca.prestar_libro(titulo)

    def devolver(self, titulo: str) -> str:
        return self.biblioteca.devolver_libro(titulo)

    def comprar(self, titulo: str, autor: str, precio: float, cantidad: int) -> str:
        try:
            return self.biblioteca.comprar_libro(titulo, autor, precio, cantidad)
        except ValidationError as e:
            return f"❌ Datos inválidos: {e.errors()}"

    def vender(self, titulo: str) -> str:
        return self.biblioteca.vender_libro(titulo)

    def catalogo(self) -> list[str]:
        return [str(libro) for libro in self.biblioteca.obtener_catalogo()]
