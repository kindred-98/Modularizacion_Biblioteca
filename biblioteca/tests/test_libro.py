from models.libro import Libro

def test_creacion_libro():
    libro = Libro("1984", "Orwell", 10.0, 2)
    assert libro.titulo == "1984"
    assert libro.autor == "Orwell"
    assert libro.precio == 10.0
    assert libro.cantidad == 2
    assert libro.prestado is False