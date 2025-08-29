from abc import ABC, abstractmethod
import math

class ReglaPrecio(ABC):
    """Interfaz para todas las reglas de precio (Strategy Pattern)"""
    
    @abstractmethod
    def calcular_total(self, cantidad, precio_unitario):
        """
        Calcula el precio total según la regla específica
        
        Args:
            cantidad: Cantidad de unidades
            precio_unitario: Precio por unidad del producto
        
        Returns:
            float: Precio total calculado
        """
        pass
    
    @abstractmethod
    def es_aplicable(self, sku):
        """
        Verifica si la regla aplica para un SKU específico
        
        Args:
            sku: Código del producto
        
        Returns:
            bool: True si la regla aplica
        """
        pass


class ReglaPrecioNormal(ReglaPrecio):
    """Regla para productos normales (EA): precio * cantidad"""
    
    def calcular_total(self, cantidad, precio_unitario):
        return cantidad * precio_unitario
    
    def es_aplicable(self, sku):
        return sku.startswith("EA")


class ReglaPrecioPorPeso(ReglaPrecio):
    """
    Regla para productos por peso (WE): 
    precio_unitario está en gramos, se calcula por kilogramos
    """
    
    def calcular_total(self, cantidad, precio_unitario):
        # cantidad = kilogramos, precio_unitario = precio por gramo
        gramos_totales = cantidad * 1000  # convertir kg a gramos
        return gramos_totales * precio_unitario
    
    def es_aplicable(self, sku):
        return sku.startswith("WE")


class ReglaPrecioEspecial(ReglaPrecio):
    """
    Regla para productos con descuento especial (SP):
    20% descuento por cada 3 unidades, máximo 50% de descuento
    """
    
    def calcular_total(self, cantidad, precio_unitario):
        precio_base = cantidad * precio_unitario
        
        # Calcular grupos de 3 unidades
        grupos_descuento = cantidad // 3
        
        # Calcular porcentaje de descuento (20% por grupo, máximo 50%)
        porcentaje_descuento = min(grupos_descuento * 0.20, 0.50)
        
        # Aplicar descuento
        descuento = precio_base * porcentaje_descuento
        precio_final = precio_base - descuento
        
        return precio_final
    
    def es_aplicable(self, sku):
        return sku.startswith("SP")


# Función helper para obtener la regla correcta (opcional)
def obtener_regla_precio(sku):
    """
    Factory function para obtener la regla de precio correcta
    
    Args:
        sku: Código del producto
    
    Returns:
        ReglaPrecio: Instancia de la regla apropiada
    
    Raises:
        ValueError: Si el SKU no corresponde a ninguna regla
    """
    reglas = [
        ReglaPrecioNormal(),
        ReglaPrecioPorPeso(),
        ReglaPrecioEspecial()
    ]
    
    for regla in reglas:
        if regla.es_aplicable(sku):
            return regla
    
    raise ValueError(f"No existe regla de precio para el SKU: {sku}")