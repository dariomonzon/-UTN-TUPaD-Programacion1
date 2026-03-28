# TP integrador – Repetitivas- Condicionales y Secuenciales.

# Ejercicio 1— “Caja del Kiosco”

total_sin_descuento = 0
total_con_descuento = 0
precio_final = 0

cantidad_str = input("Ingrese la cantidad de productos: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) == 0:
    print("Error: Ingrese una cantidad correcta")
    cantidad_str = input("Ingrese la cantidad de productos: ").strip()

cantidad_int = int(cantidad_str)

for i in range(1,cantidad_int+1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error: El precio debe ser positivo")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio_int = int(precio_str)

    descuento = input ("Posee Descuento (S/N):").strip().lower()
    while descuento != "s" and descuento != "n":
        print("Error: Ingrese S para Si o N para No")
        descuento = input ("Posee Descuento (S/N):").strip().lower()

    total_sin_descuento += precio_int

    if descuento == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_int

print(f"""
      
Total sin descuentos: {total_sin_descuento:.2f}
Total con descuentos: {total_con_descuento:.2f}
Ahorro: {ahorro:.2f}
Precio Promedio por producto: {promedio:.2f}
""")


# Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 1

while intentos < 4:
    usuario_ingresado = input(f"Intento {intentos}/3 - Usuario: ").strip()
    claveo_ingresada = input("Ingrese clave: ").strip()
    intentos +=1
    if usuario_ingresado == usuario_correcto and claveo_ingresada == clave_correcta:
        intentos = 4
        while True:
            print("""
            Ingrese una opcion:
            1. Ver estado de inscripción (mostrar “Inscripto”)
            2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
            3. Mostrar mensaje motivacional (1 frase)
            4. Salir        
            """)
            opcion = input()
            if not opcion.isdigit():
                print ("Error: ingrese un número válido.")
                continue
            
            opcion = int(opcion)
            if opcion<1 or opcion>4:
                print ("Error: opción fuera de rango.")
                continue
            
            match opcion:
                case 1:
                    print("Inscripto")
                case 2:
                    nueva_clave = input("Ingrese nueva clave de 6 numeros: ").strip()
                    confirmacion_clave = input("Ingrese confirmacion de nueva clave: ").strip()
                    if not nueva_clave.isdigit() or len(nueva_clave) != 6:
                        print ("Clave rechazada")
                    elif nueva_clave != confirmacion_clave: 
                        print ("Las contraseñas no coinciden. Clave rechazada.")
                    else:   
                        print ("Clave reemplazada existosamente")
                        clave_correcta = nueva_clave
                case 3:
                    print ("""Cada ejercicio que resuelves es un ladrillo más en el puente hacia tus sueños; sigue construyendo, aunque el camino parezca largo""")
                case 4: 
                    break
    elif intentos == 4:                
        print(f"Cuenta bloqueada")

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""
paciente = ""
turno = ""

nombre_operador = input("Ingrese su nombre: ").strip()
while not nombre_operador.isalpha():
    print("Ingrese solo letras")
    nombre_operador = input("Ingrese su nombre: ").strip()

while True:
    
    print("""Elija Una Opcion:
        1. Reservar turno
        2. Cancelar turno (por nombre)
        3. Ver agenda del día
        4. Ver resumen general
        5. Cerrar sistema 
        """ )
    
    opcion = input()

    if not opcion.isdigit():
        print("Solo se permiten numeros")
        continue
    
    opcion = int(opcion)
    if opcion < 1 or opcion > 5:
        print("Fuera de rango de opciones")
        continue

    match opcion:
        case 1:
            turno = input("Ingrese el dia del turno: 1=Lunes, 2=Martes: ")
            while not turno.isdigit() and int(turno) != 1 and int(turno) != 2:
                print ("Opcion invalida")
                turno = input("Ingrese el dia del turno: 1=Lunes, 2=Martes: ")
            
            turno = int(turno)
                                             
            paciente = input("Ingrese el nombre del paciente: ").strip()
            while not paciente.isalpha():
                print("Solo letras")
                paciente = input("Ingrese el nombre del paciente: ")
            
            if turno == 1:
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print ("El paciente ya posee un turno para el día lunes")
                else:
                    if lunes1 == "" :
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente
                    else:
                        print ("No hay turnos disponibles para el dia Lunes")
                
            if turno == 2:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print ("El paciente ya posee un turno para el día lunes")
                else:
                    if martes1 == "" :
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente
                    else:
                        print ("No hay turnos disponibles para el dia Lunes")
                
        case 2:
            turno = input("Ingrese el dia del turno: 1=Lunes, 2=Martes: ")
            while not turno.isdigit() and int(turno) != 1 and int(turno) != 2:
                print ("Opcion invalida")
                turno = input("Ingrese el dia del turno: 1=Lunes, 2=Martes: ")
            
            turno = int(turno)

            paciente = input("Ingrese el nombre del paciente: ").strip()
            while not paciente.isalpha():
                print("Solo letras")
                paciente = input("Ingrese el nombre del paciente: ")
            if turno == 1:
                    if lunes1 == paciente :
                        lunes1 = ""
                    elif lunes2 == paciente:
                        lunes2 = ""
                    elif lunes3 == paciente:
                        lunes3 = ""
                    elif lunes4 == paciente:
                        lunes4 = ""
                    else:
                        print ("No hay turnos disponibles para el dia Lunes")
            
            if turno == 2:
                    if martes1 == paciente :
                        martes1 = ""
                    elif martes2 == paciente:
                        martes2 = ""
                    elif martes3 == paciente:
                        martes3 = ""
                    
        case 3:
            print(f"Turno 1 - Dia Lunes: {"Libre" if lunes1 == "" else lunes1}")
            print(f"Turno 2 - Dia Lunes: {"Libre" if lunes2 == "" else lunes2}")
            print(f"Turno 3 - Dia Lunes: {"Libre" if lunes3 == "" else lunes3}")    
            print(f"Turno 4 - Dia Lunes: {"Libre" if lunes4 == "" else lunes4}")
            print("---------------------------------------")
            print(f"Turno 1 - Dia Martes: {"Libre" if martes1 == "" else martes1}")
            print(f"Turno 2 - Dia Martes: {"Libre" if martes2 == "" else martes2}")
            print(f"Turno 3 - Dia Martes: {"Libre" if martes3 == "" else martes3}")    
        
        case 4:
            Turnos_Lunes_Libre = 0
            Turnos_Lunes_Ocupado = 0
            Turnos_Martes_Libre = 0
            Turnos_Martes_Ocupado = 0
            if lunes1 == "":
                Turnos_Lunes_Libre+=1 
            else: 
                Turnos_Lunes_Ocupado+=1
            if lunes2 == "":
                Turnos_Lunes_Libre+=1 
            else: 
                Turnos_Lunes_Ocupado+=1
            if lunes3 == "":
                Turnos_Lunes_Libre+=1 
            else: 
                Turnos_Lunes_Ocupado+=1
            if lunes4 == "":
                Turnos_Lunes_Libre+=1 
            else: 
                Turnos_Lunes_Ocupado+=1
            if martes1 == "":
                Turnos_Martes_Libre+=1 
            else: 
                Turnos_Martes_Ocupado+=1
            if martes2 == "":
                Turnos_Martes_Libre+=1 
            else: 
                Turnos_Martes_Ocupado+=1
            if martes3 == "":
                Turnos_Martes_Libre+=1 
            else: 
                Turnos_Martes_Ocupado+=1
            print(f"Para el dia Lunes hay {Turnos_Lunes_Ocupado} turnos asigandos y {Turnos_Lunes_Libre} turnos libres")
            print(f"Para el dia Martes hay {Turnos_Martes_Ocupado} turnos asigandos y {Turnos_Martes_Libre} turnos libres")
            if Turnos_Lunes_Ocupado == 0 and Turnos_Martes_Ocupado == 0:
                print("En ambos dias no hay turnos asignados")
            if Turnos_Lunes_Ocupado > Turnos_Martes_Ocupado:
                print("El día Lunes hay mas turnos que el día Martes")
            elif Turnos_Lunes_Ocupado < Turnos_Martes_Ocupado:
                print("El día Martes hay mas turnos que el día Lunes")
            else:
                print("En ambos dias hay la misma cantidad de turnos")
        case 5:
            break
            
# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
regla_anti_spam = 0
bloqueo = False
num = ""
energia_maxima = 100

nombre_agente = input("Ingrese el nombre del agente: ").strip()
while not nombre_agente.isalpha():
    print("Ingrese solo letras")
    nombre_agente = input("Ingrese el nombre del agente: ").strip()

if alarma and tiempo<=3 and cerraduras_abiertas < 3:
    bloqueo = True
    print("Bloqueo por alarma")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    print(f" Estado: Energia: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}")
    print("""
          Ingrese una opcion:
          1. Forzar cerradura (costo: -20 energía, -2 tiempo)
          2. Hackear panel (costo: -10 energía, -3 tiempo)
          3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energia extra)
          """)

    opcion = input()

    while not opcion.isdigit() and int(opcion)<0 and int(opcion)>3:
        print("Ingrese una opcion correcta")
        
    opcion = int(opcion)

    

    match opcion:
        case 1:
            energia-= 20
            tiempo -=2
            if regla_anti_spam == 2:
                bloqueo = True
                print("Alarma Activada - Cerrado automatico")
                
            if energia < 40:
                print("Hay riesgo de alarma")
                num = input("Ingrese un numero entre 1 y el 3: ")

                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    print("Ingrese una opcion correcta")
                    num = input("Ingrese un numero entre 1 y el 3: ")
        
                num = int(num)
                if num == 3:
                     alarma = True
                else:
                    cerraduras_abiertas+=1
            else:
                cerraduras_abiertas+=1        
            
            regla_anti_spam+=1
        case 2:
            energia-= 10
            tiempo -=3
            regla_anti_spam = 0
            for i in range(4):
                codigo_parcial+= "A"
            if len(codigo_parcial)>= 8:
                cerraduras_abiertas+=1
        case 3:
            energia+= 15
            if energia > energia_maxima:
                energia = energia_maxima
            tiempo -=3
            regla_anti_spam = 0
            if alarma:
                energia-=10
        
        case 4:
              break
if cerraduras_abiertas == 3:
    print("VICTORIA")
    print(f" Estado: Energia: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}")
if (tiempo <= 0 or energia <=0) and cerraduras_abiertas < 3:
    print("DERROTA")
    print(f" Estado: Energia: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}")
if bloqueo:
    print("DERROTA (bloqueo)")
    print(f" Estado: Energia: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}")
         
# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

nombre_gladiador= input("Ingrese el nombre del gladiador: ").strip().upper() 
#strip permite quitar los espacios del texto ingresado
while not nombre_gladiador.isalpha(): 
    #isalpha solo permite letras
    print("Error. Solo se permiten letras")
    nombre_gladiador= input("Ingrese el nombre del gladiador: ").strip().upper()

vida_del_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_base_gladiador = 15
danio_base_enemigo = 12
turno_gladiador = True

while vida_enemigo>0 and vida_del_gladiador>0:
    if turno_gladiador:
        print(f"El Gladiador {nombre_gladiador} tiene {vida_del_gladiador} puntos de vida")
        print(f"El enemigo tiene {vida_enemigo} puntos de vida")
        print(f"Te quedan {pociones_vida} pocion es de vida")
        while True:
            print("""
                  1.Ataque Pesado
                  2. Rafaga Veloz
                  3. Curar
                  """)
            opcion=input("Elegi una opcion de accion: ")
            match opcion:
                case "1":
                    if vida_enemigo< 20:
                        vida_enemigo -= danio_base_gladiador*1.5
                        print(f"Atacaste al enemigo por {danio_base_gladiador*1.5} puntos")
                    else:
                        vida_enemigo -= danio_base_gladiador
                        print(f"Atacaste al enemigo por {danio_base_gladiador} puntos")
                        break
                case "2":
                    for i in range(3):
                        vida_enemigo-=1
                        print(f"Golpe conectado por 5 de daño")
                    break
                case "3":
                    if pociones_vida>0:
                        vida_del_gladiador+=30
                        pociones_vida-=1
                    else:
                        print(f"¡No quedan pociones!")
                        print("Perdiste el turno")
                    break
                case _:
                    print("El valor ingresado es invalido, intente de nuevo")
        turno_gladiador = False
    else:
        vida_del_gladiador -= danio_base_enemigo
        print(f"¡El enemigo te atacó por 12 puntos de daño!")
        turno_gladiador = True #sirve para cambiar el turno al gladiador

if vida_del_gladiador>0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla")
else:
    print(f"¡DERROTA! {nombre_gladiador} Has caido en batalla")












