def mostrar_bienvenida():
    print("=" * 40)
    print("    CAFETERIA - EL BUEN CAFÉ")
    print("=" * 40)
    print("  Bienvenidos/ al Buen Café.")
    print()

def mostrar_menu():
    print("\n----- MENÚ PRINCIPAL -----")
    print("1. Ver menú de productos")
    print("2. Agregar producto al pedido")
    print("3. Ver pedido actual")
    print("4. Pagar y generar factura")
    print("5. Salir")

def mostrar_catalogo_de_productos(nombres, tamaños, precios):
    print("\n----- CATÁLOGO DE PRODUCTOS -----")
    # Usamos un ciclo for para mostrar las listas paralelas
    for i in range(len(nombres)):
        print(f"{i + 1}. {nombres[i]} - Tamaño: {tamaños[i]} - ${precios[i]:,}")

def agregar_producto_al_pedido(nombres, tamaños, precios, pedidos_nombres, pedidos_precios, pedidos_cantidades):
    mostrar_catalogo_de_productos(nombres, tamaños, precios)
    
    seleccion = input("\nIngresa el número del producto que deseas: ")
    
    # Validación básica (Punto 5 del requerimiento)
    if not seleccion.isdigit():
        print("Error: Debes ingresar un número válido.")
        return
    
    seleccion = int(seleccion)
    if seleccion < 1 or seleccion > len(nombres):
        print("Error: El producto no existe en el catálogo.")
        return
    
    cantidad = input("¿Cuántas unidades desea? ")
    if not cantidad.isdigit() or int(cantidad) < 1:
        print("Error: La cantidad debe ser un número mayor a 0.")
        return
    
    indice = seleccion - 1
    # Guardamos los datos en nuestras listas de pedido
    pedidos_nombres.append(nombres[indice])
    pedidos_precios.append(precios[indice])
    pedidos_cantidades.append(int(cantidad))
    
    print(f"\nSe agregó: {cantidad} x {nombres[indice]} al pedido.")

def ver_pedido_actual(pedidos_nombres, pedidos_precios, pedidos_cantidades):
    if len(pedidos_nombres) == 0:
        print("\nTu pedido actual está vacío.")
        return
    
    print("\n---- TU PEDIDO ACTUAL ----")
    for i in range(len(pedidos_nombres)):
        subtotal_item = pedidos_precios[i] * pedidos_cantidades[i]
        print(f"{i+1}. {pedidos_nombres[i]} x{pedidos_cantidades[i]} - ${subtotal_item:,}")

def generar_factura(pedidos_nombres, pedidos_precios, pedidos_cantidades):
    if len(pedidos_nombres) == 0:
        print("\nNo hay productos en tu pedido. Agrega algo primero.")
        return
    
    print("\n" + "=" * 40)
    print("    FACTURA CAFETERIA-EL BUEN CAFÉ")
    print("=" * 40)
    
    subtotal = 0
    for i in range(len(pedidos_nombres)):
        costo_linea = pedidos_precios[i] * pedidos_cantidades[i]
        subtotal += costo_linea
        print(f"{pedidos_nombres[i]} x{pedidos_cantidades[i]}: ${costo_linea:,}")
    
    # --- REQUISITO ADICIONAL: Descuento del 10% si supera $50.000 ---
    descuento = 0
    if subtotal > 50000:
        descuento = subtotal * 0.10
    
    subtotal_con_descuento = subtotal - descuento
    iva = subtotal_con_descuento * 0.19
    total = subtotal_con_descuento + iva
    
    print("-" * 40)
    print(f"Subtotal:       ${subtotal:,.0f}")
    if descuento > 0:
        print(f"Descuento 10%: -${descuento:,.0f}")
    print(f"IVA (19%):      ${iva:,.0f}")
    print(f"TOTAL A PAGAR:  ${total:,.0f}")
    print("=" * 40)
    print("    ¡Gracias por su compra!")
    
    # IMPORTANTE: Al finalizar la compra, vaciamos el pedido para el siguiente cliente
    pedidos_nombres.clear()
    pedidos_precios.clear()
    pedidos_cantidades.clear()

def main():
    # Catálogo (Listas Paralelas - Punto 2)
    productos = ["Café Americano", "Capuccino", "Latte Vainilla", "Chocolate Caliente", "Jugo Naranja", "Croissant"]
    tamaños = ["Mediano", "Grande", "Grande", "Mediano", "Grande", "---"]
    precios = [5000, 8500, 9000, 7000, 6500, 8000]
    
    # Listas vacías para el pedido
    ped_nombres = []
    ped_precios = []
    ped_cantidades = []
    
    mostrar_bienvenida()
    
    # Bucle infinito para que el programa se mantenga abierto (Punto 10)
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            mostrar_catalogo_de_productos(productos, tamaños, precios)
        elif opcion == "2":
            agregar_producto_al_pedido(productos, tamaños, precios, ped_nombres, ped_precios, ped_cantidades)
        elif opcion == "3":
            ver_pedido_actual(ped_nombres, ped_precios, ped_cantidades)
        elif opcion == "4":
            generar_factura(ped_nombres, ped_precios, ped_cantidades)
        elif opcion == "5":
            print("\nGracias por su visita, ¡hasta pronto!")
            continuar = False # Esto rompe el ciclo y cierra el programa
        else:
            print("\nOpción no válida. Intenta de nuevo.")

# Punto de entrada del programa5

if __name__ == "__main__":
    main()