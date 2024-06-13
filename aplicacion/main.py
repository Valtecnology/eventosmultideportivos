
import mysql.connector

# Establecer la conexión a la base de datos y retornar el error si sucede
def conexion():
  try:
    multideportivo = mysql.connector.connect(
      host="localhost",
      user="root",
      password="esekuele24",
      database="multideportivo")
    print("Conexion exitosa")
    return multideportivo
  except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos: {}".format(error))
    return None 
conexion() 

# funciones relacionadas al CRUD
def sum_part():
  try:
    nom = input("Ingrese el nombre del nuevo participante: ")
    nombre = nom
    ape = input("Ingrese el apellido del nuevo participante: ")
    apellido = ape
    eda = input("Ingrese la edad del nuevo participante: ")
    edad = eda
    gen = input("Ingrese el sexo (hombre|mujer) del nuevo participante: ")
    genero = gen
    cone = conexion()
    cursor = cone.cursor()
    sql =  "INSERT INTO participante (id_Participante, nombre, apellido, edad, genero) VALUES (null, %s, %s, %s, %s)"
    valores = (nombre, apellido, edad, genero)
    cursor.execute(sql, valores)
    cone.commit()
    print(cursor.rowcount, " registro ingresado")
    cone.close()
  except mysql.connector.Error as error:
    print("Error de ingreso de datos: {}".format(error))  
 
def sum_dep():
  try:
    nom = input("Ingrese el nombre del nuevo deporte: ")
    nombre = nom
    des = input("Ingrese una descripcion corta del deporte añadido: ")
    descripcion = des
    cone = conexion()
    cursor = cone.cursor()
    sql =  "INSERT INTO disciplina_deportiva (id_disciplina, nombre_disciplina, descripcion) VALUES (null, %s, %s)"
    valores = (nombre, descripcion)
    cursor.execute(sql, valores)
    cone.commit()
    print(cursor.rowcount, " registro ingresado")
    cone.close()
  except mysql.connector.Error as error:
    print("Error de ingreso de datos: {}".format(error))
    
  
def sum_encu():
  try:
    fe = input("Ingrese la fecha del nuevo evento(YYYY-MM-DD): ")
    fecha = fe 
    hor = input("Ingrese la hora del evento (HH:MM:SS): ")
    hora = hor
    idd = input("Ingrese el ID del evento existente correspondiente: ")
    id = int(idd)
    cone = conexion()
    cursor = cone.cursor()
    sql = "INSERT INTO encuentro (FK_Evento_id, fecha_encuentro, hora_encuentro) VALUES (%s, %s, %s)"
    valores = (id, fecha, hora)
    cursor.execute(sql, valores)
    cone.commit()
    print(cursor.rowcount, " registro ingresado")
    cone.close()
  except mysql.connector.Error as error:
    print("Error de ingreso de datos: {}".format(error))
    
  
def sum_even():
  try:
    nom = input("Ingrese el nombre del nuevo evento: ")
    nombre = nom 
    fe1 = input("Ingrese la fecha de inicio del evento (YYYY-MM-DD): ")
    fecha1 = fe1
    fe2 = input("Ingrese la fecha de cierre del evento (YYYY-MM-DD): ")
    fecha2 = fe2 
    cone = conexion()
    cursor = cone.cursor()
    sql =  "INSERT INTO evento (id_evento, nombre_evento, fecha_inicio, fecha_cierre) VALUES (null, %s, %s, %s)"
    valores = [nombre, fecha1, fecha2]
    cursor.execute(sql, valores)
    cone.commit()
    print(cursor.rowcount, " registro ingresado")
    cone.close()
  except mysql.connector.Error as error:
    print("Error de ingreso de datos: {}".format(error))
    
  
def con_even():
  try:
    cone = conexion()
    cursor = cone.cursor()
    cursor.execute("SELECT * FROM evento")
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))
    
def con_encu_part():
  try:
    cone = conexion()
    cursor = cone.cursor()
    cursor.execute("SELECT nombre, apellido, edad, genero, id_encuentro, fecha_encuentro, hora_encuentro FROM encuentro INNER JOIN participante ON encuentro.id_encuentro = participante.id_Participante")
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))

  
def con_even_encu():
  try:
    cone = conexion()
    cursor = cone.cursor()
    cursor.execute("SELECT id_encuentro, nombre_evento, fecha_encuentro, hora_encuentro FROM evento INNER JOIN encuentro ON encuentro.id_encuentro = evento.id_evento")
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))
    
def con_age_part():
  try:
    aage1 = input("Ingrese la edad minima a listar: ")
    aage2 = input("Ingrese la edad maxima a listar: ")
    age1 = int(aage1)  
    age2 = int(aage2)
    cone = conexion()
    cursor = cone.cursor()
    sql = "SELECT * FROM participante WHERE edad BETWEEN %s AND %s"
    valores = [age1, age2]
    cursor.execute(sql, valores)
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))
    

def con_gen_dep():
  try:
    gen = input("Ingrese el genero a consultar: ")
    genero = gen  
    dep = input("Ingrese el deporte a consultar: ")
    deporte = dep  
    cone = conexion()
    cursor = cone.cursor()
    sql = "SELECT id_participante, nombre, genero, nombre_disciplina FROM participante INNER JOIN disciplina_deportiva ON disciplina_deportiva.id_disciplina = participante.id_Participante WHERE genero = %s AND nombre_disciplina = %s"
    valores = [genero, deporte]
    cursor.execute(sql,valores)
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))
  
def con_prox_even():
  try:
    nnum = input("Ingrese el número de eventos mas lejanos a listar: ")
    num = int(nnum)  # Convertir entrada a entero
    cone = conexion()
    cursor = cone.cursor()
    sql = "SELECT * FROM evento ORDER BY fecha_inicio DESC LIMIT %s"
    valores = [num]
    cursor.execute(sql,valores)
    resultados = cursor.fetchall() 
    for resultado in resultados:
        print(resultado)
    cone.commit()
    cone.close()
    return resultados
  except mysql.connector.Error as error:
    print("Error de lectura de datos: {}".format(error))
 

def menu():
    print(" --- Menu ---")
    print("1. Agregar Participantes")
    print("2. Agregar Deportes")
    print("3. Agregar Encuentros")
    print("4. Agregar Eventos")
    print("5. Consultar Eventos")
    print("6. Consultar Encuentros y sus Participantes")
    print("7. Consultar Eventos y sus Encuentros")
    print("8. Consultar Participantes por rango etario")
    print("9. Consultar Participantes por Genero y Deporte ")
    print("10. Consultar Proximos Encuentros")
    print("0. Salir")

# Lista de funciones que coinciden con las opciones del menú
funciones = [None, sum_part, sum_dep, sum_encu, sum_even, con_even, con_encu_part, con_even_encu, con_age_part, con_gen_dep, con_prox_even]

def crud(): #navegar y salir del programa
    while True:
        menu()
        try:
            index = int(input("Ingrese la opcion de menu elegida: "))
            if index == 0:
                print("Saliendo del programa...")
                break
            elif 1 <= index < len(funciones):
                funcion = funciones[index]
                if callable(funcion):
                    while True:
                        funcion()
                        again = input("Si desea volver a utilizar esta funcion, ingrese '1'. Si desea volver al menu, ingrese '0': ")
                        if again == '0':
                            break
                        elif again != '1':
                            print("Opción inválida, intentelo nuevamente.")
                else:
                    print("Hubo un error, intentelo nuevamente")
            else:
                print("La opcion seleccionada no es correcta, intentelo nuevamente")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

crud()



