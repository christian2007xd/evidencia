import csv
import datetime
import sys
import sqlite3
from sqlite3 import Error


def parse_fecha(fecha_str):
    """Convierte un string de fecha a datetime.date, soportando DD/MM/YYYY o YYYY-MM-DD"""
    try:
        if "/" in fecha_str:
            return datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
        else:
            return datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def main():
    print("Iniciando el sistema de reservaciones...")
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            # Tablas base
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cliente (
                    clave_c INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL
                );
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sala (
                    clave_s INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    cupo INTEGER NOT NULL
                );
            """)
            cursor.execute("CREATE TABLE IF NOT EXISTS turno (clave_t INTEGER PRIMARY KEY, nombre TEXT NOT NULL);")
            
            # Insertar turnos iniciales
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(1,'Matutino')")
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(2,'Vespertino')")
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(3,'Nocturno')")
            conn.commit()
            
            # Tabla reservas con timestamps
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservas (
                    clave_r INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_evento TEXT NOT NULL,
                    fecha TEXT,
                    turno INTEGER NOT NULL,
                    cliente INTEGER NOT NULL,
                    sala INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP,
                    FOREIGN KEY(cliente) REFERENCES cliente(clave_c),
                    FOREIGN KEY(sala) REFERENCES sala(clave_s),
                    FOREIGN KEY(turno) REFERENCES turno(clave_t)
                );
            """)
            conn.commit()
            
            # Verificar registros iniciales
            cursor.execute("SELECT COUNT(*) FROM cliente")
            clientes_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM sala")
            salas_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM reservas")
            reservas_count = cursor.fetchone()[0]
            if clientes_count == 0 and salas_count == 0 and reservas_count == 0:
                print("No se encontraron registros previos. Iniciando con estado inicial vacío.\n")
                
    except Error as e:
        print(e)
        return

    TURNOS = ["Matutino", "Vespertino", "Nocturno"]

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar reservación")
        print("2. Editar nombre del evento")
        print("3. Consultar reservaciones")
        print("4. Registrar cliente")
        print("5. Registrar sala")
        print("6. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            # --- Registrar reservación ---
            while True:
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                    Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                if not Clientes:
                    print("No hay clientes registrados.")
                    break

                while True:
                    try:
                        clientes_ordenados = sorted(Clientes.items(), key=lambda x: (x[1][1], x[1][0]))
                        print("\n--- Clientes Registrados ---")
                        print(f"{'Clave':<10}{'Apellido':<20}{'Nombre':<15}")
                        for clave, (nombre, apellido) in clientes_ordenados:
                            print(f"{clave:<10}{apellido:<20}{nombre:<15}")
                        clave_cliente_input = input("Ingrese la clave del cliente o escriba 'CANCELAR' para salir: ").strip()
                        if clave_cliente_input.upper() == "CANCELAR":
                            break
                        if clave_cliente_input not in Clientes:
                            print("La clave ingresada no existe.")
                            continue
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                if clave_cliente_input.upper() == "CANCELAR":
                    break

                # Fecha de reservación
                while True:
                    fecha_reservacion = input("Ingrese la fecha de la reservación (DD/MM/YYYY) o 'CANCELAR' para salir: ").strip()
                    if fecha_reservacion.upper() == "CANCELAR":
                        break
                    fecha_dt = parse_fecha(fecha_reservacion)
                    if fecha_dt is None:
                        print("Formato de fecha inválido. Intente de nuevo.")
                        continue
                    if (fecha_dt - datetime.date.today()).days < 2:
                        print("La reservación debe ser al menos con 2 días de anticipación.")
                        continue
                    # Validar domingo
                    if fecha_dt.weekday() == 6:  # domingo
                        lunes_sig = fecha_dt + datetime.timedelta(days=1)
                        print(f"La fecha cae domingo. Se propone como alternativa el lunes siguiente: {lunes_sig.strftime('%d/%m/%Y')}")
                        aceptar = input("¿Desea aceptar esta fecha? (S/N): ").strip().upper()
                        if aceptar == "S":
                            fecha_dt = lunes_sig
                        else:
                            continue
                    break
                if fecha_reservacion.upper() == "CANCELAR":
                    break

                # Selección de sala
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_s, nombre, cupo FROM sala;")
                    Salas = {str(s[0]): (s[1], s[2]) for s in cursor.fetchall()}
                if not Salas:
                    print("No hay salas registradas.")
                    break
                print("\n--- Salas Disponibles ---")
                print(f"{'Clave':<10}{'Nombre':<30}{'Cupo':<8}")
                for clave, (nombre, cupo) in Salas.items():
                    print(f"{clave:<10}{nombre:<30}{cupo:<8}")
                while True:
                    clave_sala_input = input("Ingrese la clave de la sala o 'CANCELAR' para salir: ").strip()
                    if clave_sala_input.upper() == "CANCELAR":
                        break
                    if clave_sala_input not in Salas:
                        print("La clave ingresada no existe.")
                        continue
                    break
                if clave_sala_input.upper() == "CANCELAR":
                    break

                # Turno
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas;")
                    Reservaciones = {str(r[0]): (str(r[1]), str(r[2]), r[5], r[3], r[4]) for r in cursor.fetchall()}
                
                turnos_ocupados = [r[3] for r in Reservaciones.values() if r[1] == clave_sala_input and parse_fecha(r[4]) == fecha_dt]
                
                if len(turnos_ocupados) >= 3:
                    print("Esa sala ya tiene los 3 turnos ocupados para esa fecha.")
                    break
                while True:
                    turno = input("Ingrese el turno (Matutino, Vespertino, Nocturno) o 'CANCELAR' para salir: ").strip().capitalize()
                    if turno.upper() == "CANCELAR":
                        break
                    if turno not in TURNOS:
                        print("Turno inválido. Intente de nuevo.")
                        continue
                    if TURNOS.index(turno)+1 in turnos_ocupados:
                        print(f"La sala ya está reservada en el turno {turno} para esa fecha.")
                        continue
                    break
                if turno.upper() == "CANCELAR":
                    break
                
                while True:
                    nombre_evento = input("Ingrese el nombre del evento o 'CANCELAR' para salir: ").strip()
                    if nombre_evento.upper() == "CANCELAR":
                        break
                    if not nombre_evento or nombre_evento.isspace():
                        print("El nombre del evento no puede estar vacío ni contener solo espacios.")
                        continue
                    break
                if nombre_evento.upper() == "CANCELAR":
                    break
                
                evento_duplicado = any(r[1] == clave_sala_input and parse_fecha(r[4]) == fecha_dt and r[3] == TURNOS.index(turno)+1 and r[2].lower() == nombre_evento.lower() for r in Reservaciones.values())
                if evento_duplicado:
                    print("Ya existe un evento con ese nombre en la misma sala, fecha y turno.")
                    break
                
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO reservas (nombre_evento, fecha, turno, cliente, sala) VALUES (?, ?, ?, ?, ?);",
                        (nombre_evento, fecha_dt.strftime("%Y-%m-%d"), TURNOS.index(turno)+1, int(clave_cliente_input), int(clave_sala_input))
                    )
                    conn.commit()
                print("Reservación registrada con éxito.")
                break

        elif opcion == "2":
            # --- Editar nombre del evento ---
            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas;")
                Reservaciones = {str(r[0]): (str(r[1]), str(r[2]), r[5], r[3], r[4]) for r in cursor.fetchall()}
                
            if not Reservaciones:
                print("No hay reservaciones registradas.")
                continue
            
            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                cursor.execute("SELECT clave_s, nombre FROM sala;")
                Salas = {str(s[0]): s[1] for s in cursor.fetchall()}   
                
            try:
                fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ").strip()
                fecha_fin = input("Ingrese la fecha de fin (DD/MM/YYYY): ").strip()
                f_inicio = parse_fecha(fecha_inicio)
                f_fin = parse_fecha(fecha_fin)
                if f_inicio is None or f_fin is None:
                    print("Formato de fecha inválido.")
                    continue
                if f_fin < f_inicio:
                    print("La fecha de fin no puede ser anterior a la de inicio.")
                    continue
            except ValueError:
                print("Formato de fecha inválido.")
                continue
            
            print(f"\n--- Reservaciones entre {fecha_inicio} y {fecha_fin} ---")
            print(f"{'Folio':<8}{'Fecha':<12}{'Turno':<20}{'Evento':<25}{'Sala':<25}{'Cliente':<25}")
            print("-" * 105)
            
            for folio, (cli, sala, evento, turno_num, fecha_str) in Reservaciones.items():
                fecha = parse_fecha(fecha_str)
                if fecha is None:
                    continue
                if f_inicio <= fecha <= f_fin:
                    cliente_nombre = f"{Clientes[cli][1]} {Clientes[cli][0]}" if cli in Clientes else "Desconocido"
                    sala_nombre = Salas[sala] if sala in Salas else "Desconocida"
                    turno_nombre = TURNOS[int(turno_num)-1]
                    print(f"{folio:<8}{fecha.strftime('%d/%m/%Y'):<12}{turno_nombre:<20}{evento:<25}{sala_nombre:<25}{cliente_nombre:<25}")
                    
            folio_a_editar = input("Ingrese el folio a editar: ").strip()
            if folio_a_editar not in Reservaciones:
                print("Folio no encontrado.")
                continue
            
            while True:
                nuevo_nombre = input("Ingrese el nuevo nombre del evento: ").strip()
                if not nuevo_nombre or nuevo_nombre.isspace():
                    print("El nombre no puede estar vacío ni contener solo espacios.")
                    continue
                break
            
            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE reservas SET nombre_evento = ?, updated_at = CURRENT_TIMESTAMP WHERE clave_r = ?;",
                    (nuevo_nombre, int(folio_a_editar))
                )
                conn.commit()
            print("Evento actualizado correctamente.")

        elif opcion == "3":
            # --- Consultar reservaciones ---
            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas;")
                Reservaciones = {str(r[0]): (str(r[1]), str(r[2]), r[5], r[3], r[4]) for r in cursor.fetchall()}
                
            if not Reservaciones:
                print("No hay reservaciones registradas.")
                continue
            
            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                cursor.execute("SELECT clave_s, nombre FROM sala;")
                Salas = {str(s[0]): s[1] for s in cursor.fetchall()}
            
            fecha_consulta = input("Ingrese la fecha a consultar (DD/MM/YYYY) o ENTER para fecha actual: ").strip()
            if not fecha_consulta:
                fecha_obj = datetime.date.today()
            else:
                fecha_obj = parse_fecha(fecha_consulta)
                if fecha_obj is None:
                    print("Formato de fecha inválido.")
                    continue
            fecha_iso = fecha_obj.strftime("%Y-%m-%d")
                
            print(f"\n--- Reporte de Reservaciones ({fecha_obj.strftime('%d/%m/%Y')}) ---")
            print(f"{'Folio':<8}{'Turno':<20}{'Cliente':<30}{'Sala':<25}{'Evento':<20}")
            print("-" * 90)
            
            filas_para_csv = []
            for folio, (cli, sala, evento, turno_num, fecha_str) in Reservaciones.items():
                fecha = parse_fecha(fecha_str)
                if fecha is None:
                    continue
                if fecha.strftime("%Y-%m-%d") == fecha_iso:
                    cliente_nombre = f"{Clientes[cli][1]} {Clientes[cli][0]}" if cli in Clientes else "Desconocido"
                    sala_nombre = Salas[sala] if sala in Salas else "Desconocida"
                    turno_nombre = TURNOS[int(turno_num)-1]
                    print(f"{folio:<8}{turno_nombre:<20}{cliente_nombre:<30}{sala_nombre:<25}{evento:<20}")
                    filas_para_csv.append({
                        "Folio": folio,
                        "Fecha": fecha_str,
                        "Turno": turno_nombre,
                        "Cliente": cliente_nombre,
                        "Sala": sala_nombre,
                        "Evento": evento
                    })
                    
            if not filas_para_csv:
                print("*" * 28)
                print("**No hay reservaciones para esta fecha.**")
                print("*" * 28)
                continue
            
            resp = input("¿Desea exportar este reporte a CSV? (S/N): ").strip().upper()
            if resp == "S":
                nombre_archivo = f"reservaciones_{fecha_obj.strftime('%Y%m%d')}.csv"
                
                try:
                    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as csvfile:
                        fieldnames = ["Folio", "Fecha", "Turno", "Cliente", "Sala", "Evento"]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        for fila in filas_para_csv:
                            writer.writerow(fila)
                    print(f"Reporte exportado correctamente a '{nombre_archivo}'.")
                except Exception as e:
                    print(f"Ocurrió un error al exportar a CSV: {e}")

        elif opcion == "4":
                while True:
                    
                    try:
                        nombre = input("Nombre del cliente: ").strip()
                        if not nombre:
                            raise Exception(" El nombre no pueden estar vacío.")
                        if not nombre.replace(" ", "").isalpha():
                            raise Exception(" El nombre solo debe contener letras.")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                while True:
                    try:
                        apellido = input("Apellido del cliente: ").strip()
                        if not apellido:
                            raise Exception(" El apellido no puede estar vacío.")
                        if not apellido.replace(" ", "").isalpha():
                            raise Exception(" El apellido solo debe contener letras.")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                    
                try:
                    with sqlite3.connect("reservaciones.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO cliente (nombre, apellido) VALUES (?,?)",(nombre, apellido) )
                        print("Registro agregado exitosamente")
                except Error as e:
                    print (e)
                except Exception:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                    

        elif opcion == "5":
                while True: 
                    
                    try:
                        nombre = input("Nombre de la sala: ").strip()
                        if not nombre:
                            raise Exception("El nombre de la sala no puede estar vacío.")
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                while True:
                    try:
                        cupo = float(input("Cupo de la sala: "))
                        if cupo <= 0:
                            raise Exception("El cupo debe ser un número positivo.")
                        if not cupo.is_integer():
                            raise Exception("El cupo debe ser un número entero.")
                        cupo = int(cupo)
                        break
                    except ValueError:
                        print("El cupo solo puede contener números, sin letras ni símbolos.")
                    except Exception as e:
                        print(f"Error: {e} ")
                    
                try:
                    with sqlite3.connect("reservaciones.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO sala(nombre, cupo) VALUES (?, ?);", (nombre, cupo))
                        print("Registro agregado exitosamente")
                except Error as e:
                    print (e)
                except Exception:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()