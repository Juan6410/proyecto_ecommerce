# Proyecto E-commerce

Tienda virtual por consola en Python con carrito de compras y diferentes tipos de productos.

## Tipos de productos
- **EA**: Normales (precio × cantidad)
- **WE**: Por peso (kg × precio por gramo)  
- **SP**: Descuento especial (20% cada 3 unidades, máx 50%)

## Ejecutar
```bash
python main.py
```

## Estructura
```
proyecto_ecommerce/
├── models/
│   ├── producto.py
│   ├── item.py
│   ├── carrito.py
│   └── tienda.py
├── services/
│   └── reglas_precio.py
└── main.py
```

## Uso
1. Ver catálogo
2. Agregar productos al carrito (SKU + cantidad)
3. Ver carrito actual
4. Eliminar items
5. Finalizar compra
6. Ver ventas totales

## Ejemplos
- `EA001`: Laptop $1,500,000 × 2 = $3,000,000
- `WE001`: Carne $15/g × 2.5kg = $37,500
- `SP001`: 10 Auriculares $80,000 → 50% desc = $400,000
