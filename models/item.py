class Item:
    
    def __init__(self, producto, cantidad):
        """
        Inicializa un item del carrito
        
        Args:
            producto: Instancia de Producto
            cantidad: Cantidad de unidades/kilogramos
        
        Raises:
            ValueError: Si cantidad inválida o stock insuficiente
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        
        if not producto.tiene_unidades(cantidad):
            raise ValueError(f"Stock insuficiente. Disponible: {producto.unidades_disponibles}, solicitado: {cantidad}")
        
        self.producto = producto
        self.cantidad = cantidad
        self._total = self.calcular_total()
    
    def calcular_total(self):
        return self.producto.calcular_precio_total(self.cantidad)
    
    def obtener_total(self):
        return self._total
    
    def actualizar_cantidad(self, nueva_cantidad):
        if nueva_cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        
        diferencia = nueva_cantidad - self.cantidad
        
        if diferencia > 0: 
            if not self.producto.tiene_unidades(diferencia):
                return False
        
        self.cantidad = nueva_cantidad
        self._total = self.calcular_total()
        return True
    
    def __str__(self):
        if self.producto.sku.startswith("WE"):
            # Para productos por peso, mostrar en kg
            return f"{self.producto.nombre} - Cantidad: {self.cantidad} kg - Subtotal: ${self._total:,.2f}"
        else:
            # Para productos especiales
            if isinstance(self.cantidad, float):
                cantidad_display = int(self.cantidad) if self.cantidad.is_integer() else self.cantidad
            else:
                cantidad_display = self.cantidad
            return f"{self.producto.nombre} - Cantidad: {cantidad_display} unidades - Subtotal: ${self._total:,.2f}"

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.producto.sku == other.producto.sku
