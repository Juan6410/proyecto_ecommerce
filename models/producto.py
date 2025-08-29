class Producto:
    
    def __init__(self, sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.unidades_disponibles = unidades_disponibles
        self.precio_unitario = precio_unitario

        from services.reglas_precio import ManejadorReglas
        self._manejador_reglas = ManejadorReglas()
    
    def tiene_unidades(self, cantidad):
        return self.unidades_disponibles >= cantidad
    
    def descontar_unidades(self, cantidad):
        if self.tiene_unidades(cantidad):
            self.unidades_disponibles -= cantidad
        else:
            raise ValueError("Stock insuficiente")
    
    def calcular_precio_total(self, cantidad):
        regla = self._manejador_reglas.obtener_regla(self.sku)
        return regla.calcular_total(cantidad, self.precio_unitario)
    
    def __str__(self):
        return f"{self.sku} - {self.nombre}: ${self.precio_unitario:,.0f} ({self.unidades_disponibles} disponibles)"