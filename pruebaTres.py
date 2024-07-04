reservas = []
def agregarReserva(nombre, ciudad, tour, cantidad):
    tours = ["Torres del paine", "Chiloé", "Carretera austral"]
    if tour not in tours:
        print("Tour no encontrado")
        return
    datos = {}
    datos["Cliente"] = nombre
    datos["Ciudad"] = ciudad
    datos["Tour"] = tour
    datos["Cantidad"] = cantidad
    reservas.append(datos)
def listarReservas(reservas):
    for reserva in reservas:
        print(reserva)
def imprimirDestino(reservas,tour):
    for i in reservas:
        if i["Tour"] == tour:
            with open(f"{tour}.txt", 'a') as archivo:
                archivo.write(str(i))
                archivo.write("\n")

while True:
    print("Bienvenido a SurExplora, ¿Qué desea hacer?(Ingrese el número)")
    print("""1.Registrar reserva
2.Listar todas las reservas
3.Imprimir detalle de reservas por destino
4.Salir""")
    opcion = int(input(""))
    if opcion == 1:
        nombre = input("Ingrese nombre y apellido: ")
        ciudad = input("Ingrese ciudad: ")
        tour = input("Ingrese detalle del tour: ").capitalize()
        cantidad = int(input("Ingrese la cantidad de personas: "))
        agregarReserva(nombre,ciudad,tour,cantidad)
    if opcion == 2:
        listarReservas(reservas)
    if opcion == 3:
        tour = input("Ingrese el destino del tour: ")
        imprimirDestino(reservas,tour)
    if opcion == 4:
        break
    input("¿Desea hacer algo más?")