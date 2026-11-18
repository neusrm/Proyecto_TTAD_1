import json
from analysis import total_facturado, ventas_por_categoria, producto_mas_vendido


def main():
    with open("data.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    ventas = datos["ventas"]

    total = total_facturado(ventas)
    categorias = ventas_por_categoria(ventas)
    producto, cantidad = producto_mas_vendido(ventas)

    print("Total facturado:", total, "€")

    print("Ventas por categoría:")
    for categoria, importe in categorias.items():
        print(categoria, ":", importe, "€")

    print("Producto más vendido:", producto, "-", cantidad, "unidades")


if __name__ == "__main__":
    main()