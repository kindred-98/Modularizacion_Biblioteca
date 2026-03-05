from models.biblioteca import Biblioteca
from models.libro import Libro

def test_agregar_y_buscar_libro():
    b = Biblioteca("Test")
    libro = Libro("Dune", "Herbert", 20.0)
    b.agregar_libro(libro)

    encontrado = b.buscar_libro("Dune")
    assert encontrado is not None
    assert encontrado.titulo == "Dune"

def test_prestar_y_devolver():
    b = Biblioteca("Test")
    b.agregar_libro(Libro("Dune", "Herbert", 20.0))

    assert b.prestar_libro("Dune") is True
    assert b.prestar_libro("Dune") is False  # ya prestado
    assert b.devolver_libro("Dune") is True
    assert b.devolver_libro("Dune") is False  # ya devuelto

def test_vender_libro():
    b = Biblioteca("Test")
    b.agregar_libro(Libro("Dune", "Herbert", 20.0, 1))

    assert b.vender_libro("Dune") is True
    assert b.vender_libro("Dune") is False  # sin stock
