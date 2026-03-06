"""
Esquema de validación para Libro usando Pydantic.
"""

from pydantic import BaseModel, Field


class LibroSchema(BaseModel):
    titulo: str = Field(..., min_length=1, description="Título del libro")
    autor: str = Field(..., min_length=1, description="Autor del libro")
    precio: float = Field(..., gt=0, description="Precio mayor que 0")
    cantidad: int = Field(..., ge=1, description="Cantidad mínima 1")

    class Config:
        validate_assignment = True
        anystr_strip_whitespace = True
