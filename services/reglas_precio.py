from abc import ABC, abstractmethod

class ReglaPrecio(ABC):
    """Interface ReglaPrecio según diagrama"""
    
    @abstractmethod
    def es_aplicable(self, sku):
        """Verifica si la regla aplica para un SKU específico"""
        pass
    
    @abstractmethod
    def calcular_total(self, cantidad, precio):
        """Calcula el precio total según la regla específica"""
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
    """
    ManejadorReglas según diagrama UML
    Principios aplicados:
    - Single Responsibility: Solo maneja la obtención de reglas
    - Open/Closed: Abierto para nuevas reglas, cerrado para modificación
    - Creator: Crea las instancias de reglas (GRASP)
    """
    
    def __init__(self):
        # Principio: Creator - ManejadorReglas crea las reglas
        self._reglas = [
            ReglaPrecioNormal(),
            ReglaPrecioPorPeso(),
            ReglaPrecioEspecial()
        ]
    
    def obtener_regla(self, sku):
        """
        Factory method para obtener la regla correcta
        Principio: Expert Information - tiene la información para decidir
        
        Args:
            sku: Código del producto
            
        Returns:
            ReglaPrecio: Instancia de la regla apropiada
            
        Raises:
            ValueError: Si no existe regla para el SKU
        """
        for regla in self._reglas:
            if regla.es_aplicable(sku):
                return regla
        
        raise ValueError(f"No existe regla de precio para el SKU: {sku}")
    
    def agregar_regla(self, regla):
        """
        Permite agregar nuevas reglas dinámicamente
        Principio: Open/Closed - extensible sin modificar código existente
        """
        if not isinstance(regla, ReglaPrecio):
            raise TypeError("La regla debe implementar ReglaPrecio")
        
        self._reglas.append(regla)