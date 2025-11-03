import csv
import datetime
import sqlite3
from sqlite3 import Error

def parse_fecha(fecha_str):
    """Convierte un string de fecha a datetime.date, soportando DD/MM/YYYY o YYYY-MM-DD"""
    for fmt in ("%m/%d/%Y", "%m-%d-%Y", "%Y-%m-%d"):
        try:
            return datetime.datetime.strptime(fecha_str, fmt).date()
        except Exception:
            continue
    return None

def asegurar_columna_estado(conn):
    """Asegura la existencia de la columna "estado" en la tabla "reservas"."""
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(reservas);")
    cols = [c[1] for c in cursor.fetchall()]
    if "estado" not in cols:
        cursor.execute("ALTER TABLE reservas ADD COLUMN estado TEXT DEFAULT 'Activa';")
        conn.commit()

def main():
    print("Iniciando el sistema de reservaciones...")
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
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
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(1,'Matutino');")
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(2,'Vespertino');")
            cursor.execute("INSERT OR IGNORE INTO turno VALUES(3,'Nocturno');")
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
            asegurar_columna_estado(conn)
            cursor.execute("SELECT COUNT(*) FROM cliente;")
            clientes_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM sala;")
            salas_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM reservas;")
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
        print("4. Cancelar reservación")
        print("5. Registrar cliente")
        print("6. Registrar sala")
        print("7. Salir")
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            while True:
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                    Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                if not Clientes:
                    print("No hay clientes registrados.")
                    break

                while True:
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
                if clave_cliente_input.upper() == "CANCELAR":
                    break
                
                while True:
                    fecha_reservacion = input("Ingrese la fecha de la reservación (MM/DD/AAAA) o 'CANCELAR' para salir: ").strip()
                    if fecha_reservacion.upper() == "CANCELAR":
                        break
                    fecha_dt = parse_fecha(fecha_reservacion)
                    if fecha_dt is None:
                        print("Formato de fecha inválido. Intente de nuevo.")
                        continue
                    if (fecha_dt - datetime.date.today()).days < 2:
                        print("La reservación debe ser al menos con 2 días de anticipación.")
                        continue
                    if fecha_dt.weekday() == 6:
                        lunes_sig = fecha_dt + datetime.timedelta(days=1)
                        print(f"La fecha cae domingo. Se propone como alternativa el lunes siguiente: {lunes_sig.strftime('%m/%d/%Y')}")
                        aceptar = input("¿Desea aceptar esta fecha? (S/N): ").strip().upper()
                        if aceptar == "S":
                            fecha_dt = lunes_sig
                        else:
                            continue
                    break
                if fecha_reservacion.upper() == "CANCELAR":
                    break
                
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
                
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas WHERE (estado IS NULL OR estado != 'Cancelada');")
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
            
            while True:
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas WHERE (estado IS NULL OR estado != 'Cancelada');")
                    Reservaciones = {str(r[0]): (str(r[1]), str(r[2]), r[5], r[3], r[4]) for r in cursor.fetchall()}
                if not Reservaciones:
                    print("No hay reservaciones registradas.")
                    break
                
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                    Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                    cursor.execute("SELECT clave_s, nombre FROM sala;")
                    Salas = {str(s[0]): s[1] for s in cursor.fetchall()}
                
                fecha_inicio = input("Ingrese la fecha de inicio (MM/DD/AAAA) o 'CANCELAR' para salir: ").strip()
                if fecha_inicio.upper() == "CANCELAR":
                    break
                fecha_fin = input("Ingrese la fecha de fin (MM/DD/AAAA) o 'CANCELAR' para salir: ").strip()
                if fecha_fin.upper() == "CANCELAR":
                    break
                
                f_inicio = parse_fecha(fecha_inicio)
                f_fin = parse_fecha(fecha_fin)
                if f_inicio is None or f_fin is None:
                    print("Formato de fecha inválido.")
                    continue
                if f_fin < f_inicio:
                    print("La fecha de fin no puede ser anterior a la de inicio.")
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
                        print(f"{folio:<8}{fecha.strftime('%m/%d/%Y'):<12}{turno_nombre:<20}{evento:<25}{sala_nombre:<25}{cliente_nombre:<25}")
                
                folio_a_editar = input("Ingrese el folio a editar o 'CANCELAR' para salir: ").strip()
                if folio_a_editar.upper() == "CANCELAR":
                    break
                if folio_a_editar not in Reservaciones:
                    print("Folio no encontrado.")
                    continue
                
                while True:
                    nuevo_nombre = input("Ingrese el nuevo nombre del evento o 'CANCELAR' para salir: ").strip()
                    if nuevo_nombre.upper() == "CANCELAR":
                        break
                    if not nuevo_nombre or nuevo_nombre.isspace():
                        print("El nombre no puede estar vacío ni contener solo espacios.")
                        continue
                    break
                if nuevo_nombre.upper() == "CANCELAR":
                    break
                
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE reservas SET nombre_evento = ?, updated_at = CURRENT_TIMESTAMP WHERE clave_r = ?;",
                        (nuevo_nombre, int(folio_a_editar))
                    )
                    conn.commit()
                print("Evento actualizado correctamente.")
                break
        
        elif opcion == "3":
            while True:
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_r, cliente, sala, turno, fecha, nombre_evento FROM reservas WHERE (estado IS NULL OR estado != 'Cancelada');")
                    Reservaciones = {str(r[0]): (str(r[1]), str(r[2]), r[5], r[3], r[4]) for r in cursor.fetchall()}
                if not Reservaciones:
                    print("No hay reservaciones registradas.")
                    break
                
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT clave_c, nombre, apellido FROM cliente;")
                    Clientes = {str(c[0]): (c[1], c[2]) for c in cursor.fetchall()}
                    cursor.execute("SELECT clave_s, nombre FROM sala;")
                    Salas = {str(s[0]): s[1] for s in cursor.fetchall()}
                
                fecha_consulta = input("Ingrese la fecha a consultar (MM/DD/AAAA) o ENTER para fecha actual, o 'CANCELAR' para salir: ").strip()
                if fecha_consulta.upper() == "CANCELAR":
                    break
                if not fecha_consulta:
                    fecha_obj = datetime.date.today()
                else:
                    fecha_obj = parse_fecha(fecha_consulta)
                    if fecha_obj is None:
                        print("Formato de fecha inválido.")
                        continue
                fecha_iso = fecha_obj.strftime("%Y-%m-%d")

                print(f"\n{'-' * 30} REPORTE DE RESERVACIONES PARA EL DÍA ({fecha_obj.strftime('%m/%d/%Y')}) {'-' * 38}")
                print(f"{'Sala':<25}{'Cliente':<35}{'Evento':<30}{'Turno':<30}")
                print("-" *120)
                
                filas_para_csv = []
                for folio, (cli, sala, evento, turno_num, fecha_str) in Reservaciones.items():
                    fecha = parse_fecha(fecha_str)
                    if fecha is None:
                        continue
                    if fecha.strftime("%Y-%m-%d") == fecha_iso:
                        cliente_nombre = f"{Clientes[cli][1]} {Clientes[cli][0]}" if cli in Clientes else "Desconocido"
                        sala_nombre = Salas[sala] if sala in Salas else "Desconocida"
                        turno_nombre = TURNOS[int(turno_num)-1]
                        print(f"{sala_nombre:<25}{cliente_nombre:<35}{evento:<30}{turno_nombre:<30}")
                        filas_para_csv.append({
                            "Folio": folio,
                            "Fecha": fecha_str,
                            "Turno": turno_nombre,
                            "Cliente": cliente_nombre,
                            "Sala": sala_nombre,
                            "Evento": evento
                        })
                
                if not filas_para_csv:
                    print(F"\n{''*35}No hay reservaciones para esta fecha.{''* 48}")
                    print("*" * 120)
                    break
                
                resp = input("¿Desea exportar este reporte a CSV? (S/N) o 'CANCELAR' para salir: ").strip().upper()
                if resp == "CANCELAR":
                    break
                if resp == "S":
                    nombre_archivo = f"reservaciones_{fecha_obj.strftime('%Y%m%d')}.csv"
                    try:
                        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as csvfile:
                            fieldnames = ["Folio", "Fecha", "Turno", "Cliente", "Sala", "Evento"]
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            for fila in filas_para_csv:
                                fecha_csv = parse_fecha(fila["Fecha"])
                                if fecha_csv:
                                    fila["Fecha"] = fecha_csv.strftime("%m/%d/%Y")
                                writer.writerow(fila)
                        print(f"Reporte exportado correctamente a '{nombre_archivo}'.")
                    except Exception as e:
                        print(f"Ocurrió un error al exportar a CSV: {e}")
                break
            
        elif opcion == "4":
            while True:
                with sqlite3.connect("reservaciones.db") as conn:
                    cursor = conn.cursor()
                    asegurar_columna_estado(conn)
                    print("\n--- CANCELAR RESERVACIÓN ---")
                    print("Puedes escribir 'CANCELAR' en cualquier momento para volver al menú.\n")
                    
                    fecha_inicio = input("Ingresa la fecha de inicio (MM/DD/AAAA) o 'CANCELAR': ").strip()
                    if fecha_inicio.upper() == "CANCELAR":
                        break
                    fecha_fin = input("Ingresa la fecha final (MM/DD/AAAA) o 'CANCELAR': ").strip()
                    if fecha_fin.upper() == "CANCELAR":
                        break
                    try:
                        fecha_i = datetime.datetime.strptime(fecha_inicio, "%m/%d/%Y").date()
                        fecha_f = datetime.datetime.strptime(fecha_fin, "%m/%d/%Y").date()
                    except ValueError:
                        print("Formato inválido. Usa exclusivamente el formato MM/DD/AAAA.")
                        continue
                    
                    cursor.execute("""
                        SELECT clave_r, cliente, sala, fecha, nombre_evento 
                        FROM reservas 
                        WHERE (estado IS NULL OR estado != 'Cancelada');
                    """)
                    reservas = cursor.fetchall()
                    
                    hoy = datetime.date.today()
                    reservas_filtradas = []
                    for r in reservas:
                        fecha_r = parse_fecha(r[3])
                        if fecha_r and fecha_i <= fecha_r <= fecha_f and (fecha_r - hoy).days >= 2:
                            reservas_filtradas.append(r)
                    
                    if not reservas_filtradas:
                        print("\nNo se encontraron reservaciones activas en ese rango o no cumplen con los 2 días de anticipación.\n")
                        continue
                    
                    print("\nReservaciones encontradas:")
                    for r in reservas_filtradas:
                        print(f"Folio: {r[0]} | Cliente: {r[1]} | Sala: {r[2]} | Fecha: {parse_fecha(r[3]).strftime('%m/%d/%Y')} | Evento: {r[4]}")
                    
                    folio = input("\nIngresa el folio de la reservación que deseas cancelar o 'CANCELAR': ").strip()
                    if folio.upper() == "CANCELAR":
                        break
                    
                    cursor.execute("""
                        SELECT fecha FROM reservas 
                        WHERE clave_r = ? AND (estado IS NULL OR estado != 'Cancelada');
                    """, (folio,))
                    resultado = cursor.fetchone()
                    
                    if not resultado:
                        print("Folio no válido o ya cancelado.")
                        continue
                    
                    fecha_reserva = parse_fecha(resultado[0])
                    if not fecha_reserva:
                        print("Fecha inválida en la reservación.")
                        continue
                    
                    diferencia = (fecha_reserva - hoy).days
                    if diferencia < 2:
                        print("Solo puedes cancelar reservaciones con al menos 2 días de anticipación.")
                        continue
                    
                    confirmar = input("¿Seguro que deseas cancelar esta reservación? (S/N) o 'CANCELAR': ").upper()
                    if confirmar == "CANCELAR":
                        break
                    if confirmar == "S":
                        cursor.execute("UPDATE reservas SET estado = 'Cancelada', updated_at = CURRENT_TIMESTAMP WHERE clave_r = ?", (folio,))
                        conn.commit()
                        print("La reservación fue cancelada correctamente.")
                        break
                    elif confirmar == "N":
                        print("Operación cancelada.")
                        break
                    else:
                        print("Por favor responde S o N.")
                break
            
        elif opcion == "5":
            while True:
                nombre = input("Nombre del cliente o 'CANCELAR' para salir: ").strip()
                if nombre.upper() == "CANCELAR":
                    break
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                if not nombre.replace(" ", "").isalpha():
                    print("El nombre solo debe contener letras.")
                    continue
                apellido = input("Apellido del cliente o 'CANCELAR' para salir: ").strip()
                if apellido.upper() == "CANCELAR":
                    break
                if not apellido:
                    print("El apellido no puede estar vacío.")
                    continue
                if not apellido.replace(" ", "").isalpha():
                    print("El apellido solo debe contener letras.")
                    continue
                try:
                    with sqlite3.connect("reservaciones.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO cliente (nombre, apellido) VALUES (?,?);", (nombre, apellido))
                        conn.commit()
                        print("Registro agregado exitosamente")
                except Error as e:
                    print(e)
                break
        
        elif opcion == "6":
            while True:
                nombre = input("Nombre de la sala o 'CANCELAR' para salir: ").strip()
                if nombre.upper() == "CANCELAR":
                    break
                if not nombre:
                    print("El nombre de la sala no puede estar vacío.")
                    continue
                try:
                    cupo = input("Cupo de la sala o 'CANCELAR' para salir: ").strip()
                    if cupo.upper() == "CANCELAR":
                        break
                    cupo = float(cupo)
                    if cupo <= 0 or not cupo.is_integer():
                        print("El cupo debe ser un número entero positivo.")
                        continue
                    cupo = int(cupo)
                except ValueError:
                    print("El cupo solo puede contener números, sin letras ni símbolos.")
                    continue
                try:
                    with sqlite3.connect("reservaciones.db") as conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO sala(nombre, cupo) VALUES (?, ?);", (nombre, cupo))
                        conn.commit()
                        print("Registro agregado exitosamente")
                except Error as e:
                    print(e)
                break
            
        elif opcion == "7":
            confirmar = input("\n¿Seguro que deseas salir del sistema? (S/N): ").strip().upper()
            if confirmar == "S":
                print("\nSaliendo del sistema... ¡Hasta pronto!")
                break
            else:
                print("\nOperación cancelada. Regresando al menú principal...")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()