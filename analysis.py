def total_facturado(ventas):
    total = 0

    for venta in ventas:
        total = total + venta["cantidad"] * venta["precio_unitario"]

    return total

def ventas_por_categoria(ventas):
    categorias = {}

    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]

        if categoria in categorias:
            categorias[categoria] = categorias[categoria] + importe
        else:
            categorias[categoria] = importe

    return categorias

def producto_mas_vendido(ventas):
    productos = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]

        if producto in productos:
            productos[producto] = productos[producto] + cantidad
        else:
            productos[producto] = cantidad

    producto_mayor = max(productos, key=productos.get)

    return producto_mayor, productos[producto_mayor]