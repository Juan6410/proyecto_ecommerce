from models.item import Item

class Carrito:
    def __init__(self):
        self.items = []
        self._total_ventas = 0.0
    
    def agregar_item(self, producto, cantidad):
        # Buscar si ya existe el producto en el carrito
        for item in self.items:
            if item.producto.sku == producto.sku:
                if item.actualizar_cantidad(item.cantidad + cantidad):
                    return True
                else:
                    raise ValueError("No se puede agregar: stock insuficiente")
        
        # Si no existe, crear nuevo item
        nuevo_item = Item(producto, cantidad)
        self.items.append(nuevo_item)
        return True
    
    def eliminar_item(self, sku):
        for i, item in enumerate(self.items):
            if item.producto.sku == sku:
                self.items.pop(i)
                return True
        return False
    
    def calcular_total(self):
        return sum(item.obtener_total() for item in self.items)
    
    def finalizar_compra(self):
        if not self.items:
            raise ValueError("El carrito está vacío")
        
        # Descontar unidades del inventario
        for item in self.items:
            item.producto.descontar_unidades(item.cantidad)
        
        total_compra = self.calcular_total()
        self._total_ventas += total_compra
        
        # Limpiar carrito
        self.items.clear()
        
        return total_compra
    
    def esta_vacio(self):
        return len(self.items) == 0
    
    def __str__(self):
        if self.esta_vacio():
            return "Carrito vacío"
        
        resultado = "=== CARRITO DE COMPRAS ===\n"
        for item in self.items:
            resultado += f"{item}\n"
        resultado += f"TOTAL: ${self.calcular_total():,.2f}"
        return resultado