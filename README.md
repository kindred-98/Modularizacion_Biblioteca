<div align="center">

# 📚 Sistema de Gestión de Biblioteca Modular

Un sistema de gestión de biblioteca desarrollado en Python que demuestra las mejores prácticas de arquitectura de software: modularidad, separación de responsabilidades, validación robusta con Pydantic, y cobertura completa de pruebas unitarias. Diseñado para ser escalable, mantenible y extensible, este proyecto sirve como referencia para aplicaciones empresariales en Python.

---

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Pydantic](https://img.shields.io/badge/Validation-Pydantic-009688?style=for-the-badge&logo=pydantic)
![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?style=for-the-badge&logo=pytest)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Modular-FF9800?style=for-the-badge)
![Clean Code](https://img.shields.io/badge/Code-Clean_Code-blueviolet?style=for-the-badge)

</div>

---
## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Instalación](#instalación)
- [Uso](#uso)
- [Pruebas](#pruebas)
- [Validación de Datos](#validación-de-datos-con-pydantic)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Autor](#autor)

<a id="características"></a>
## ✨ Características

- **Gestión Completa del Catálogo**: Agregar, buscar, listar y gestionar libros con metadatos completos
- **Sistema de Inventario**: Control de stock, préstamos, devoluciones y operaciones comerciales
- **Validación Automática**: Uso de Pydantic para validación de datos de entrada y salida
- **Arquitectura Modular**: Separación clara entre modelos, servicios y interfaz de usuario
- **Pruebas Unitarias**: Cobertura completa con pytest para asegurar la calidad del código
- **Interfaz CLI**: Menú interactivo para operaciones del usuario
- **Documentación**: Código documentado con docstrings y README detallado

<a id="arquitectura"></a>
## 🏗️ Arquitectura

El proyecto sigue los principios de **Clean Architecture** y **Domain-Driven Design (DDD)**, organizando el código en capas bien definidas:

```
biblioteca/
│
├── models/                    # Capa de Dominio
│   ├── libro_schema.py        # Esquemas de validación (Pydantic)
│   ├── libro.py               # Entidad de dominio Libro
│   └── biblioteca.py          # Agregado raíz Biblioteca
│
├── services/                  # Capa de Aplicación
│   └── inventario_service.py  # Casos de uso y lógica de negocio
│
├── ui/                        # Capa de Presentación
│   └── menu.py                 # Interfaz de línea de comandos
│
├── tests/                     # Capa de Pruebas
│   ├── test_libro.py
│   ├── test_biblioteca.py
│   └── test_inventario_service.py
│
└── main.py                    # Punto de entrada
```

### Principios de Diseño Aplicados

- **Separación de Responsabilidades**: Cada módulo tiene una única responsabilidad
- **Inyección de Dependencias**: Los servicios dependen de abstracciones, no de implementaciones concretas
- **Validación en la Frontera**: Pydantic valida datos en el límite del sistema
- **Principio de Inversión de Dependencias**: Las capas superiores no dependen de las inferiores

<a id="instalación"></a>
## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/Modularizacion_Biblioteca.git
   cd Modularizacion_Biblioteca
   ```

2. **Crea un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

<a id="uso"></a>
## ▶️ Uso

### Ejecución del Programa

Para iniciar la aplicación, ejecuta:

```bash
python main.py
```

Esto abrirá un menú interactivo donde podrás:

- Agregar nuevos libros al catálogo
- Buscar libros por título, autor o ISBN
- Listar todos los libros disponibles
- Gestionar préstamos y devoluciones
- Realizar operaciones de compra/venta
- Ver reportes de ingresos

### Ejemplo de Uso Programático

```python
from biblioteca.models.libro import Libro
from biblioteca.services.inventario_service import InventarioService

# Crear un libro
libro = Libro(titulo="1984", autor="George Orwell", precio=25.99)

# Usar el servicio de inventario
servicio = InventarioService()
servicio.agregar_libro(libro)
```

<a id="pruebas"></a>
## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas unitarias usando pytest.

### Ejecutar las Pruebas

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con salida detallada
pytest -v

# Ejecutar con cobertura
pytest --cov=biblioteca --cov-report=html
```

### Estructura de Pruebas

- `test_libro.py`: Pruebas de la entidad Libro
- `test_biblioteca.py`: Pruebas del agregado Biblioteca
- `test_inventario_service.py`: Pruebas de los casos de uso

<a id="validación-de-datos-con-pydantic"></a>
## 🔍 Validación de Datos con Pydantic

Pydantic se utiliza para validar automáticamente todos los datos que entran al sistema, asegurando integridad y consistencia.

### Beneficios

1. **Validación Automática**: Tipos de datos, rangos y formatos se validan automáticamente
2. **Normalización**: Eliminación de espacios innecesarios, conversión de tipos
3. **Errores Estructurados**: Mensajes de error claros y localizables
4. **Separación de Preocupaciones**: La lógica de negocio se enfoca en reglas, no en validaciones básicas
5. **Preparación para APIs**: Compatible con FastAPI para futuras expansiones

### Integración en la Arquitectura

```
Input Usuario → UI → Servicio → Validación Pydantic → Modelo → Persistencia
```

Los esquemas Pydantic actúan como contratos entre capas, garantizando que solo datos válidos fluyan a través del sistema.

<a id="contribución"></a>
## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Guías de Contribución

- Sigue los principios de Clean Code
- Mantén la cobertura de pruebas > 90%
- Documenta nuevas funcionalidades con docstrings
- Actualiza el README si es necesario

<a id="licencia"></a>
## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---
<div align="center">

<a id="autor"></a>
## 👨‍💻 Autor

**Desarrollado por A.D.E.V - Demostrando las mejores prácticas en desarrollo Python**

[![GitHub](https://img.shields.io/badge/GitHub-@angel-181717?style=for-the-badge&logo=github)](https://github.com/angel/Modularizacion_Biblioteca)

</div>