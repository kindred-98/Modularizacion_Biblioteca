from models.biblioteca import Biblioteca
from models.libro import Libro
from services.inventario_service import InventarioService

def test_servicio_prestar():
    b = Biblioteca("Test")
    b.agregar_libro(Libro("Dune", "Herbert", 20.0))
    s = InventarioService(b)

    assert "prestado" in s.prestar("Dune").lower()

def test_servicio_catalogo():
    b = Biblioteca("Test")
    b.agregar_libro(Libro("Dune", "Herbert", 20.0))
    s = InventarioService(b)

    catalogo = s.catalogo()
    assert len(catalogo) == 1
    assert "Dune" in catalogo[0]
