import sys
from models.tienda import Tienda
from models.carrito import Carrito

def print_menu():
    print("\n=== TIENDA (consola) ===")
    print("1) Listar productos")
    print("2) Agregar al carrito (SKU, cantidad)")
    print("3) Ver carrito")
    print("4) Eliminar ítem del carrito (SKU)")
    print("5) Finalizar compra")
    print("6) Ver total de ventas acumulado")
    print("0) Salir")

def listar_productos(tienda: Tienda):
    productos = tienda.listar_productos()
    print("\n=== CATÁLOGO ===")
    for p in productos:
        print(f"{p.sku:<6} | {p.nombre:<22} | ${p.precio_unitario:>10,.2f} | disp: {p.unidades_disponibles}")
    if not productos:
        print("(sin productos)")

def ver_carrito(carrito: Carrito):
    print()
    if carrito.esta_vacio():
        print("Carrito vacío")
    else:
        print(carrito)

def main():
    tienda = Tienda()
    tienda.cargar_productos_iniciales()  # datos de ejemplo listos para probar
    carrito = tienda.crear_carrito()

    while True:
        try:
            print_menu()
            opcion = input("Elige una opción: ").strip()

            if opcion == "1":
                listar_productos(tienda)

            elif opcion == "2":
                sku = input("SKU del producto: ").strip().upper()
                cantidad_str = input("Cantidad (unidades o kg si es WE): ").strip()
                try:
                    cantidad = float(cantidad_str)
                except ValueError:
                    print("Cantidad inválida.")
                    continue

                try:
                    tienda.agregar_producto_a_carrito(carrito, sku, cantidad)
                    print("Ítem agregado correctamente.")
                    ver_carrito(carrito)
                except ValueError as e:
                    print(f"Error: {e}")

            elif opcion == "3":
                ver_carrito(carrito)

            elif opcion == "4":
                sku = input("SKU a eliminar: ").strip().upper()
                if carrito.eliminar_item(sku):
                    print("Ítem eliminado.")
                else:
                    print("Ese SKU no está en el carrito.")
                ver_carrito(carrito)

            elif opcion == "5":
                try:
                    total = tienda.finalizar_compra(carrito)
                    print(f"\n¡Compra finalizada! Total: ${total:,.2f}")
                    # crear un carrito nuevo para continuar comprando si el usuario quiere
                    carrito = tienda.crear_carrito()
                except ValueError as e:
                    print(f"Error: {e}")

            elif opcion == "6":
                print(f"Total de ventas acumulado: ${tienda.obtener_total_ventas():,.2f}")

            elif opcion == "0":
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida.")

        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario.")
            sys.exit(0)

if __name__ == "__main__":
    main()
