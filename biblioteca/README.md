# Modularizacion_Biblioteca

# 📚 Sistema de Gestión de Biblioteca — Arquitectura Modular en Python
Un proyecto diseñado para demostrar cómo construir una aplicación real aplicando arquitectura modular, POO, Clean Code, validación profesional con Pydantic y separación estricta de responsabilidades.
El resultado es un sistema robusto, escalable y fácil de mantener, ideal como base para proyectos más grandes o como ejemplo de buenas prácticas en Python.
---

## 🧱 Estructura del proyecto

```
biblioteca/
│
├── models/
│   ├── libro_schema.py      # Validación automática con Pydantic
│   ├── libro.py             # Modelo de dominio (POO)
│   └── biblioteca.py        # Lógica interna del catálogo
│
├── services/
│   └── inventario_service.py 
│   # Reglas de negocio y comunicación con la UI
│
├── ui/
│   └── menu.py               # Interfaz de usuario (CLI)
│
├── tests/
│   ├── test_libro.py
│   ├── test_biblioteca.py
│   └── test_inventario_service.py
│
├── main.py
└── README.md

```

### 🧩 Roles de cada capa
-models/ → Modelos de dominio y validación de datos.
-services/ → Lógica de negocio, reglas y mensajes.
-ui/ → Interacción con el usuario (CLI).
-tests/ → Pruebas unitarias con pytest.
-main.py → Punto de entrada de la aplicación.
Esta estructura permite mantener el código limpio, desacoplado y preparado para crecer.

---

## ▶️ Ejecución del Programa ⚙️ 

Ejecuta el menú principal:
```bash
python main.py
```

---

## 🧪 Pruebas Unitarias

Asegúrate de tener instalado pytest: 
```bash
pip install pytest
```
Ejecuta todos los tests:
```bash
pytest -v

```

---
## ✨ Características Principales
-Gestión completa del catálogo (agregar, buscar, listar).
-Préstamo y devolución de libros.
-Compra y venta con control de stock.
-Registro automático de ingresos.
-Arquitectura modular y escalable.
-Validación automática con Pydantic.
-Código documentado con docstrings.
-Tests unitarios incluidos.

---

## 🧩 Validación de Datos con Pydantic
El proyecto utiliza Pydantic para garantizar que todos los datos que entran al sistema sean válidos antes de crear o modificar un libro.
Esto aporta seguridad, limpieza y profesionalidad al código.

### ¿Qué aporta Pydantic aquí?
1-Valida tipos y reglas automáticamente (precio > 0, cantidad ≥ 1, textos no vacíos).
2-Normaliza cadenas (elimina espacios innecesarios).
3-Evita objetos inválidos dentro del catálogo.
4-Genera errores estructurados, fáciles de manejar en la capa de servicios.
5-Separa la validación del modelo, manteniendo el código limpio.
6-Prepara el proyecto para una futura API REST, ya que Pydantic es estándar en FastAPI.

### Cómo se integra
1-LibroSchema (Pydantic) valida los datos de entrada.
2-Libro recibe datos ya validados y se mantiene libre de validaciones manuales.
3-InventarioService captura errores de validación y los transforma en mensajes claros.
4-La UI solo pide datos, sin preocuparse por reglas o formatos.
Este enfoque profesional garantiza que el sistema sea robusto, mantenible y escalable.

📄 Licencia
MIT License.
