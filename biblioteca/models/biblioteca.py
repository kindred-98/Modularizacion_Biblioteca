from .libro import Libro

class Biblioteca:
    """
    Gestiona un catálogo de libros y operaciones sobre ellos.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.catalogo: list[Libro] = []
        self.ingresos = 0.0

    def agregar_libro(self, libro: Libro):
        self.catalogo.append(libro)

    def buscar_libro(self, titulo: str) -> Libro | None:
        titulo = titulo.strip().lower()
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo:
                return libro
        return None

    def prestar_libro(self, titulo: str) -> str:
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if libro.prestado:
            return "⚠️ Ya está prestado."
        libro.prestado = True
        return "📖 Libro prestado."

    def devolver_libro(self, titulo: str) -> str:
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if not libro.prestado:
            return "⚠️ No estaba prestado."
        libro.prestado = False
        return "🔄 Libro devuelto."

    def comprar_libro(self, titulo: str, autor: str, precio: float, cantidad: int) -> str:
        existente = self.buscar_libro(titulo)
        if existente:
            existente.cantidad += cantidad
            return f"📦 Stock actualizado: {existente.cantidad} unidades."
        nuevo = Libro(titulo, autor, precio, cantidad)
        self.agregar_libro(nuevo)
        return "📚 Libro añadido al catálogo."

    def vender_libro(self, titulo: str) -> str:
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if libro.prestado:
            return "⚠️ No se puede vender un libro prestado."
        if libro.cantidad <= 0:
            return "⚠️ Sin stock."
        libro.cantidad -= 1
        self.ingresos += libro.precio
        return f"💰 Vendido por ${libro.precio:.2f}. Ingresos: ${self.ingresos:.2f}"

    def obtener_catalogo(self):
        return self.catalogo
