import time
import re
import datetime
import holidays
import json
import random


dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sábado", "domingo"]
dias_semana_normal = ["lunes", "martes", "miercoles", "jueves", "viernes"]
dias_semana_finde = ["sabado", "domingo"]


def main():
    pantalla_inicio()
    print()
    pantalla_luego_iniciar_sesion()


def obtener_tipo_de_usuario():
    while (True):
        print("¿Qué usuario eres?")
        print("Opciones:")
        print("1. Estudiante o público general")
        print("2. Empleado o proovedor")
        print("3. Asistente a eventos")
        print("4. Personal directivo")
        print("0. Cancelar")
        print("Seleccione una opción: ", end="")
        x = input()
        if (x == "1"):
            x = "estudiante_o_publico_general"
            return x
        elif (x == "2"):
            while (True):
                print()
                print("    ¿Eres proovedor de una cafetería?")
                print("    Opciones:")
                print("    1. Sí")
                print("    2. No")
                print("    0. Cancelar")
                print("    Seleccione una opción: ", end="")
                y = input()
                if (y == "1"):
                    x = "proovedor"
                    x = x + "_cafeteria"
                    return x
                elif (y == "2"):
                    x = "empleado_o_proovedor"
                    return x
                elif (y == "0"):
                    x = None
                    yendo_al_menu()
                else:
                    print("!!! Opción inválida. Intente de nuevo. !!!")
                    print()
                    continue
        elif (x == "3"):
            x = "asistente_a_eventos"
            return x
        elif (x == "4"):
            x = "personal_directivo"
            return x
        elif (x == "0"):
            x = None
            yendo_al_menu()
        else:
            print("!!!Opción inválida. Intente de nuevo. !!!")
            print()
            continue


def obtener_movilidad_fisica():
    while (True):
        print("¿Usted está o se encuentra con una persona en condición de movilidad reducida?")
        print("Opciones:")
        print("1. Sí")
        print("2. No")
        print("0. Cancelar")
        print("Seleccione una opción: ", end="")
        x = str(input())
        if (x == "1"):
            x = "discapacitado"
            return x
        elif (x == "2"):
            x = "sano"
            return x
        elif (x == "0"):
            x = None
            yendo_al_menu()
        else:
            print("!!! Opción inválida. Intente de nuevo. !!!")
            print()
            continue


def obtener_tipo_de_carro():
    while (True):
        print("¿Qué tipo de carro tienes?")
        print("1. Carro normal")
        print("2. Carro eléctrico")
        print("3. Carro de baja emisión")
        print("0. Cancelar")
        print("Seleccione una opción: ", end="")
        x = str(input())
        if (x == "1"):
            x = "carro_normal"
            return x
        elif (x == "2"):
            x = "carro_electrico"
            return x
        elif (x == "3"):
            x = "carro_de_baja_emision"
            return x
        elif (x == "0"):
            x = None
            yendo_al_menu()
        else:
            print("!!! Opción inválida. Intente de nuevo. !!!")
            print()
            continue


def zonas_disponibles_parqueo():
    # Realmente aquí iría lo que se recibe del sensor, pero quedamos en suponer lo que se recibía
    dia = obtener_dia_de_la_semana()
    festivo = obtener_si_es_festivo()
    hora = obtener_hora_actual()
    hora = convertir_hora_a_numero(hora)
    tipo_usuario = obtener_tipo_usuario_del_json(correo)

"""    # PARQUEADERO VEHICULAR DE EMPLEADOS
        # PORTERIA VEHICULAR AVENIDA REGIONAL / EDIFICIO ARGOS
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5 and tipo_usuario == "empleado_o_proovedor"):
                # codigo
            elif (6 <= hora <= 22.5):
                # codigo
        elif (dia in dias_semana_finde):
            if (6 <= hora <= 18):
                # codigo
    if (festivo == "si"):
        if (dia in dias_semana):
            if (6 <= hora <= 6 and tipo_usuario == "empleado_o_proovedor"):
                # codigo

        # PORTERIA VEHICULAR DE EMPLEADOS AVENIDAS LAS VEGAS
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5 and tipo_usuario == "empleado_o_proovedor"):
                # codigo
            elif (6 <= hora <= 22.5):
                # codigo
        elif (dia == "sabado"):
            if (6 <= hora <= 18):
                # codigo

    # PARQUEADERO VEHIICULAR NORTE
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5):
                # codigo
        elif (dia == "sabado"):
            if (6 <= hora <= 18):
                # codigo

    # PARQUEADERO VEHICULAR SUR
        # PORTERIA VEHICULAR LA AVENIDA LAS VEGAS SECTOR LA AGUACATALA
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5):
                # codigo
        elif (dia == "sabado"):
            if (6 <= hora <= 18):
                # codigo
    elif (festivo == "si"):
        if (dia in dias_semana_normal):
            if (6 <= hora <= 18):
                # codigo

        # PORTERIA VEHICULAR EDIFICIO DE INGENIERIAS
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5):
                # codigo
        elif (dia == "sabado"):
            if (6 <= hora <= 18):
                # codigo

    # PARQUEADERO VEHICULAR PARQUE LOS GUAYABOS
    if (festivo == "no"):
        if (dia in dias_semana_normal):
            if (5 <= hora <= 22.5):
                # codigo
        elif (dia == "sabado"):
            if (6 <= hora <= 18):
                # codigo """


def recomendaciones_disponibles(usuario, movilidad_fisica, carro, system_randomizer):
    # Aquí se debería usar información del sensor,  pero quedamos en suponer lo que se recibía
    return None


def recomendaciones_ocupadas(usuario, movilidad_fisica, carro, system_randomizer):
    # Aquí se debería usar información del sensor,  pero quedamos en suponer lo que se recibía
    return None

def obtener_dia_de_la_semana():
    hoy = datetime.datetime.now()
    dia_semana_numero = hoy.weekday()
    dia_semana_nombre = dias_semana[dia_semana_numero]
    return dia_semana_nombre


def obtener_si_es_festivo():
    hoy = datetime.date.today()
    co_holidays = holidays.Colombia()
    if hoy in co_holidays:
        return "si"
    else:
        return "no"


def pantalla_inicio():
    while True:
        print("Opciones:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("0. Salir")
        print("dev. Opcion de desarrollador, ver que se llenan los parqueaderos")
        x = input("Seleccione una opción: ")
        if x == "1":
            print()
            registrar_usuario()
        elif x == "2":
            print()
            sesion = iniciar_sesion()
            if sesion == "sesion_iniciada":
                break
        elif x == "0":
            exit()
        elif x == "dev":
            developer_base()
        else:
            print("!!! Opción inválida. Intente de nuevo. !!!")
            print()


def pantalla_luego_iniciar_sesion():
    '''zonas_disponibles_parqueo(usuario, movilidad_fisica, carro, llenado_randomizer)
    recomendaciones_disponibles(usuario, movilidad_fisica, carro, llenado_randomizer)
    recomendaciones_ocupadas(usuario, movilidad_fisica, carro, llenado_randomizer)'''
    print("¿Qué quieres hacer?")
    print("Opciones:")
    print("1. Ver Zonas disponibles del parqueadero")
    print("2. Ver Recomendaciones para donde parquearte libres")
    print("3. Ver Recomendaciones ocupadas")
    print("0. Cerrar sesión")
    print("Seleccione una opción: ", end="")
    x = input()
    if (x == "1"):
        zonas_disponibles_parqueo()
    elif (x == "0"):
        print()
        print("Sesión cerrada exitosamente.")
        print()
        main()


def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9._]+@eafit\.edu\.co$'
    return re.match(patron, correo) is not None


def registrar_usuario():
    print("Por favor responda las preguntas a continuación....")
    print()
    tipo_usuario = obtener_tipo_de_usuario()
    print()
    movilidad_fisica = obtener_movilidad_fisica()
    print()
    tipo_carro = obtener_tipo_de_carro()
    print()
    print("!Casi todo listo!")
    while True:
        correo = input("Ingrese su correo electrónico usando el formato [usuario insitucional]@eafit.edu.co): ")
        if es_correo_valido(correo):
            break
        else:
            print("!!! Formato de correo no válido. Intente de nuevo. !!!")
            print()
    contrasena = input("Crear contraseña: ")
    usuario_data = {
        "correo": correo,
        "usuario": correo.split("@")[0],
        "contrasena": contrasena,
        "tipo_usuario": tipo_usuario,
        "movilidad_fisica": movilidad_fisica,
        "tipo_carro": tipo_carro
    }
    with open("usuarios.json", "a") as archivo:
        json.dump(usuario_data, archivo)
        archivo.write('\n')
    print("Registro exitoso")
    print()


def iniciar_sesion():
    while (True):
        global correo
        correo = input("Ingrese su correo electrónico: ")
        if es_correo_valido(correo) == False:
            print("!!! Formato de correo no válido. Intente de nuevo. !!!")
            print()
        else:
            break
    contrasena = input("Ingrese su contraseña: ")
    with open("usuarios.json", "r") as archivo:
        for linea in archivo:
            usuario_data = json.loads(linea.strip())
            if usuario_data["correo"] == correo and usuario_data["contrasena"] == contrasena:
                print("Inicio de sesión exitoso.")
                print()
                x = "sesion_iniciada"
                return x
    print("!!! Correo o contraseña incorrectos. Intente de nuevo. !!!")
    print()
    return "-1"


def obtener_hora_actual():
    while (True):
        ahora = datetime.datetime.now()
        print(ahora.strftime("%H:%M:%S"))
        time.sleep(10)


def yendo_al_menu():
    print()
    print("/// YENDO AL ///")
    print("///   MENU ///")
    print()
    main()


def convertir_hora_a_numero(hora_str):
    partes = hora_str.split(":")
    hora = int(partes[0])
    minuto = int(partes[1])
    return hora + minuto / 60


def obtener_tipo_usuario_del_json(correo):
    with open("usuarios.json", "r") as archivo:
        usuarios = json.load(archivo)
        for usuario in usuarios:
            if usuario["correo"] == correo:
                return usuario["tipo_usuario"]


def parking_spot_number():
    return i + 1


'''def randint_nottaken():
    our_rangeset = set([x for x in range(1, n + 1)])
    if i > 0:
        random_takenuserid = random.choice(list(our_rangeset))
        our_rangeset.remove(random_takenuserid)
        if decision == True:
            return random_takenuserid
        else:
            return -1
    else:
        if decision == True:
            return random.choice(list(our_rangeset))
        else:
            return -1'''


def random_user():
    if (len(usernames) != 0 and decision == True):
        print(usernames)
        random_username = random.choice(usernames)
        usernames.remove(random_username)
        return random_username
    if (decision == False):
        return -1
    if (len(usernames) == 0):
        spot["status"] = False
        return -1


def save_to_json(parking_list, filename):
    with open(filename, 'a') as json_file:
        json.dump(parking_list, json_file)
        json_file.write('\n')


def obtener_hora_actual():
        ahora = datetime.datetime.now()
        return ahora.strftime("%H:%M:%S")


def developer_base():
    ticks = float(input("Actualizar la lista automáticamente cada cuántos segundos?: "))
    list_length = int(input("¿Cuál es el tamaño de la lista de estacionamiento?: "))
    '''global n
    n = int(input("Como condición asumida, ¿cuántos usuarios han sido registrados?: "))'''
    global i
    global usernames
    global spot
    global decision
    j = 1
    while True:
        decision = random.choice([True, False])
        with open("usuarios.json", 'r') as file:
            user_records = [json.loads(line) for line in file]
        usernames = [user.get("usuario") for user in user_records]
        parking_list = []
        for i in range(list_length):
            spot = {
                "parking spot": parking_spot_number(),
                "status": decision,
                "sent_by_username": random_user(),
                "hour": obtener_hora_actual()
            }
            parking_list.append(spot)
        print("Tick #" + str(j), end=" - ")
        print(parking_list, end="\n\n")
        save_to_json(parking_list, 'zonas.json')
        time.sleep(ticks)
        j += 1


main()