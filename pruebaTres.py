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
#Función quemalmacena los datos en un diccionario que luego se agrega a la lista reservas con los datos correspondientes, verifica si el tour ingresado esta entre los tours disponibles.
def listarReservas(reservas):
    for reserva in reservas:
        print(reserva)
#Imprime las reservas ingresadas separados por linea
def imprimirDestino(reservas,tour):
    for i in reservas:
        if i["Tour"] == tour:
            with open(f"{tour}.txt", 'a') as archivo:
                archivo.write(str(i))
                archivo.write("\n")
#Recorre la lista reservas, verifica si la reserva tiene el mismo nombre que necesitan filtrar y lo escribe todo en un archivo txt
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
#Pide los datos al usuario
    if opcion == 2:
        listarReservas(reservas)
    if opcion == 3:
        tour = input("Ingrese el destino del tour: ")
        imprimirDestino(reservas,tour)
    if opcion == 4:
        break
