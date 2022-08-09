diccionario = {"Codigo": ["E-001", "E-002", "E-003", "E-004", "E-005"],
               "Nombre": ["Leche", "Azucar", "Arroz", "Tomates", "Huevos"],
               "Precio": ["4,40", "4,50", "3,80", "3,60", "6,20"]}
print(diccionario)
for key in diccionario:
    print(key, " : ", diccionario[key])

costo = 0
continuar = True
while continuar:
    codigo = input("Ingresa el codigo del producto: ")
    cantidad = int(input("Ingresa la cantidad de productos: "))
    continuar = input("¿Quieres añadir mas productos a la lista (Si/No)?: ") == "Si"

    if codigo == "E-001":
        nombre = "Leche"
        precio = 4.40
    elif codigo == "E-002":
        nombre = "Azucar"
        precio = 4.50
    elif codigo == "E-003":
        nombre = "Arroz"
        precio = 3.80
    elif codigo == "E-004":
        nombre = "Tomates"
        precio = 3.60
    elif codigo == "E-005":
        nombre = "Huevos"
        precio = 6.20
    tot = precio * cantidad
    costo += tot
    tupla = [str(codigo), '\t', nombre, '\t', str(cantidad), '\t', str(precio), '\t''\t', str(tot)]
    cadenavalores = "".join(tupla)
    f = open("demofile.txt", "a")
    f.write("\n" + cadenavalores)
    f.close()
f = open("demofile.txt")
print(f.read())
f.close()
print("El total de la compra es: ", costo)
