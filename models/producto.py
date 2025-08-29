from abc import ABC, abstractmethod
from services.reglas_precio import ReglaPrecioNormal, ReglaPrecioPorPeso, ReglaPrecioEspecial

class Producto(ABC):
    def __init__(self, sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponibles = unidades_disponibles
        self.precio_unitario = precio_unitario
        self._regla_precio = self._obtener_regla_precio()
    
    @abstractmethod
    def _obtener_regla_precio(self):
        """Cada tipo de producto define su regla de precio"""
        pass
    
    def tiene_unidades(self, cantidad):
        return self.unidades_disponibles >= cantidad
    
    def descontar_unidades(self, cantidad):
        if self.tiene_unidades(cantidad):
            self.unidades_disponibles -= cantidad
            return True
        return False
    
    def calcular_precio_total(self, cantidad):
        return self._regla_precio.calcular_total(cantidad, self.precio_unitario)
    
    @staticmethod
    def crear_producto(sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        """Factory method para crear el tipo correcto de producto según SKU"""
        if sku.startswith("EA"):
            return ProductoNormal(sku, nombre, descripcion, unidades_disponibles, precio_unitario)
        elif sku.startswith("WE"):
            return ProductoPorPeso(sku, nombre, descripcion, unidades_disponibles, precio_unitario)
        elif sku.startswith("SP"):
            return ProductoDescuentoEspecial(sku, nombre, descripcion, unidades_disponibles, precio_unitario)
        else:
            raise ValueError(f"SKU no válido: {sku}")
    
    def __str__(self):
        return f"{self.sku} - {self.nombre}: ${self.precio_unitario:,.0f} ({self.unidades_disponibles} disponibles)"


class ProductoNormal(Producto):
    def _obtener_regla_precio(self):
        return ReglaPrecioNormal()


class ProductoPorPeso(Producto):
    def _obtener_regla_precio(self):
        return ReglaPrecioPorPeso()


class ProductoDescuentoEspecial(Producto):
    def _obtener_regla_precio(self):
        return ReglaPrecioEspecial()