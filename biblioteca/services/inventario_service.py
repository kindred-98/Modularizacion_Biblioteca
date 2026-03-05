"""
Servicio de Inventario
----------------------

Contiene funciones que conectan la lógica de negocio con la interfaz
de usuario, devolviendo mensajes claros según el resultado.
"""

from models.biblioteca import Biblioteca


class InventarioService:
    """
    Servicio que encapsula operaciones de la biblioteca y devuelve
    mensajes listos para mostrar en la interfaz.
    """

    def __init__(self, biblioteca: Biblioteca):
        self.biblioteca = biblioteca

    def prestar(self, titulo: str) -> str:
        return "📖 Libro prestado." if self.biblioteca.prestar_libro(titulo) else "❌ No se pudo prestar."

    def devolver(self, titulo: str) -> str:
        return "🔄 Libro devuelto." if self.biblioteca.devolver_libro(titulo) else "❌ No se pudo devolver."

    def comprar(self, titulo: str, autor: str, precio: float, cantidad: int) -> str:
        self.biblioteca.comprar_libro(titulo, autor, precio, cantidad)
        return "📦 Compra registrada."

    def vender(self, titulo: str) -> str:
        return "💰 Venta realizada." if self.biblioteca.vender_libro(titulo) else "❌ No se pudo vender."

    def catalogo(self) -> list[str]:
        return [str(libro) for libro in self.biblioteca.obtener_catalogo()]
