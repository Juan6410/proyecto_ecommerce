from models.producto import Producto
from models.carrito import Carrito

class Tienda:
    def __init__(self):
        self.productos = {}  # Diccionario: sku -> producto
        self._total_ventas = 0.0
    
    def agregar_producto_al_catalogo(self, sku, nombre, descripcion, unidades_disponibles, precio_unitario):
        if sku in self.productos:
            raise ValueError(f"El producto {sku} ya existe en el catálogo")
        
        producto = Producto(sku, nombre, descripcion, unidades_disponibles, precio_unitario)
        self.productos[sku] = producto
        return producto
    
    def buscar_producto(self, sku):
        return self.productos.get(sku)
    
    def listar_productos(self):
        return list(self.productos.values())
    
    def crear_carrito(self):
        return Carrito()
    
    def agregar_producto_a_carrito(self, carrito, sku, cantidad):
        producto = self.buscar_producto(sku)
        if not producto:
            raise ValueError(f"Producto {sku} no encontrado")
        
        return carrito.agregar_item(producto, cantidad)
    
    def finalizar_compra(self, carrito):
        total_compra = carrito.finalizar_compra()
        self._total_ventas += total_compra
        return total_compra
    
    def obtener_total_ventas(self):
        return self._total_ventas
    
    def cargar_productos_iniciales(self):
        #productos de prueba precargados
        productos_iniciales = [
            ("EA001", "Laptop Gaming", "Laptop para juegos de alto rendimiento", 10, 1500000),
            ("EA002", "Mouse Inalámbrico", "Mouse ergonómico inalámbrico", 25, 45000),
            ("WE001", "Carne de Res", "Carne premium por gramo", 5000, 15),
            ("WE002", "Pollo", "Pechuga de pollo por gramo", 3000, 8),
            ("SP001", "Auriculares", "Auriculares inalámbricos con descuento", 20, 80000),
            ("SP002", "Teclado Mecánico", "Teclado gaming con descuento especial", 15, 120000)
        ]
        
        for sku, nombre, desc, unidades, precio in productos_iniciales:
            self.agregar_producto_al_catalogo(sku, nombre, desc, unidades, precio)