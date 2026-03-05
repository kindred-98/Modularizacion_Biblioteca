# Modularizacion_Biblioteca

# 📚 Sistema de Gestión de Biblioteca (Python)

Este proyecto implementa un sistema modular para gestionar una biblioteca: préstamo, devolución, compra, venta y visualización del catálogo.  
Está diseñado siguiendo principios de **Clean Code**, **arquitectura modular**, **separación de responsabilidades** y **POO**.

---

## 🧱 Estructura del proyecto

```
biblioteca/
│
├── models/
│   ├── libro.py
│   └── biblioteca.py
│
├── services/
│   └── inventario_service.py
│
├── ui/
│   └── menu.py
│
├── tests/
│   ├── test_libro.py
│   ├── test_biblioteca.py
│   └── test_inventario_service.py
│
├── main.py
└── README.md
```

### Roles de cada módulo

- **models/** → Clases puras (Libro, Biblioteca). Sin prints.
- **services/** → Lógica de negocio y mensajes para la UI.
- **ui/** → Interfaz de usuario (menú interactivo).
- **tests/** → Pruebas unitarias con pytest.
- **main.py** → Punto de entrada.

---

## ▶️ Ejecución

Ejecuta el menú principal:
```bash
python main.py
```

---

## 🧪 Ejecutar tests
Asegúrate de tener instalado pytest: 
```bash
pip install pytest
```
Ejecuta todos los tests:
```bash
pytest -v

```

---
## ✨ Características
-Gestión de catálogo (agregar, buscar, listar).
-Préstamo y devolución de libros.
-Compra y venta con control de stock.
-Registro de ingresos.
-Arquitectura limpia y extensible.
-Totalmente documentado con docstrings.

---
📄 Licencia
MIT License.
