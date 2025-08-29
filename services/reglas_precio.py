from abc import ABC, abstractmethod

class ReglaPrecio(ABC):
    @abstractmethod
    def es_aplicable(self, sku):
        pass
    
    @abstractmethod
    def calcular_total(self, cantidad, precio):
        pass


class ReglaPrecioNormal(ReglaPrecio):
    """Regla para productos normales (EA)"""
    
    def es_aplicable(self, sku):
        return sku.startswith("EA")
    
    def calcular_total(self, cantidad, precio):
        return cantidad * precio


class ReglaPrecioPorPeso(ReglaPrecio):
    """Regla para productos por peso (WE)"""
    
    def es_aplicable(self, sku):
        return sku.startswith("WE")
    
    def calcular_total(self, cantidad, precio):
        # cantidad en kg, precio por gramo
        gramos_totales = cantidad * 1000
        return gramos_totales * precio


class ReglaPrecioEspecial(ReglaPrecio):
    """Regla para productos con descuento especial (SP)"""
    
    def es_aplicable(self, sku):
        return sku.startswith("SP")
    
    def calcular_total(self, cantidad, precio):
        precio_base = cantidad * precio
        grupos_descuento = cantidad // 3
        porcentaje_descuento = min(grupos_descuento * 0.20, 0.50)
        descuento = precio_base * porcentaje_descuento
        return precio_base - descuento


class ManejadorReglas:
    
    def __init__(self):
        # Principio: Creator - ManejadorReglas crea las reglas
        self._reglas = [
            ReglaPrecioNormal(),
            ReglaPrecioPorPeso(),
            ReglaPrecioEspecial()
        ]
    
    def obtener_regla(self, sku):
        for regla in self._reglas:
            if regla.es_aplicable(sku):
                return regla
        
        raise ValueError(f"No existe regla de precio para el SKU: {sku}")
    
    def agregar_regla(self, regla):
        if not isinstance(regla, ReglaPrecio):
            raise TypeError("La regla debe implementar ReglaPrecio")
        
        self._reglas.append(regla)