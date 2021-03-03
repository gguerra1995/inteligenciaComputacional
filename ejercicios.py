def llantas_ponchadas(cantidad):
    if cantidad < 5:
        precio = 300
    elif (cantidad >= 5) & (cantidad < 10):
        precio = 250
    else:
        precio = 200
    print(f"El precio unitario de las llantas ponchadas es: {precio}, además, el total a pagar es: {cantidad*precio}")

llantas_ponchadas(5)
llantas_ponchadas(4)
llantas_ponchadas(10)


def valor_final_televisores(valor, cedula):
    if cedula[-2:] == "01":
        print(f"El valor final por la compra de televisores es: {valor-(valor*0.1)} (descuento del 10%)")
    elif cedula[-2:] == "25":
        print(f"El valor final por la compra de televisores es: {valor-(valor*0.2)} (descuento del 20%)")
    elif cedula[-2:] == "44":
        print(f"El valor final por la compra de televisores es: {valor-(valor*0.35)} (descuento del 35%)")
    elif cedula[-2:] == "57":
        print(f"El valor final por la compra de televisores es: {valor-(valor*0.5)} (descuento del 50%)")
    else:
        print(f"El valor final por la compra de televisores es: {valor} (No hubo descuento)")

valor_final_televisores(50000,"01")
valor_final_televisores(50000,"25")
valor_final_televisores(50000,"44")
valor_final_televisores(50000,"57")
valor_final_televisores(50000,"99")

def descuento_colchones(precio_unitario, cantidad):
    if (cantidad >= 0) & (cantidad < 3):
        print(f"El descuento a hacer es del 0%, el precio final es: {precio_unitario*cantidad}")
    elif (cantidad >= 3) & (cantidad < 6):
        print(f"El descuento a hacer es del 20%, el precio final es: {(precio_unitario*cantidad)-(precio_unitario*cantidad*0.2)}")
    elif (cantidad >= 6) & (cantidad < 8):
        print(f"El descuento a hacer es del 25%, el precio final es: {(precio_unitario*cantidad)-(precio_unitario*cantidad*0.25)}")
    elif cantidad >= 8:
        print(f"El descuento a hacer es del 30%, el precio final es: {(precio_unitario*cantidad)-(precio_unitario*cantidad*0.3)}")

descuento_colchones(5000,1)
descuento_colchones(5000,5)
descuento_colchones(5000,7)
descuento_colchones(5000,9)


def muestra_estudiantes(numero):
    if numero < 20:
        print(f"Se tomará el 50% del salón, el cual es: {int(numero*0.5)}")
    elif (numero >= 20) & (numero < 30):
        print(f"Se tomará el 60% del salón, el cual es: {int(numero*0.6)}")
    elif numero >= 30:
        print(f"Se tomará el 70% del salón, el cual es: {int(numero*0.7)}")

muestra_estudiantes(19)
muestra_estudiantes(26)
muestra_estudiantes(32)