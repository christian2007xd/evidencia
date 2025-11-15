from tabulate import tabulate

while True:
    print("Activos")
    print ("Ingrese los activos correspondientes:")
    while True:
        try:
            Estado_efectivo_15 = float(input("Ingresa el estado de efectivo del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")
        continue

    while True:        
        try:        
            Estado_clientes_15 = float(input("Ingresa el estado de clientes del 2015: "))
            break
        except ValueError:
                print ("Favor de ingresar valores numéricos.")

    while True:
        try:
            Estado_Deudores_Diversos_15 = float(input("Ingresa el estado de deudores diversos del 2015: "))
            break
        except ValueError:
                print ("Favor de ingresar valores numéricos.")

    while True:
        try:
            Estado_Funcionarios_Empleados_15 = float(input("Ingresa el estado de funcionarios y empleados del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")
        continue

    while True:
        try:        
            Estado_Inventario_Materiales_15 = float(input("Ingresa el estado de inventario de materiales del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")  
        continue
    while True:   
        try:   
            Estado_Inventario_Producto_Terminado_15 = float(input("Ingresa el estado de Inventario de producto terminado del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")
        continue

    Total_Activo_Circulante_15 = Estado_efectivo_15 + Estado_clientes_15 + Estado_Deudores_Diversos_15 + Estado_Funcionarios_Empleados_15 + Estado_Inventario_Materiales_15 + Estado_Inventario_Producto_Terminado_15

    while True:
        try:     
            Estado_Terreno_15 = float(input("Ingresa el estado de Terreno del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")  
        continue

    while True:
        try:
            Estado_Planta_Equipo_15 = float(input("Ingresa el estado de planta y equipo del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")
        continue

    while True:
        try:
            Estado_Depreciación_acumulada_15 = float(input("Ingresa el estado de depreciación acumulada del 2015: "))
            break
        except ValueError:
            print ("Favor de ingresar valores numéricos.")
        continue
    
    Total_Activo_No_Circulante_15 = Estado_Terreno_15 + Estado_Planta_Equipo_15 - Estado_Depreciación_acumulada_15

    Total_Activos_15 = Total_Activo_Circulante_15 + Total_Activo_No_Circulante_15

    activos = [        
        ["Efectivo", f"{Estado_efectivo_15:,.2f}"],
        ["Clientes", f"{Estado_clientes_15:,.2f}"],
        ["Deudores Diversos", f"{Estado_Deudores_Diversos_15:,.2f}"], 
        ["Funcionarios y empleados", f"{Estado_Funcionarios_Empleados_15:,.2f}"],
        ["Inventario de materiales",f"{Estado_Inventario_Materiales_15:,.2f}"], 
        ["Inventario de productos terminados", f"{Estado_Inventario_Producto_Terminado_15:,.2f}"], 
        ["Total de activo circulante",f"{Total_Activo_Circulante_15:,.2f}"], 
        ["Terreno", f"{Estado_Terreno_15:,.2f}"], 
        ["Planta y equipo", f"{Estado_Planta_Equipo_15:,.2f}"],
        ["Depreciación acumulada", f"{Estado_Depreciación_acumulada_15:,.2f}"],
        ["Total de activo no circulante", f"{Total_Activo_No_Circulante_15:,.2f}"],
        ["Total de activos", f"{Total_Activos_15:,.2f}"]
    ]

    tabla_activos = tabulate(
        activos,
        tablefmt = "grid"
    )
    print ("*"*50)
    print(f'{"ACTIVOS":>48}')
    print (tabla_activos)

 
    print ("\n")
    print ("*"*50)
    print("Pasivos")
    print ("Ingrese los pasivos de 2015 correspondientes:")

    while True:
        try:
            Estado_proveedores_15 = float(input("Ingrese proveedores : "))
            break
        except ValueError:
            print("Ingrese un valor flotante.")
            continue

    while True:
        try:
            Estado_documentos_pagar_15 = float(input("Ingrese documentos por pagar: "))
            break
        except ValueError:
            print("Ingrese un valor flotante.")
            continue

    while True:
        try:
            ISR_por_pagar_15 = float(input("Ingrese ISR por pagar: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

    total_pasivo_corto_plazo_2015 = Estado_proveedores_15 + Estado_documentos_pagar_15 + ISR_por_pagar_15

    while True:
        try:
            Estado_prestamos_bancarios_15 = float((input("Ingrese estado de préstamos bancarios: ")))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

    total_pasivo_largo_plazo_15 = Estado_prestamos_bancarios_15
    pasivo_total_2015 = total_pasivo_corto_plazo_2015 + total_pasivo_largo_plazo_15
    pasivos = [
        ["Proveedores", f"{Estado_proveedores_15:,.2f}"],
        ["Documentos por pagar", f"{Estado_documentos_pagar_15:,.2f}"],
        ["ISR por pagar", f"{ISR_por_pagar_15:,.2f}"],
        ["Total pasivo a corto plazo", f"{total_pasivo_corto_plazo_2015:,.2f}"],
        ["Préstamos bancarios", f"{Estado_prestamos_bancarios_15:,.2f}"],
        ["Total pasivo a largo plazo", f"{total_pasivo_largo_plazo_15:,.2f}"],
        ["Total pasivo", f"{pasivo_total_2015:,.2f}"]
    ]
    pasivo_tabla = tabulate(
        pasivos,
        tablefmt="grid"
    )
    print ("*"*50)
    print (f"{'Pasivos':^48}")
    print (pasivo_tabla)

    print ("*"*50)
    print("Capital")
    print("Ingrese el capital correspondiente:")

    while True:
        try:
            Estado_capital_contribuido_15 = float(input("Ingrese el capital contribuido: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
    while True:
        try:
            Estado_capital_ganado_15 = float(input("Ingrese el capital ganado: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

    capital_contable_total_2015 = Estado_capital_contribuido_15 + Estado_capital_ganado_15
    capital = [
        ["Capital contribuido", f"{Estado_capital_contribuido_15:,.2f}"],
        ["Capital ganado", f"{Estado_capital_ganado_15:,.2f}"],
        ["Capital total", f"{capital_contable_total_2015:,.2f}"]
    ]
    capital_tabla = tabulate(
        capital,
        tablefmt = "grid"
    )
    print (capital_tabla)

    confirmación = pasivo_total_2015 + capital_contable_total_2015
    print("*"*20)
    print (f"La suma del pasivo y capital es {confirmación:,.2f}")
    if confirmación == Total_Activos_15:
        print("*"*20)
        print ("Concuerda con el activo. Sigue adelante.")
        break
    else:
        print("*"*20)
        print ("No concuerda con el activo, vuelve a ingresar los datos.")
        print("*"*50)
        print("\n")
        continue
    
print(f"\n{' Requerimiento de materiales ':*^50}")
print("La empresa maneja de forma fija Material A, Material B y Material C, Producto CL, Producto CE, Producto CR ")
print("*"*50)
while True:
        try:
            requerimiento_materialA_CL = float(input("Ingrese la cantidad de material A para el producto CL: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            requerimiento_materialA_CE = float(input("Ingrese la cantidad de material A para el producto CE: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            requerimiento_materialA_CR = float(input("Ingrese la cantidad de material A para el producto CR: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            requerimiento_materialB_CL = float(input("Ingrese la cantidad de material B para el producto CL: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            requerimiento_materialB_CE = float(input("Ingrese la cantidad de material B para el producto CE: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            requerimiento_materialB_CR = float(input("Ingrese la cantidad de material B para el producto CR: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            requerimiento_materialC_CL = float(input("Ingrese la cantidad de material C para el producto CL: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            requerimiento_materialC_CE = float(input("Ingrese la cantidad de material C para el producto CE: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            requerimiento_materialC_CR = float(input("Ingrese la cantidad de material C para el producto CR: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            hrs_mano_obra_CL = float(input("Ingrese la cantidad de horas de mano de obra para el producto CL: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            hrs_mano_obra_CE = float(input("Ingrese la cantidad de horas de mano de obra para el producto CE: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            hrs_mano_obra_CR = float(input("Ingrese la cantidad de horas de mano de obra para el producto CR: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

print("\n Los gastos indirectos de fabricación se aplican con base a las horas de mano de obra.")

costo_mano_obra_1erS = float(input("Ingresa el costo de mano de obra por hora durante el primer semestre."))
costo_mano_obra_2dpS = float(input("Ingresa el costo de mano de obra por hora durante el segundo semestre."))

print(f"\n{' Información de inventarios ':*^50}")
print("\n *** Primer semestre ***\n")
print("Se asume que los inventarios iniciales son iguales al final del primer semestre. No hay inventario de artículos en proceso")
while True:
        try:
            materialA_inventario1erS = float(input("Ingrese el inventario inicial del material A en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialA_costo1erS = float(input("Ingrese el costo del material A en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialB_inventario1erS = float(input("Ingrese el inventario inicial del material B en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialB_costo1erS = float(input("Ingrese el costo del material B en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialC_inventario1erS = float(input("Ingrese el inventario inicial del material C en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialC_costo1erS = float(input("Ingrese el costo del material C en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            inventariofinal_CL_1erS = float(input("Ingrese el inventario del producto CL en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")                                                                    
            continue
while True:
        try:
            inventariofinal_CE_1erS = float(input("Ingrese el inventario del producto CE en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            inventariofinal_CR_1erS = float(input("Ingrese el inventario del producto CR en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

print("\n *** Segundo semestre ***\n")
while True:
        try:
            materialA_inventario2do = float(input("Ingrese el inventario final del material A en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")                                                                                    
            continue

while True:
        try:
            materialA_costo2doS = float(input("Ingrese el costo del material A en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")                                                
            continue

while True:
        try:
            materialB_inventario2doS = float(input("Ingrese el inventario final del material B en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialB_costo2doS = float(input("Ingrese el costo del material B en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialC_inventario2doS = float(input("Ingrese el inventario final del material C en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            materialC_costo2doS = float(input("Ingrese el costo del material C en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue


while True:
        try:
            inventariofinal_CL_2doS = float(input("Ingrese el inventario del producto CL en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            inventariofinal_CE_2doS = float(input("Ingrese el inventario del producto CE en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            inventariofinal_CR_2doS = float(input("Ingrese el inventario del producto CR en el segundo semestre: "))
            break
        except ValueError:                                                                                          
            print("Ingrese datos flotantes.")
            continue
        
print(f"\n{' Productos ':*^50}")

print("\n *** Primer semestre ***\n")
while True:
        try:
            precioventa_CL_1er = float(input("Ingrese el precio de venta del producto CL en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            precioventa_CE_1er = float(input("Ingrese el precio de venta del producto CE en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            precioventa_CR_1er = float(input("Ingrese el precio de venta del producto CR en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            ventasplaneadas_CL_1er = float(input("Ingrese las ventas planeadas del producto CL en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            ventasplaneadas_CE_1er = float(input("Ingrese las ventas planeadas del producto CE en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            ventasplaneadas_CR_1er = float(input("Ingrese las ventas planeadas del producto CR en el primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

print("\n *** Segundo semestre ***\n")
while True:
        try:
            precioventa_CL_2do = float(input("Ingrese el precio de venta del producto CL en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            precioventa_CE_2do = float(input("Ingrese el precio de venta del producto CE en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            precioventa_CR_2do = float(input("Ingrese el precio de venta del producto CR en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            ventasplaneadas_CL_2do = float(input("Ingrese las ventas planeadas del producto CL en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            ventasplaneadas_CE_2do = float(input("Ingrese las ventas planeadas del producto CE en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            ventasplaneadas_CR_2do = float(input("Ingrese las ventas planeadas del producto CR en el segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

print ("\n")
print ("Gastos de administración y ventas. ")
while True:
        try:
            depreciación_admin = float(input("Ingrese la depreciación anual de administración y ventas: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue
while True:
        try:
            sueldosysalarios = float(input("Ingrese la cantidad anual de sueldos y salarios: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue

while True:
        try:
            comisiones = float(input("Ingrese el porcentaje de comisiones, de ser 100 escriba 1: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue  
while True:
        try:
            varios_admin_1ero = float(input("Ingrese la cantidad de gastos varios del primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue   
while True:
        try:
            varios_admin_2do = float(input("Ingrese la cantidad de gastos varios del segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue 
while True:
        try:
            interesesporprestamo = float(input("Ingrese la cantidad de intereses porprestamo anuales: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue      
print("\n")
print ("Gastos de Fabricación Indirectos")
while True:
        try:
            depreciación_GIF = float(input("Ingrese la cantidad de depreciacion anual: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue  
while True:
        try:
            seguros_GIF = float(input("Ingrese la cantidad de seguros anual: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue 
while True:
        try:
            mantenimiento_GIF_1ero = float(input("Ingrese la cantidad de mantenimiento del primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue   
while True:
        try:
            mantenimiento_GIF_2do = float(input("Ingrese la cantidad de mantenimiento del segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue  

while True:
        try:
            energéticos_GIF_1ero = float(input("Ingrese la cantidad de energéticos del primer semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue 
while True:
        try:
            energéticos_GIF_2do = float(input("Ingrese la cantidad de energéticos del segundo semestre: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue 

while True:
        try:
            varios_GIF = float(input("Ingrese la cantidad de gastos varios anuales: "))
            break
        except ValueError:
            print("Ingrese datos flotantes.")
            continue 
print("\n")
print ("Datos adicionales")
while True:
    try:
        equipo_nuevo = float(input("De haber un equipo nuevo, insertar su valor monetario. No se toma en cuenta la depreciación: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue
while True:
    try:
        tasa_ISR = float(input("Inserte la tasa del ISR en decimal: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue
while True:
    try:
        tasa_PTU = float(input("Inserte la tasa del PTU en decimal: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue

print ("SE PAGARA EL ISR DEL 2015")
while True:
    try:
        saldoclientes_acobrar_2015 = float(input("Inserte el porcentaje a cobrar de clientes de 2015 en decimal, de ser 100 escriba 1: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue
while True:
    try:
        ventaspresupuestadas_acobrar_2016 = float(input("Inserte el porcentaje a cobrar de ventas presupuestadas en decimal, de ser 100 escriba 1: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue
while True:
    try:
        proveedores_apagar_2016 = float(input("Inserte el porcentaje a pagar de proveedores en decimal, de ser 100 escriba 1: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue
while True:
    try:
        compraspresupuestadas_apagar_2016 = float(input("Inserte el porcentaje a pagar de compras presupuestadas en decimal, de ser 100 escriba 1: "))
        break
    except ValueError:
         print("Inserte un flotante.")
         continue

#C E D U L A SSS
print ("Presupuesto de ventas")
#producto CL
unidades_a_vender_CL_1 = ventasplaneadas_CL_1er
unidades_a_vender_CL_2 = ventasplaneadas_CL_2do
precio_venta_CL_1 = precioventa_CL_1er
precio_venta_CL_2 = precioventa_CL_2do
importe_venta_CL_1 = unidades_a_vender_CL_1*precio_venta_CL_1
importe_venta_CL_2 = unidades_a_vender_CL_2*precio_venta_CL_2
importe_venta_CL_anual = importe_venta_CL_1 + importe_venta_CL_2
#producto CE
unidades_a_vender_CE_1 = ventasplaneadas_CE_1er
unidades_a_vender_CE_2 = ventasplaneadas_CE_2do
precio_venta_CE_1 = precioventa_CE_1er
precio_venta_CE_2 = precioventa_CE_2do
importe_venta_CE_1 = unidades_a_vender_CE_1*precio_venta_CE_1
importe_venta_CE_2 = unidades_a_vender_CE_2*precio_venta_CE_2
importe_venta_CE_anual = importe_venta_CE_1 + importe_venta_CE_2
#producto CR
unidades_a_vender_CR_1 = ventasplaneadas_CR_1er
unidades_a_vender_CR_2 = ventasplaneadas_CR_2do
precio_venta_CR_1 = precioventa_CR_1er
precio_venta_CR_2 = precioventa_CR_2do
importe_venta_CR_1 = unidades_a_vender_CR_1*precio_venta_CR_1
importe_venta_CR_2 = unidades_a_vender_CR_2*precio_venta_CR_2
importe_venta_CR_anual = importe_venta_CR_1 + importe_venta_CR_2
total_ventas_S1 = importe_venta_CL_1+importe_venta_CE_1+importe_venta_CR_1
total_ventas_S2 = importe_venta_CL_2+importe_venta_CE_2+importe_venta_CR_2
total_ventas_anual = total_ventas_S1+total_ventas_S2

presupuesto_ventas = [
        ["Producto CL", "","",""],
        ["Unidades a vender", f"{unidades_a_vender_CL_1:,.2f}",f"{unidades_a_vender_CL_2:,.2f}","",""],
        ["Precio de venta", f"{precio_venta_CL_1:,.2f}", f"{precio_venta_CL_2:,.2f}","",""],
        ["Importe de venta", f"{importe_venta_CL_1:,.2f}", f"{importe_venta_CL_2:,.2f}", f"{importe_venta_CL_anual:,.2f}",""],
        ["Producto CE","","",""],
        ["Unidades a vender", f"{unidades_a_vender_CE_1:,.2f}",f"{unidades_a_vender_CE_2:,.2f}",""],
        ["Precio de venta", f"{precio_venta_CE_1:,.2f}", f"{precio_venta_CE_2:,.2f}",""],
        ["Importe de venta", f"{importe_venta_CE_1:,.2f}", f"{importe_venta_CE_2:,.2f}",f"{importe_venta_CE_anual:,.2f}"],
        ["Producto CR","","",""],
        ["Unidades a vender", f"{unidades_a_vender_CR_1:,.2f}",f"{unidades_a_vender_CR_2:,.2f}",""],
        ["Precio de venta", f"{precio_venta_CR_1:,.2f}", f"{precio_venta_CR_2:,.2f}",""],
        ["Importe de venta", f"{importe_venta_CR_1:,.2f}", f"{importe_venta_CR_2:,.2f}",f"{importe_venta_CR_anual:,.2f}"],
        ["Total de ventas por semestre", f"{total_ventas_S1:,.2f}", f"{total_ventas_S2:,.2f}",f"{total_ventas_anual:,.2f}"]
    ]
    
presupuesto_de_ventas_tabla = tabulate(
        presupuesto_ventas,
        headers = ["Producto", "Primer semestre", "Segundo semestre", "2016"],
        tablefmt = "grid"
    )
print (presupuesto_de_ventas_tabla)

#Determinación del Saldo de Clientes y Flujo de Entradas
print("Determinación del Saldo de Clientes y Flujo de Entradas")
saldo_clientes_2015 = Estado_clientes_15
ventas_2016 = total_ventas_anual
total_clientes_2016 = Estado_clientes_15 + total_ventas_anual
cobranza_2015 = saldo_clientes_2015*saldoclientes_acobrar_2015
cobranza_2016 = ventas_2016*ventaspresupuestadas_acobrar_2016
suma_cobranzas = cobranza_2015 + cobranza_2016
saldo_clientes_16 = saldo_clientes_2015 - suma_cobranzas

lista_saldo_clientes_flujo_entradas = [
    ["Saldo de clientes 31-Dic-2015", "", f"{saldo_clientes_2015:,.2f}"],
    ["Ventas 2016", "", f"{ventas_2016:,.2f}"],
    ["Total de Clientes 2016", "", f"{total_clientes_2016:,.2f}"],
    ["Entradas de Efectivo:", "",""],
    ["Por Cobranza del 2015:", f"{cobranza_2015:,.2f}", ""],
    ["Por Cobranza del 2016", f"{cobranza_2016:,.2f}", ""],
    ["","",f"{suma_cobranzas:,.2f}"],
    ["Saldo de Clientes del 2016","", f"{saldo_clientes_16:,.2f}"]
]

tabla_saldo_clientes_flujo_entradas = tabulate(
    lista_saldo_clientes_flujo_entradas,
    headers = ["Descripción","Importe","Total"],
    tablefmt = "grid"
)
print(tabla_saldo_clientes_flujo_entradas)

#Productos CL
unidades_a_vender_CL2_1 = ventasplaneadas_CL_1er
unidades_a_vender_CL2_2 = inventariofinal_CL_1erS
unidades_a_vender_CL2_2016 = unidades_a_vender_CL2_1 + unidades_a_vender_CL2_2
inventariofinal_CL2_1 =  inventariofinal_CL_1erS
inventariofinal_CL2_2 = inventariofinal_CL_2doS
inventariofinal_CL2_2016 = inventariofinal_CL_2doS
total_unidades_CL2_1 = inventariofinal_CL2_1 + unidades_a_vender_CL2_1
total_unidades_CL2_2 = inventariofinal_CL_1erS + inventariofinal_CL_2doS
total_unidades_CL2_2016 = total_unidades_CL2_1 + total_unidades_CL2_2
inventario_inicial_CL2_1 = inventariofinal_CL_1erS
inventario_inicial_CL2_2 = inventariofinal_CL_1erS
inventario_inicial_CL2_2016 = inventariofinal_CL_1erS
unidades_producir_CL2_1 = total_unidades_CL2_1 - inventario_inicial_CL2_1
unidades_producir_CL2_2 = total_unidades_CL2_2 - inventario_inicial_CL2_2
unidades_producir_CL2_2016 = unidades_producir_CL2_1 + unidades_producir_CL2_2
#Productos CE
unidades_a_vender_CE2_1 = ventasplaneadas_CE_1er
unidades_a_vender_CE2_2 = ventasplaneadas_CE_2do
unidades_a_vender_CE2_2016 = unidades_a_vender_CE2_1 + unidades_a_vender_CE2_2
invenatrio_final_CE2_1 = inventariofinal_CE_1erS
invenatrio_final_CE2_2 = inventariofinal_CE_2doS   
invenatrio_final_CE2_2016 = inventariofinal_CE_2doS
total_unidades_CE2_1 = unidades_a_vender_CE2_1 + invenatrio_final_CE2_1
total_unidades_CE2_2 = unidades_a_vender_CE2_2 + invenatrio_final_CE2_2
total_unidades_CE2_2016 = total_unidades_CE2_1 + total_unidades_CE2_2
inventario_inicial_CE2_1 = inventariofinal_CE_1erS
inventario_inicial_CE2_2 = inventariofinal_CE_1erS
inventario_inicial_CE2_2016 = inventariofinal_CE_1erS
unidades_producir_CE2_1 = total_unidades_CE2_1 - inventario_inicial_CE2_1
unidades_producir_CE2_2 = total_unidades_CE2_2 - inventario_inicial_CE2_2
unidades_producir_CE2_2016 = unidades_producir_CE2_1 + unidades_producir_CE2_2


#Productos CR
unidades_a_vender_CR2_1 = ventasplaneadas_CR_1er
unidades_a_vender_CR2_2 = ventasplaneadas_CR_2do
unidades_a_vender_CR2_2016 = unidades_a_vender_CR2_1 + unidades_a_vender_CR2_2
invenatrio_final_CR2_1 = inventariofinal_CR_1erS
invenatrio_final_CR2_2 = inventariofinal_CR_2doS
invenatrio_final_CR2_2016 = inventariofinal_CR_2doS
total_unidades_CR2_1 = unidades_a_vender_CR2_1 + invenatrio_final_CR2_1
total_unidades_CR2_2 = unidades_a_vender_CR2_2 + invenatrio_final_CR2_2
total_unidades_CR2_2016 = total_unidades_CR2_1 + total_unidades_CR2_2
inventario_inicial_CR2_1 = inventariofinal_CR_1erS
inventario_inicial_CR2_2 = inventariofinal_CR_1erS
inventario_inicial_CR2_2016 = inventariofinal_CR_1erS 
unidades_producir_CR2_1 = total_unidades_CR2_1 - inventario_inicial_CR2_1
unidades_producir_CR2_2 = total_unidades_CR2_2 - inventario_inicial_CR2_2
unidades_producir_CR2_2016 = unidades_producir_CR2_1 + unidades_producir_CR2_2


presupuesto_produccion = [
    ["3. Presupuesto de Producción", "", "", ""],
    ["", "1er. Semestre", "2do. Semestre", "Total 2016"],

    ["PRODUCTO CL", "", "", ""],
    ["Unidades a vender", f"{unidades_a_vender_CL2_1:,.2f}", f"{unidades_a_vender_CL2_2:,.2f}", f"{unidades_a_vender_CL2_2016:,.2f}"],
    ["(+) Inventario Final", f"{inventariofinal_CL2_1:,.2f}", f"{inventariofinal_CL2_2:,.2f}", f"{inventariofinal_CL2_2016:,.2f}"],
    ["(=) Total de Unidades", f"{total_unidades_CL2_1:,.2f}", f"{total_unidades_CL2_2:,.2f}", f"{total_unidades_CL2_2016:,.2f}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_CL2_1:,.2f}", f"{inventario_inicial_CL2_2:,.2f}", f"{inventario_inicial_CL2_2016:,.2f}"],
    ["(=) Unidades a Producir", f"{unidades_producir_CL2_1:,.2f}", f"{unidades_producir_CL2_2:,.2f}", f"{unidades_producir_CL2_2016:,.2f}"],

    ["PRODUCTO CE", "", "", ""],
    ["Unidades a vender", f"{unidades_a_vender_CE2_1:,.2f}", f"{unidades_a_vender_CE2_2:,.2f}", f"{unidades_a_vender_CE2_2016:,.2f}"],
    ["(+) Inventario Final", f"{invenatrio_final_CE2_1:,.2f}", f"{invenatrio_final_CE2_2:,.2f}", f"{invenatrio_final_CE2_2016:,.2f}"],
    ["(=) Total de Unidades", f"{total_unidades_CE2_1:,.2f}", f"{total_unidades_CE2_2:,.2f}", f"{total_unidades_CE2_2016:,.2f}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_CE2_1:,.2f}", f"{inventario_inicial_CE2_2:,.2f}", f"{inventario_inicial_CE2_2016:,.2f}"],
    ["(=) Unidades a Producir", f"{unidades_producir_CE2_1:,.2f}", f"{unidades_producir_CE2_2:,.2f}", f"{unidades_producir_CE2_2016:,.2f}"],

    ["PRODUCTO CR", "", "", ""],
    ["Unidades a vender",f"{unidades_a_vender_CR2_1:,.2f}", f"{unidades_a_vender_CR2_2:,.2f}", f"{unidades_a_vender_CR2_2016:,.2f}"],
    ["(+) Inventario Final", f"{invenatrio_final_CR2_1:,.2f}", f"{invenatrio_final_CR2_2:,.2f}", f"{invenatrio_final_CR2_2016:,.2f}"],
    ["(=) Total de Unidades", f"{total_unidades_CR2_1:,.2f}", f"{total_unidades_CR2_2:,.2f}", f"{total_unidades_CR2_2016:,.2f}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_CR2_1:,.2f}", f"{inventario_inicial_CR2_2:,.2f}", f"{inventario_inicial_CR2_2016:,.2f}"],
    ["(=) Unidades a Producir", f"{unidades_producir_CR2_1:,.2f}", f"{unidades_producir_CR2_2:,.2f}", f"{unidades_producir_CR2_2016:,.2f}"],
]

presupuesto_produccion_tabla = tabulate(
    presupuesto_produccion,
    headers = ["Producto", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt = "grid"
)
print(presupuesto_produccion_tabla)

#PRODUCTO CL MATERIAL A
unidades_a_producir_CL_1 = ventasplaneadas_CL_1er
unidades_a_producir_CL_2 = inventariofinal_CL_2doS
unidades_a_producir_CL_2016 = unidades_a_producir_CL_1 + unidades_a_producir_CL_2
requerimiento_material_CL_A_1 = requerimiento_materialA_CL
requerimiento_material_CL_A_2 = requerimiento_materialA_CL
requerimiento_material_CL_A_2016 = requerimiento_materialA_CL
total_A_requerido_CL_1 = requerimiento_material_CL_A_1 * unidades_a_producir_CL_1
total_A_requerido_CL_2 = requerimiento_material_CL_A_2 * unidades_a_producir_CL_2
total_A_requerido_CL_2016 = total_A_requerido_CL_1 + total_A_requerido_CL_2
#producto CL material B
requerimiento_material_CL_B_1 = requerimiento_materialB_CL
requerimiento_material_CL_B_2 = requerimiento_materialB_CL
requerimiento_material_CL_B_2016 = requerimiento_materialB_CL
total_B_requerido_CL_1 = requerimiento_material_CL_B_1 * unidades_a_producir_CL_1
total_B_requerido_CL_2 = requerimiento_material_CL_B_2 * unidades_a_producir_CL_2
total_B_requerido_CL_2016 = total_B_requerido_CL_1 + total_B_requerido_CL_2
#producto CL material C
requerimiento_material_CL_C_1 = requerimiento_materialC_CL
requerimiento_material_CL_C_2 = requerimiento_materialC_CL
requerimiento_material_CL_C_2016 = requerimiento_materialC_CL
total_C_requerido_CL_1 = requerimiento_material_CL_C_1 * unidades_a_producir_CL_1
total_C_requerido_CL_2 = requerimiento_material_CL_C_2 * unidades_a_producir_CL_2
total_C_requerido_CL_2016 = total_C_requerido_CL_1 + total_C_requerido_CL_2

#PRODUCTO CE MATERIAL A
unidades_a_producir_CE_1 = ventasplaneadas_CE_1er
unidades_a_producir_CE_2 = unidades_producir_CE2_2
unidades_a_producir_CE_2016 = unidades_a_producir_CE_1 + unidades_a_producir_CE_2
requerimiento_material_CE_A_1 = requerimiento_materialA_CE
requerimiento_material_CE_A_2 = requerimiento_materialA_CE
requerimiento_material_CE_A_2016 = requerimiento_materialA_CE
total_A_requerido_CE_1 = requerimiento_material_CE_A_1 * unidades_a_producir_CE_1
total_A_requerido_CE_2 = requerimiento_material_CE_A_2 * unidades_a_producir_CE_2
total_A_requerido_CE_2016 = total_A_requerido_CE_1 + total_A_requerido_CE_2
#producto CE material B
requerimiento_material_CE_B_1 = requerimiento_materialB_CE
requerimiento_material_CE_B_2 = requerimiento_materialB_CE
requerimiento_material_CE_B_2016 = requerimiento_materialB_CE
total_B_requerido_CE_1 = requerimiento_material_CE_B_1 * unidades_a_producir_CE_1
total_B_requerido_CE_2 = requerimiento_material_CE_B_2 * unidades_a_producir_CE_2
total_B_requerido_CE_2016 = total_B_requerido_CE_1 + total_B_requerido_CE_2
#producto CE material C
requerimiento_material_CE_C_1 = requerimiento_materialC_CE
requerimiento_material_CE_C_2 = requerimiento_materialC_CE
requerimiento_material_CE_C_2016 = requerimiento_materialC_CE
total_C_requerido_CE_1 = requerimiento_material_CE_C_1 * unidades_a_producir_CE_1
total_C_requerido_CE_2 = requerimiento_material_CE_C_2 * unidades_a_producir_CE_2
total_C_requerido_CE_2016 = total_C_requerido_CE_1 + total_C_requerido_CE_2

#PRODUCTO CR MATERIAL A
unidades_a_producir_CR_1 = ventasplaneadas_CR_1er
unidades_a_producir_CR_2 = unidades_producir_CR2_2
unidades_a_producir_CR_2016 = unidades_a_producir_CR_1 + unidades_a_producir_CR_2
requerimiento_material_CR_A_1 = requerimiento_materialA_CR
requerimiento_material_CR_A_2 = requerimiento_materialA_CR
requerimiento_material_CR_A_2016 = requerimiento_materialA_CR
total_A_requerido_CR_1 = requerimiento_material_CR_A_1 * unidades_a_producir_CR_1
total_A_requerido_CR_2 = requerimiento_material_CR_A_2 * unidades_a_producir_CR_2
total_A_requerido_CR_2016 = total_A_requerido_CR_1 + total_A_requerido_CR_2
#producto CR material B
requerimiento_material_CR_B_1 = requerimiento_materialB_CR
requerimiento_material_CR_B_2 = requerimiento_materialB_CR
requerimiento_material_CR_B_2016 = requerimiento_materialB_CR
total_B_requerido_CR_1 = requerimiento_material_CR_B_1 * unidades_a_producir_CR_1
total_B_requerido_CR_2 = requerimiento_material_CR_B_2 * unidades_a_producir_CR_2
total_B_requerido_CR_2016 = total_B_requerido_CR_1 + total_B_requerido_CR_2
#producto CR material C
requerimiento_material_CR_C_1 = requerimiento_materialC_CR
requerimiento_material_CR_C_2 = requerimiento_materialC_CR
requerimiento_material_CR_C_2016 = requerimiento_materialC_CR
total_C_requerido_CR_1 = requerimiento_material_CR_C_1 * unidades_a_producir_CR_1
total_C_requerido_CR_2 = requerimiento_material_CR_C_2 * unidades_a_producir_CR_2
total_C_requerido_CR_2016 = total_C_requerido_CR_1 + total_C_requerido_CR_2

#Total de requerimientos en A
total_de_material_A_requerido_1 = total_A_requerido_CL_1 + total_A_requerido_CE_1 + total_A_requerido_CR_1
total_de_material_A_requerido_2 = total_A_requerido_CL_2 + total_A_requerido_CE_2 + total_A_requerido_CR_2
total_de_material_A_requerido_2016 = total_A_requerido_CL_2016 + total_A_requerido_CE_2016 + total_A_requerido_CR_2016

#Total de requerimientos en B
total_de_material_B_requerido_1 = total_B_requerido_CL_1 + total_B_requerido_CE_1 + total_B_requerido_CR_1
total_de_material_B_requerido_2 = total_B_requerido_CL_2 + total_B_requerido_CE_2 + total_B_requerido_CR_2
total_de_material_B_requerido_2016 = total_B_requerido_CL_2016 + total_B_requerido_CE_2016 + total_B_requerido_CR_2016

#Total de requerimientos en C
total_de_material_C_requerido_1 = total_C_requerido_CL_1 + total_C_requerido_CE_1 + total_C_requerido_CR_1
total_de_material_C_requerido_2 = total_C_requerido_CL_2 + total_C_requerido_CE_2 + total_C_requerido_CR_2
total_de_material_C_requerido_2016 = total_C_requerido_CL_2016 + total_C_requerido_CE_2016 + total_C_requerido_CR_2016


presupuesto_requerimiento_materiales = [
    ["PRODUCTO CL", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CL_1:,.2f}", f"{unidades_a_producir_CL_2:,.2f}", f"{unidades_a_producir_CL_2016:,.2f}"],

    ["Material A", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CL_A_1:,.2f}", f"{requerimiento_material_CL_A_2:,.2f}", f"{requerimiento_material_CL_A_2016:,.2f}"],
    ["Total de Material A requerido", f"{total_A_requerido_CL_1:,.2f}", f"{total_A_requerido_CL_2:,.2f}", f"{total_A_requerido_CL_2016:,.2f}"],

    ["Material B", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CL_B_1:,.2f}", f"{requerimiento_material_CL_B_2:,.2f}", f"{requerimiento_material_CL_B_2016:,.2f}"],
    ["Total de Material B requerido", f"{total_B_requerido_CL_1:,.2f}", f"{total_B_requerido_CL_2:,.2f}", f"{total_B_requerido_CL_2016:,.2f}"],

    ["Material C", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CL_C_1:,.2f}", f"{requerimiento_material_CL_C_2:,.2f}", f"{requerimiento_material_CL_C_2016:,.2f}"],
    ["Total de Material C requerido", f"{total_C_requerido_CL_1:,.2f}", f"{total_C_requerido_CL_2:,.2f}", f"{total_C_requerido_CL_2016:,.2f}"],

    ["PRODUCTO CE", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CE_1:,.2f}", f"{unidades_a_producir_CE_2:,.2f}", f"{unidades_a_producir_CE_2016:,.2f}"],

    ["Material A", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CE_A_1:,.2f}", f"{requerimiento_material_CE_A_2:,.2f}", f"{requerimiento_material_CE_A_2016:,.2f}"],
    ["Total de Material A requerido", f"{total_A_requerido_CE_1:,.2f}", f"{total_A_requerido_CE_2:,.2f}", f"{total_A_requerido_CE_2016:,.2f}"],

    ["Material B", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CE_B_1:,.2f}",f"{requerimiento_material_CE_B_2:,.2f}", f"{requerimiento_material_CE_B_2016:,.2f}"],
    ["Total de Material B requerido", f"{total_B_requerido_CE_1:,.2f}", f"{total_B_requerido_CE_2:,.2f}", f"{total_B_requerido_CE_2016:,.2f}"],

    ["Material C", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CE_C_1:,.2f}", f"{requerimiento_material_CE_C_2:,.2f}", f"{requerimiento_material_CE_C_2016:,.2f}"],
    ["Total de Material C requerido", f"{total_C_requerido_CE_1:,.2f}", f"{total_C_requerido_CE_2:,.2f}", f"{total_C_requerido_CE_2016:,.2f}"],

    ["PRODUCTO CR", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CR_1:,.2f}", f"{unidades_a_producir_CR_2:,.2f}", f"{unidades_a_producir_CR_2016:,.2f}"],

    ["Material A", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CR_A_1:,.2f}", f"{requerimiento_material_CR_A_2:,.2f}", f"{requerimiento_material_CR_A_2016:,.2f}"],
    ["Total de Material A requerido", f"{total_A_requerido_CR_1:,.2f}", f"{total_A_requerido_CR_2:,.2f}", f"{total_A_requerido_CR_2016:,.2f}"],

    ["Material B", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CR_B_1}", f"{requerimiento_material_CR_B_2}", f"{requerimiento_material_CR_B_2016}"],
    ["Total de Material B requerido", f"{total_B_requerido_CR_1}", f"{total_B_requerido_CR_2}", f"{total_B_requerido_CR_2016}"],

    ["Material C", "", "", ""],
    ["Requerimiento de material", f"{requerimiento_material_CR_C_1}", f"{requerimiento_material_CR_C_2}", f"{requerimiento_material_CR_C_2016}"],
    ["Total de Material C requerido", f"{total_C_requerido_CR_1}", f"{total_C_requerido_CR_2}", f"{total_C_requerido_CR_2016}"],

    ["Total de Requerimientos", "", "", ""],
    ["Material A", f"{total_de_material_A_requerido_1}", f"{total_de_material_A_requerido_2}", f"{total_de_material_A_requerido_2016}"],
    ["Material B", f"{total_de_material_B_requerido_1}", f"{total_de_material_B_requerido_2}", f"{total_de_material_B_requerido_2016}"],
    ["Material C", f"{total_de_material_C_requerido_1}", f"{total_de_material_C_requerido_2}", f"{total_de_material_C_requerido_2016}"],
]

presupuesto_requerimiento_materiales_tabla = tabulate(
    presupuesto_requerimiento_materiales,
    headers=["Producto", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt="grid"
)
print(presupuesto_requerimiento_materiales_tabla)

#presupuesto de compra de materiales A
requerimiento_material_A_1 = total_de_material_A_requerido_1
requerimiento_material_A_2 = total_de_material_A_requerido_2
requerimiento_material_A_2016 = total_de_material_A_requerido_2016
inventario_final_A_1 = materialA_inventario1erS
inventario_final_A_2 = materialA_inventario2do
inventario_final_A_2016 = materialA_inventario2do
total_de_material_A_requerido_1 = requerimiento_material_A_1 + inventario_final_A_1
total_de_material_A_requerido_2 = requerimiento_material_A_2 + inventario_final_A_2
total_de_material_A_requerido_2016 = requerimiento_material_A_2016 + inventario_final_A_2016
inventario_inicial_A_1 = materialA_inventario1erS
inventario_inicial_A_2 = materialA_inventario1erS
inventario_inicial_A_2016 = materialA_inventario1erS
materia_comprar_A_1 = total_de_material_A_requerido_1 - inventario_inicial_A_1
materia_comprar_A_2 = total_de_material_A_requerido_2 - inventario_inicial_A_2
materia_comprar_A_2016 = total_de_material_A_requerido_2016 - inventario_inicial_A_2016
precio_de_compra_A_1 = materialA_costo1erS
precio_de_compra_A_2 = materialA_costo2doS
total_de_material_A_dinero_1 = materia_comprar_A_1 * precio_de_compra_A_1 
total_de_material_A_dinero_2 = materia_comprar_A_2 * precio_de_compra_A_2
total_de_material_A_dinero_2016 = total_de_material_A_dinero_1 + total_de_material_A_dinero_2

#presupuesto de compra de materiales B
requerimiento_material_B_1 = total_de_material_B_requerido_1
requerimiento_material_B_2 = total_de_material_B_requerido_2
requerimiento_material_B_2016 = total_de_material_B_requerido_2016
inventario_final_B_1 = materialB_inventario1erS
inventario_final_B_2 = materialB_inventario2doS
inventario_final_B_2016 = materialB_inventario2doS
total_de_material_B_requerido_1 = requerimiento_material_B_1 + inventario_final_B_1
total_de_material_B_requerido_2 = requerimiento_material_B_2 + inventario_final_B_2
total_de_material_B_requerido_2016 = requerimiento_material_B_2016 + inventario_final_B_2016
inventario_inicial_B_1 = materialB_inventario1erS
inventario_inicial_B_2 = materialB_inventario1erS
inventario_inicial_B_2016 = materialB_inventario1erS
materia_comprar_B_1 = total_de_material_B_requerido_1 - inventario_inicial_B_1
materia_comprar_B_2 = total_de_material_B_requerido_2 - inventario_inicial_B_2
materia_comprar_B_2016 = total_de_material_B_requerido_2016 - inventario_inicial_B_2016
precio_de_compra_B_1 = materialB_costo1erS
precio_de_compra_B_2 = materialB_costo2doS
total_de_material_B_dinero_1 = materia_comprar_B_1 * precio_de_compra_B_1 
total_de_material_B_dinero_2 = materia_comprar_B_2 * precio_de_compra_B_2
total_de_material_B_dinero_2016 = total_de_material_B_dinero_1 + total_de_material_B_dinero_2

#presupuesto de compra de materiales C
requerimiento_material_C_1 = total_de_material_C_requerido_1
requerimiento_material_C_2 = total_de_material_C_requerido_2
requerimiento_material_C_2016 = total_de_material_C_requerido_2016
inventario_final_C_1 = materialC_inventario1erS
inventario_final_C_2 = materialC_inventario2doS
inventario_final_C_2016 = materialC_inventario2doS
total_de_material_C_requerido_1 = requerimiento_material_C_1 + inventario_final_C_1
total_de_material_C_requerido_2 = requerimiento_material_C_2 + inventario_final_C_2
total_de_material_C_requerido_2016 = requerimiento_material_C_2016 + inventario_final_C_2016
inventario_inicial_C_1 = materialC_inventario1erS
inventario_inicial_C_2 = materialC_inventario1erS
inventario_inicial_C_2016 = materialC_inventario1erS
materia_comprar_C_1 = total_de_material_C_requerido_1 - inventario_inicial_C_1
materia_comprar_C_2 = total_de_material_C_requerido_2 - inventario_inicial_C_2
materia_comprar_C_2016 = total_de_material_C_requerido_2016 - inventario_inicial_C_2016
precio_de_compra_C_1 = materialC_costo1erS
precio_de_compra_C_2 = materialC_costo2doS
total_de_material_C_dinero_1 = materia_comprar_C_1 * precio_de_compra_C_1 
total_de_material_C_dinero_2 = materia_comprar_C_2 * precio_de_compra_C_2
total_de_material_C_dinero_2016 = total_de_material_C_dinero_1 + total_de_material_C_dinero_2

#Total de compras de materiales
Compras_totales_1 = total_de_material_A_dinero_1 + total_de_material_B_dinero_1 + total_de_material_C_dinero_1
compras_totales_2 = total_de_material_A_dinero_2 + total_de_material_B_dinero_2 + total_de_material_C_dinero_2
compras_totales_2016 = total_de_material_A_dinero_2016 + total_de_material_B_dinero_2016 + total_de_material_C_dinero_2016

presupuesto_compra_materiales = [
    ["Material A", "", "", ""],
    ["Requerimiento de materiales", f"{requerimiento_material_A_1}", f"{requerimiento_material_A_2}", f"{requerimiento_material_A_2016}"],
    ["(+) Inventario Final", f"{inventario_final_A_1}", f"{inventario_final_A_2}", f"{inventario_final_A_2016}"],
    ["Total de Materiales", f"{total_de_material_A_requerido_1}", f"{total_de_material_A_requerido_2}", f"{total_de_material_A_requerido_2016}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_A_1}", f"{inventario_inicial_A_2}", f"{inventario_inicial_A_2016}"],
    ["Material a comprar", f"{materia_comprar_A_1}", f"{materia_comprar_A_2}", f"{materia_comprar_A_2016}"],
    ["Precio de Compra", f"{precio_de_compra_A_1}", f"{precio_de_compra_A_2}",""],
    ["Total de Material A en $", f"{total_de_material_A_dinero_1}", f"{total_de_material_A_dinero_2}", f"{total_de_material_A_dinero_2016}"],

    ["Material B", "", "", ""],
    ["Requerimiento de materiales", f"{requerimiento_material_B_1}", f"{requerimiento_material_B_2}", f"{requerimiento_material_B_2016}"],
    ["(+) Inventario Final", f"{inventario_final_B_1}", f"{inventario_final_B_2}", f"{inventario_final_B_2016}"],
    ["Total de Materiales", f"{total_de_material_B_requerido_1}", f"{total_de_material_B_requerido_2}", f"{total_de_material_B_requerido_2016}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_B_1}", f"{inventario_inicial_B_2}", f"{inventario_inicial_B_2016}"],
    ["Material a comprar", f"{materia_comprar_B_1}", f"{materia_comprar_B_2}", f"{materia_comprar_B_2016}"],
    ["Precio de Compra", f"{precio_de_compra_B_1}", f"{precio_de_compra_B_2}",""],
    ["Total de Material B en $", f"{total_de_material_B_dinero_1}", f"{total_de_material_B_dinero_2}", f"{total_de_material_B_dinero_2016}"],

    ["Material C", "", "", ""],
    ["Requerimiento de materiales", f"{requerimiento_material_C_1}", f"{requerimiento_material_C_2}", f"{requerimiento_material_C_2016}"],
    ["(+) Inventario Final", f"{inventario_final_C_1}", f"{inventario_final_C_2}", f"{inventario_final_C_2016}"],
    ["Total de Materiales", f"{total_de_material_C_requerido_1}", f"{total_de_material_C_requerido_2}", f"{total_de_material_C_requerido_2016}"],
    ["(-) Inventario Inicial", f"{inventario_inicial_C_1}", f"{inventario_inicial_C_2}", f"{inventario_inicial_C_2016}"],
    ["Material a comprar", f"{materia_comprar_C_1}", f"{materia_comprar_C_2}", f"{materia_comprar_C_2016}"],
    ["Precio de Compra", f"{precio_de_compra_C_1}", f"{precio_de_compra_C_2}",""],
    ["Total de Material C en $", f"{total_de_material_C_dinero_1}", f"{total_de_material_C_dinero_2}"],

    ["Compras totales", f"{Compras_totales_1}", f"{compras_totales_2}", f"{compras_totales_2016}"]
]

presupuesto_compra_materiales_tabla = tabulate(
    presupuesto_compra_materiales,
    headers=["Producto", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt="grid"
)
print(presupuesto_compra_materiales_tabla)

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#6 Determinación del saldo de Proveedores 

saldo_proveedores_1 = Estado_proveedores_15
Compras_2016 = compras_totales_2016
saldo_proveedores_2016 = saldo_proveedores_1 + Compras_2016
Por_proveedores_2015 = Estado_proveedores_15
Por_proveedores_2016 = Compras_2016 * 0.5
total_salario_2016 = Por_proveedores_2015 + Por_proveedores_2016
salario_proveedores_2016 = total_salario_2016

presupuesto_saldo_proveedores = [
    ["Saldo de Proveedores 31-Dic-2015", "", f"{saldo_proveedores_1:,.2f}"],
    ["Compras 2016", "", f"{Compras_2016:,.2f}"],
    ["Total de Proveedores 2016", "", f"{saldo_proveedores_2016:,.2f}"],

    ["Salidas de Efectivo:", "", ""],
    ["Por Proveedores del 2015", f"{Por_proveedores_2015:,.2f}", ""],
    ["Por Proveedores del 2016", f"{Por_proveedores_2016:,.2f}", ""],
    ["Total de Salidas 2016:", "", f"{total_salario_2016:,.2f}"],

    ["Saldo de Proveedores del 2016", "", f"{salario_proveedores_2016:,.2f}"]
]

presupuesto_saldo_proveedores_tabla = tabulate(
    presupuesto_saldo_proveedores,
    headers=["Descripción", "Importe", "Total"],
    tablefmt="grid"
)
print(presupuesto_saldo_proveedores_tabla)

#7 Presupuesto de Mano de Obra Directa

#PRODUCTO CL
unidades_a_producir_CL2_1 = ventasplaneadas_CL_1er
unidades_a_producir_CL2_2 = inventariofinal_CL_2doS
unidades_a_producir_CL2_2016 = unidades_a_producir_CL2_1 + unidades_a_producir_CL2_2
horas_requeridas_CL2_1 = hrs_mano_obra_CL
horas_requeridas_CL2_2 = hrs_mano_obra_CL
horas_requeridas_CL2_2016 = hrs_mano_obra_CL
total_horas_requeridas_CL2_1 = unidades_a_producir_CL2_1 * horas_requeridas_CL2_1
total_horas_requeridas_CL2_2 = unidades_a_producir_CL2_2 * horas_requeridas_CL2_2
total_horas_requeridas_CL2_2016 = total_horas_requeridas_CL2_1 + total_horas_requeridas_CL2_2
cuota_por_hora_CL2_1 = costo_mano_obra_1erS
cuota_por_hora_CL2_2 = costo_mano_obra_2dpS
importe_de_MOD_CL2_1 = total_horas_requeridas_CL2_1 * cuota_por_hora_CL2_1
importe_de_MOD_CL2_2 = total_horas_requeridas_CL2_2 * cuota_por_hora_CL2_2
importe_de_MOD_CL2_2016 = importe_de_MOD_CL2_1 + importe_de_MOD_CL2_2
#PRODUCTO CE
unidades_a_producir_CE2_1 = unidades_producir_CE2_1
unidades_a_producir_CE2_2 = unidades_producir_CE2_2
unidades_a_producir_CE2_2016 = unidades_a_producir_CE2_1 + unidades_a_producir_CE2_2
horas_requeridas_CE2_1 = hrs_mano_obra_CE
horas_requeridas_CE2_2 = hrs_mano_obra_CE
horas_requeridas_CE2_2016 = hrs_mano_obra_CE
total_horas_requeridas_CE2_1 = unidades_a_producir_CE2_1 * horas_requeridas_CE2_1
total_horas_requeridas_CE2_2 = unidades_a_producir_CE2_2 * horas_requeridas_CE2_2
total_horas_requeridas_CE2_2016 = total_horas_requeridas_CE2_1 + total_horas_requeridas_CE2_2
cuota_por_hora_CE2_1 = costo_mano_obra_1erS
cuota_por_hora_CE2_2 = costo_mano_obra_2dpS
importe_de_MOD_CE2_1 = total_horas_requeridas_CE2_1 * cuota_por_hora_CE2_1
importe_de_MOD_CE2_2 = total_horas_requeridas_CE2_2 * cuota_por_hora_CE2_2
importe_de_MOD_CE2_2016 = importe_de_MOD_CE2_1 + importe_de_MOD_CE2_2
#PRODUCTO CR
unidades_a_producir_CR2_1 = unidades_producir_CR2_1
unidades_a_producir_CR2_2 = unidades_producir_CR2_2
unidades_a_producir_CR2_2016 = unidades_a_producir_CR2_1 + unidades_a_producir_CR2_2
horas_requeridas_CR2_1 = hrs_mano_obra_CR
horas_requeridas_CR2_2 = hrs_mano_obra_CR
horas_requeridas_CR2_2016 = hrs_mano_obra_CR
total_horas_requeridas_CR2_1 = unidades_a_producir_CR2_1 * horas_requeridas_CR2_1
total_horas_requeridas_CR2_2 = unidades_a_producir_CR2_2 * horas_requeridas_CR2_2
total_horas_requeridas_CR2_2016 = total_horas_requeridas_CR2_1 + total_horas_requeridas_CR2_2
cuota_por_hora_CR2_1 = costo_mano_obra_1erS
cuota_por_hora_CR2_2 = costo_mano_obra_2dpS
importe_de_MOD_CR2_1 = total_horas_requeridas_CR2_1 * cuota_por_hora_CR2_1
importe_de_MOD_CR2_2 = total_horas_requeridas_CR2_2 * cuota_por_hora_CR2_2
importe_de_MOD_CR2_2016 = importe_de_MOD_CR2_1 + importe_de_MOD_CR2_2
#TOTAL
total_de_horas_requeridas_1 = total_horas_requeridas_CL2_1 + total_horas_requeridas_CE2_1 + total_horas_requeridas_CR2_1
total_de_horas_requeridas_2 = total_horas_requeridas_CL2_2 + total_horas_requeridas_CE2_2 + total_horas_requeridas_CR2_2
total_de_horas_requeridas_2016 = total_de_horas_requeridas_1 + total_de_horas_requeridas_2
total_MOD_1 = importe_de_MOD_CL2_1 + importe_de_MOD_CE2_1 + importe_de_MOD_CR2_1
total_MOD_2 = importe_de_MOD_CL2_2 + importe_de_MOD_CE2_2 + importe_de_MOD_CR2_2
total_MOD_2016 = total_MOD_1 + total_MOD_2

presupuesto_mano_obra_directa = [
    ["PRODUCTO CL", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CL2_1:,.2f}", f"{unidades_a_producir_CL2_2:,.2f}", f"{unidades_a_producir_CL2_2016:,.2f}"],
    ["Horas requeridas por unidad", f"{horas_requeridas_CL2_1:,.2f}", f"{horas_requeridas_CL2_2:,.2f}", f"{horas_requeridas_CL2_2016:,.2f}"],
    ["Total de horas requeridas", f"{total_horas_requeridas_CL2_1:,.2f}", f"{total_horas_requeridas_CL2_2:,.2f}", f"{total_horas_requeridas_CL2_2016:,.2f}"],
    ["Cuota por hora", f"{cuota_por_hora_CL2_1:,.2f}", f"{cuota_por_hora_CL2_2:,.2f}"],
    ["Importe de M.O.D.", f"{importe_de_MOD_CL2_1:,.2f}", f"{importe_de_MOD_CL2_2:,.2f}", f"{importe_de_MOD_CL2_2016:,.2f}"],

    ["PRODUCTO CE", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CE2_1:,.2f}", f"{unidades_a_producir_CE2_2:,.2f}", f"{unidades_a_producir_CE2_2016:,.2f}"],
    ["Horas requeridas por unidad", f"{horas_requeridas_CE2_1:,.2f}", f"{horas_requeridas_CE2_2:,.2f}", f"{horas_requeridas_CE2_2016:,.2f}"],
    ["Total de horas requeridas", f"{total_horas_requeridas_CE2_1:,.2f}", f"{total_horas_requeridas_CE2_2:,.2f}", f"{total_horas_requeridas_CE2_2016:,.2f}"],
    ["Cuota por hora", f"{cuota_por_hora_CE2_1:,.2f}", f"{cuota_por_hora_CE2_2:,.2f}"],
    ["Importe de M.O.D.", f"{importe_de_MOD_CE2_1:,.2f}", f"{importe_de_MOD_CE2_2:,.2f}", f"{importe_de_MOD_CE2_2016:,.2f}"],

    ["PRODUCTO CR", "", "", ""],
    ["Unidades a producir", f"{unidades_a_producir_CR2_1:,.2f}", f"{unidades_a_producir_CR2_2:,.2f}", f"{unidades_a_producir_CR2_2016:,.2f}"],
    ["Horas requeridas por unidad", f"{horas_requeridas_CR2_1:,.2f}", f"{horas_requeridas_CR2_2:,.2f}", f"{horas_requeridas_CR2_2016:,.2f}"],
    ["Total de horas requeridas", f"{total_horas_requeridas_CR2_1:,.2f}", f"{total_horas_requeridas_CR2_2:,.2f}", f"{total_horas_requeridas_CR2_2016:,.2f}"],
    ["Cuota por hora", f"{cuota_por_hora_CR2_1:,.2f}", f"{cuota_por_hora_CR2_2:,.2f}"],
    ["Importe de M.O.D.", f"{importe_de_MOD_CR2_1:,.2f}", f"{importe_de_MOD_CR2_2:,.2f}", f"{importe_de_MOD_CR2_2016:,.2f}"],

    ["Total de horas requeridas por semestre", f"{total_de_horas_requeridas_1:,.2f}", f"{total_de_horas_requeridas_2:,.2f}", f"{total_de_horas_requeridas_2016:,.2f}"],
    ["Total de M.O.D. por semestre", f"{total_MOD_1:,.2f}", f"{total_MOD_2:,.2f}", f"{total_MOD_2016:,.2f}"]
]
presupuesto_mano_obra_directa_tabla = tabulate(
    presupuesto_mano_obra_directa,
    headers=["Producto", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt="grid"
)
print(presupuesto_mano_obra_directa_tabla)

# 8 Presupuesto G.I.F.
depreciacion_1 = depreciación_GIF/2
depreciacion_2 = depreciacion_1
depreciacion_2016 = depreciacion_1 +depreciacion_2
seguros_1 = seguros_GIF/2
seguros_2 = seguros_1
seguros_2016 = seguros_1 +seguros_2
mantenimiento_1 = mantenimiento_GIF_1ero
mantenimiento_2 = mantenimiento_GIF_2do
mantenimiento_2016 = mantenimiento_1 +mantenimiento_2
energeticos_1 = energéticos_GIF_1ero
energeticos_2 = energéticos_GIF_2do
energeticos_2016 = energeticos_1 +energeticos_2
varios_1 = varios_GIF/2
varios_2 = varios_1
varios_2016 = varios_1 +varios_2
total_gif_1 = depreciacion_1 + seguros_1 + mantenimiento_1 + energeticos_1 + varios_1
total_gif_2 = depreciacion_2 + seguros_2 + mantenimiento_2 + energeticos_2 + varios_2
total_gif_2016 = total_gif_1 + total_gif_2
Total_GIF = total_gif_2016
Total_horas_MOD = total_de_horas_requeridas_2016
Costo_por_hora_GIF = Total_GIF/Total_horas_MOD

presupuesto_gif = [
    ["Depreciación", f"{depreciacion_1:,.2f}", f"{depreciacion_2:,.2f}", f"{depreciacion_2016:,.2f}"],
    ["Seguros", f"{seguros_1:,.2f}", f"{seguros_2:,.2f}", f"{seguros_2016:,.2f}"],
    ["Mantenimiento", f"{mantenimiento_1:,.2f}", f"{mantenimiento_2:,.2f}", f"{mantenimiento_2016:,.2f}"],
    ["Energéticos", f"{energeticos_1:,.2f}", f"{energeticos_2:,.2f}", f"{energeticos_2016:,.2f}"],
    ["Varios", f"{varios_1:,.2f}", f"{varios_2:,.2f}", f"{varios_2016:,.2f}"],
    ["Total G.I.F. por semestre", f"{total_gif_1:,.2f}", f"{total_gif_2:,.2f}", f"{total_gif_2016:,.2f}"],

    ["Coeficiente para determinar el costo por hora de G.I.F.", "", "", ""],
    ["Total de G.I.F.", "", "", f"{Total_GIF:,.2f}"],
    ["(/) Total horas M.O.D. Anual", "", "", f"{Total_horas_MOD:,.2f}"],
    ["(=) Costo por Hora de G.I.F.", "", "", f"{Costo_por_hora_GIF:,.2f}"]
]

presupuesto_gif_tabla = tabulate(
    presupuesto_gif,
    headers=["Descripción", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt="grid"
)
print(presupuesto_gif_tabla)

# 9 GASTO DE OPERACIÓN
depreciacion_GO_1 = depreciación_admin/2
depreciacion_GO_2 = depreciacion_GO_1
depreciacion_GO_2016 = depreciacion_GO_1 +depreciacion_GO_2
sueldos_GO_1 = sueldosysalarios/2
sueldos_GO_2 = sueldos_GO_1
sueldos_GO_2016 = sueldos_GO_1 +sueldos_GO_2
comisiones_GO_1 = total_ventas_S1 * 0.01
comisiones_GO_2 = total_ventas_S2 * 0.01
comisiones_GO_2016 = comisiones_GO_1 +comisiones_GO_2
varios_GO_1 = varios_admin_1ero
varios_GO_2 = varios_admin_2do
varios_GO_2016 = varios_GO_1 +varios_GO_2
intereses_GO_1 = interesesporprestamo/2
intereses_GO_2 = intereses_GO_1
intereses_GO_2016 = intereses_GO_1 +intereses_GO_2
total_gastos_operacion_1 = depreciacion_GO_1 + sueldos_GO_1 + comisiones_GO_1 + varios_GO_1 + intereses_GO_1
total_gastos_operacion_2 = depreciacion_GO_2 + sueldos_GO_2 + comisiones_GO_2 + varios_GO_2 + intereses_GO_2
total_gastos_operacion_2016 = total_gastos_operacion_1 + total_gastos_operacion_2

presupuesto_gastos_operacion = [
    ["Depreciación", f"{depreciacion_GO_1:,.2f}", f"{depreciacion_GO_2:,.2f}", f"{depreciacion_GO_2016:,.2f}"],
    ["Sueldos y Salarios", f"{sueldos_GO_1:,.2f}", f"{sueldos_GO_2:,.2f}", f"{sueldos_GO_2016:,.2f}"],
    ["Comisiones", f"{comisiones_GO_1:,.2f}", f"{comisiones_GO_2:,.2f}", f"{comisiones_GO_2016:,.2f}"],
    ["Varios", f"{varios_GO_1:,.2f}", f"{varios_GO_2:,.2f}", f"{varios_GO_2016:,.2f}"],
    ["Intereses del Préstamo", f"{intereses_GO_1:,.2f}", f"{intereses_GO_2:,.2f}", f"{intereses_GO_2016:,.2f}"],
    ["Total de Gastos de Operación:", f"{total_gastos_operacion_1:,.2f}", f"{total_gastos_operacion_2:,.2f}", f"{total_gastos_operacion_2016:,.2f}"]
]
presupuesto_gastos_operacion_tabla = tabulate(
    presupuesto_gastos_operacion,
    headers=["Descripción", "1er. Semestre", "2do. Semestre", "Total 2016"],
    tablefmt="grid"
)
print(presupuesto_gastos_operacion_tabla)

# 10. Determinación del Costo Unitario de Productos Terminados

#producto CL
material_A_CL_CO = materialA_costo2doS
material_A_CL_CA =requerimiento_materialA_CL
material_A_CL_CU = material_A_CL_CO * material_A_CL_CA
material_B_CL_CO = materialB_costo2doS
material_B_CL_CA =requerimiento_materialB_CL
material_B_CL_CU = material_B_CL_CO * material_B_CL_CA
material_C_CL_CO = materialC_costo2doS
material_C_CL_CA =requerimiento_materialC_CL
material_C_CL_CU = material_C_CL_CO * material_C_CL_CA
mano_obra_CL_CO = costo_mano_obra_2dpS
mano_obra_CL_CA = hrs_mano_obra_CL
mano_obra_CL_CU = mano_obra_CL_CO * mano_obra_CL_CA
gasto_indirecto_fabricacion_CL_CO = Costo_por_hora_GIF
gasto_indirecto_fabricacion_CL_CA = hrs_mano_obra_CL
gasto_indirecto_fabricacion_CL_CU = gasto_indirecto_fabricacion_CL_CO *gasto_indirecto_fabricacion_CL_CA
total_costo_unitario_CL_CU = material_A_CL_CU + material_B_CL_CU + material_C_CL_CU + mano_obra_CL_CU + gasto_indirecto_fabricacion_CL_CU

#producto CE
material_A_CE_CO = materialA_costo2doS
material_A_CE_CA =requerimiento_materialA_CE
material_A_CE_CU = material_A_CE_CO * material_A_CE_CA
material_B_CE_CO = materialB_costo2doS
material_B_CE_CA =requerimiento_materialB_CE
material_B_CE_CU = material_B_CE_CO * material_B_CE_CA
material_C_CE_CO = materialC_costo2doS
material_C_CE_CA =requerimiento_materialC_CE
material_C_CE_CU = material_C_CE_CO * material_C_CE_CA
mano_obra_CE_CO = costo_mano_obra_2dpS
mano_obra_CE_CA = hrs_mano_obra_CE
mano_obra_CE_CU = mano_obra_CE_CO * mano_obra_CE_CA
gasto_indirecto_fabricacion_CE_CO = Costo_por_hora_GIF
gasto_indirecto_fabricacion_CE_CA = hrs_mano_obra_CE
gasto_indirecto_fabricacion_CE_CU = gasto_indirecto_fabricacion_CE_CO * gasto_indirecto_fabricacion_CE_CA
total_costo_unitario_CE_CU = material_A_CE_CU + material_B_CE_CU + material_C_CE_CU + mano_obra_CE_CU + gasto_indirecto_fabricacion_CE_CU

#producto CR
material_A_CR_CO = materialA_costo2doS
material_A_CR_CA =requerimiento_materialA_CR
material_A_CR_CU = material_A_CR_CO * material_A_CR_CA
material_B_CR_CO = materialB_costo2doS
material_B_CR_CA =requerimiento_materialB_CR
material_B_CR_CU = material_B_CR_CO * material_B_CR_CA
material_C_CR_CO = materialC_costo2doS
material_C_CR_CA =requerimiento_materialC_CR
material_C_CR_CU = material_C_CR_CO * material_C_CR_CA
mano_obra_CR_CO = costo_mano_obra_2dpS
mano_obra_CR_CA = hrs_mano_obra_CR
mano_obra_CR_CU = mano_obra_CR_CO * mano_obra_CR_CA
gasto_indirecto_fabricacion_CR_CO = Costo_por_hora_GIF
gasto_indirecto_fabricacion_CR_CA = hrs_mano_obra_CR
gasto_indirecto_fabricacion_CR_CU = gasto_indirecto_fabricacion_CR_CO * gasto_indirecto_fabricacion_CR_CA 
total_costo_unitario_CR_CU = material_A_CR_CU + material_B_CR_CU + material_C_CR_CU + mano_obra_CR_CU + gasto_indirecto_fabricacion_CR_CU
costo_unitario_productos = [
    ["PRODUCTO CL", "", "", ""],
    ["Material A", f"{material_A_CL_CO:,.2f}", f"{material_A_CL_CA:,.2f}", f"{material_A_CL_CU:,.2f}"],
    ["Material B", f"{material_B_CL_CO:,.2f}", f"{material_B_CL_CA:,.2f}", f"{material_B_CL_CU:,.2f}"],
    ["Material C", f"{material_C_CL_CO:,.2f}", f"{material_C_CL_CA:,.2f}", f"{material_C_CL_CU:,.2f}"],
    ["Mano de Obra", f"{mano_obra_CL_CO:,.2f}", f"{mano_obra_CL_CA:,.2f}", f"{mano_obra_CL_CU:,.2f}"],
    ["Gastos Indirectos de Fabricación", f"{gasto_indirecto_fabricacion_CL_CO:,.2f}", f"{gasto_indirecto_fabricacion_CL_CA:,.2f}", f"{gasto_indirecto_fabricacion_CL_CU:,.2f}"],
    ["Costo Unitario", "", "", f"{total_costo_unitario_CL_CU:,.2f}"],

    ["PRODUCTO CE", "", "", ""],
    ["Material A", f"{material_A_CE_CO:,.2f}", f"{material_A_CE_CA:,.2f}", f"{material_A_CE_CU:,.2f}"],
    ["Material B", f"{material_B_CE_CO:,.2f}", f"{material_B_CE_CA:,.2f}", f"{material_B_CE_CU:,.2f}"],
    ["Material C", f"{material_C_CE_CO:,.2f}", f"{material_C_CE_CA:,.2f}", f"{material_C_CE_CU:,.2f}"],
    ["Mano de Obra", f"{mano_obra_CE_CO:,.2f}", f"{mano_obra_CE_CA:,.2f}", f"{mano_obra_CE_CU:,.2f}"],
    ["Gastos Indirectos de Fabricación", f"{gasto_indirecto_fabricacion_CE_CO:,.2f}", f"{gasto_indirecto_fabricacion_CE_CA:,.2f}", f"{gasto_indirecto_fabricacion_CE_CU:,.2f}"],
    ["Costo Unitario", "", "", f"{total_costo_unitario_CE_CU:,.2f}"],

    ["PRODUCTO CR", "", "", ""],
    ["Material A", f"{material_A_CR_CO:,.2f}", f"{material_A_CR_CA:,.2f}", f"{material_A_CR_CU:,.2f}"],
    ["Material B", f"{material_B_CR_CO:,.2f}", f"{material_B_CR_CA:,.2f}", f"{material_B_CR_CU:,.2f}"],
    ["Material C", f"{material_C_CR_CO:,.2f}", f"{material_C_CR_CA:,.2f}", f"{material_C_CR_CU:,.2f}"],
    ["Mano de Obra", f"{mano_obra_CR_CO:,.2f}", f"{mano_obra_CR_CA:,.2f}", f"{mano_obra_CR_CU:,.2f}"],
    ["Gastos Indirectos de Fabricación", f"{gasto_indirecto_fabricacion_CR_CO:,.2f}", f"{gasto_indirecto_fabricacion_CR_CA:,.2f}", f"{gasto_indirecto_fabricacion_CR_CU:,.2f}"],
    ["Costo Unitario", "", "", f"{total_costo_unitario_CR_CU:,.2f}"],
]

costo_unitario_tabla = tabulate(
    costo_unitario_productos,
    headers=["Descripción", "Costo", "Cantidad", "Costo Unitario"],
    tablefmt="grid"
)
print(costo_unitario_tabla)

# 11 Valuacion de Inventarios Finales 

#Material A
material_A_U = materialA_inventario2do
material_A_CU = material_A_CL_CO
material_A_CT = material_A_U * material_A_CU

#Material B
material_B_U = materialB_inventario2doS
material_B_CU = material_B_CE_CO
material_B_CT = material_B_U * material_B_CU

#Material C
material_C_U = materialC_inventario2doS
material_C_CU = material_C_CR_CO
material_C_CT = material_C_U * material_C_CU

#Inventario Final de Materiales
ct_inv_final_materiales = material_A_CT + material_B_CT + material_C_CT

#Producto CL
producto_CL_U = inventariofinal_CL_2doS
producto_CL_CU = total_costo_unitario_CL_CU
producto_CL_CT = producto_CL_U * producto_CL_CU

# Producto CE 
producto_CE_U = inventariofinal_CE_2doS
producto_CE_CU = total_costo_unitario_CE_CU
producto_CE_CT = producto_CE_U * producto_CE_CU

# Producto CR
producto_CR_U = inventariofinal_CR_2doS
producto_CR_CU = total_costo_unitario_CR_CU
producto_CR_CT = producto_CR_U * producto_CR_CU 

# Inventario Final de Producto Termiando
ct_inv_final_producto_terminado = producto_CL_CT + producto_CE_CT + producto_CR_CT 


valuacion_inventarios_finales = [
    ["INVENTARIO FINAL DE MATERIALES", "", "", ""],
    ["Material A", f"{material_A_U:,.2f}", f"{material_A_CU:,.2f}", f"{material_A_CT:,.2f}"],
    ["Material B", f"{material_B_U:,.2f}", f"{material_B_CU:,.2f}", f"{material_B_CT:,.2f}"],
    ["Material C", f"{material_C_U:,.2f}", f"{material_C_CU:,.2f}", f"{material_C_CT:,.2f}"],
    ["Inventario Final de Materiales", "", "", f"{ct_inv_final_materiales:,.2f}"],

    ["INVENTARIO FINAL DE PRODUCTO TERMINADO", "", "", ""],
    ["Producto CL", f"{producto_CL_U:,.2f}", f"{producto_CL_CU:,.2f}", f"{producto_CL_CT:,.2f}"],
    ["Producto CE", f"{producto_CE_U:,.2f}", f"{producto_CE_CU:,.2f}", f"{producto_CE_CT:,.2f}"],
    ["Producto CR", f"{producto_CR_U:,.2f}", f"{producto_CR_CU:,.2f}", f"{producto_CR_CT:,.2f}"],
    ["Inventario Final de Producto Terminado", "", "", f"{ct_inv_final_producto_terminado:,.2f}"]
]

valuacion_inventarios_finales_tabla = tabulate(
    valuacion_inventarios_finales,
    headers=["Descripción", "Unidades", "Costo Unitario", "Costo Total"],
    tablefmt="grid"
)
print(valuacion_inventarios_finales_tabla)

# Presupuesto financiero

saldo_inicial_materiales = Estado_Inventario_Materiales_15
compras_materiales = compras_totales_2016
material_disponible = saldo_inicial_materiales + compras_materiales
inventario_final_materiales = ct_inv_final_materiales
materiales_utilizados = material_disponible - inventario_final_materiales
mano_obra_directa = total_MOD_2016
gastos_fabricacion_indirectos = Total_GIF
costo_produccion = materiales_utilizados + mano_obra_directa + gastos_fabricacion_indirectos
inventario_ini_productos_terminados = Estado_Inventario_Producto_Terminado_15
total_produccion_disponible = costo_produccion + inventario_ini_productos_terminados
inventario_fin_productos_terminados = ct_inv_final_producto_terminado
costo_ventas = total_produccion_disponible - inventario_fin_productos_terminados

Estado_de_costo = [
    ["ESTADO DE COSTO DE PRODUCCION Y VENTAS", ""],
    ["Saldo Inicial de Materiales", f"{saldo_inicial_materiales:,.2f}"],
    ["(+) Compras de Materiales", f"{compras_materiales:,.2f}"],
    ["(=) Material Disponible", f"{material_disponible:,.2f}"],
    ["(-) Inventario Final de Materiales", f"{inventario_final_materiales:,.2f}"],
    ["(=) Materiales Utilizados", f"{materiales_utilizados:,.2f}"],
    ["(+) Mano de Obra Directa", f"{mano_obra_directa:,.2f}"],
    ["(+) Gastos de Fabricación Indirectos", f"{gastos_fabricacion_indirectos:,.2f}"],
    ["(=) Costo de Producción", f"{costo_produccion:,.2f}"],
    ["(+) Inventario Inicial de Productos Terminados", f"{inventario_ini_productos_terminados:,.2f}"],
    ["(=) Total de Producción Disponible", f"{total_produccion_disponible:,.2f}"],
    ["(-) Inventario Final de Productos Terminados", f"{inventario_fin_productos_terminados:,.2f}"],
    ["(=) Costo de Ventas", f"{costo_ventas:,.2f}"]
]

Estado_de_costo_tabla = tabulate(
    Estado_de_costo,
    headers=["Descripción", "Importe"],
    tablefmt="grid"
)
print(Estado_de_costo_tabla)


#Estado de Resultados
ventas_est_result = total_ventas_anual
costo_ventas_est_result = costo_ventas
utilidad_bruta_est_result = ventas_est_result - costo_ventas_est_result
gastos_operacion_est_result = total_gastos_operacion_2016
utilidad_operacion_est_result = utilidad_bruta_est_result - gastos_operacion_est_result
isr_est_result = utilidad_operacion_est_result * 0.3
ptu_est_result = utilidad_operacion_est_result * 0.1
utilidad_neta_est_result = utilidad_operacion_est_result - isr_est_result - ptu_est_result


estado_resultados = [
    ["ESTADO DE RESULTADOS", ""],
    ["Ventas", f"{ventas_est_result:,.2f}"],
    ["(-) Costo de Ventas", f"{costo_ventas_est_result:,.2f}"],
    ["(=) Utilidad Bruta", f"{utilidad_bruta_est_result :,.2f}"],
    ["(-) Gastos de Operación", f"{gastos_operacion_est_result:,.2f}"],
    ["(=) Utilidad de Operación", f"{utilidad_operacion_est_result:,.2f}"],
    ["(-) ISR", f"{isr_est_result :,.2f}"],
    ["(-) PTU", f"{ptu_est_result:,.2f}"],
    ["(=) Utilidad Neta", f"{utilidad_neta_est_result:,.2f}"]
]

estado_resultados_tabla = tabulate(
    estado_resultados,
    headers=["Descripción", "Importe"],
    tablefmt="grid"
)
print(estado_resultados_tabla)


# Estado de Flujo Efectivo

saldo_inicial_efectivo = Estado_efectivo_15
cobranza_EFE_2016 = cobranza_2016
cobranza_EFE_2015 = cobranza_2015
total_entradas = cobranza_EFE_2016 + cobranza_EFE_2015
efectivo_disponible = total_entradas + saldo_inicial_efectivo
proveedores_EFE_2016 = Por_proveedores_2016
proveedores_EFE_2015 = Por_proveedores_2015
pago_mano_obra_directa = total_MOD_2016
pago_gastos_indirectos_fab = depreciacion_2016 - Total_GIF
pago_gastos_operacion = depreciacion_GO_2016 - total_gastos_operacion_2016
compra_activo_fijo = equipo_nuevo
pago_isr_2015 = ISR_por_pagar_15 
total_de_salidas = proveedores_EFE_2016 + proveedores_EFE_2015 + pago_mano_obra_directa + pago_gastos_indirectos_fab + pago_gastos_operacion + compra_activo_fijo + pago_isr_2015
flujo_de_efectivo_act = efectivo_disponible - total_de_salidas 


estado_flujo_efectivo = [
    ["ESTADO DE FLUJO EFECTIVO", "", ""], 
    ["Saldo Inicial de Efectivo", "", f"{saldo_inicial_efectivo:,.2f}"],
    ["Entradas:", "", ""],
    ["Cobranza 2016", f"{cobranza_EFE_2016:,.2f}", ""],
    ["Cobranza 2015", f"{cobranza_EFE_2015:,.2f}", ""],
    ["Total de Entradas", "", f"{total_entradas:,.2f}"],
    ["Efectivo Disponible", "", f"{efectivo_disponible:,.2f}"],
    ["Salidas:", "", ""],
    ["Proveedores 2016", f"{proveedores_EFE_2016:,.2f}", ""],
    ["Proveedores 2015", f"{proveedores_EFE_2015:,.2f}", ""],
    ["Pago Mano de Obra Directa", f"{pago_mano_obra_directa:,.2f}", ""],
    ["Pago Gastos Indirectos de Fabricación", f"{pago_gastos_indirectos_fab:,.2f}", ""],
    ["Pago de Gastos de Operación", f"{pago_gastos_operacion:,.2f}", ""],
    ["Compra de Activo Fijo (Maquinaria)", f"{compra_activo_fijo :,.2f}", ""],
    ["Pago ISR 2015", f"{pago_isr_2015:,.2f}", ""],
    ["Pago ISR 2016", "", ""],
    ["Total de Salidas", "", f"{total_de_salidas:,.2f}"],
    ["Flujo de Efectivo Actual", "", f"{flujo_de_efectivo_act:,.2f}"]
]

estado_flujo_efectivo_tabla = tabulate(
    estado_flujo_efectivo,
    headers=["Descripción", "Importe"],
    tablefmt="grid"
)
print(estado_flujo_efectivo_tabla)


# Balance General

# CIRCULANTE

efectivo_BG = flujo_de_efectivo_act
clientes_BG = saldo_clientes_16
deudores_div_BG = Estado_Deudores_Diversos_15
func_emp_BG = Estado_Funcionarios_Empleados_15
inv_materiales_BG = ct_inv_final_materiales
inv_prod_term_BG = ct_inv_final_producto_terminado
total_AC = efectivo_BG + clientes_BG + deudores_div_BG + func_emp_BG + inv_materiales_BG + inv_prod_term_BG

#NO CIRCULANTE

terreno_BG = Estado_Terreno_15
planta_equipo_BG = Estado_Planta_Equipo_15 + compra_activo_fijo
dp_acum_BG = Estado_Depreciación_acumulada_15 -  depreciacion_2016 - depreciacion_GO_2016
total_ANC = terreno_BG + planta_equipo_BG + dp_acum_BG

#ACTIVO TOTAL
activo_total_BG = total_AC + total_ANC

#PASIVO

#CORTO PLAZO
proveedores_BG = salario_proveedores_2016
isr_por_p1 = Estado_documentos_pagar_15
isr_por_p2 = isr_est_result
ptu_por_p = ptu_est_result
total_pas_corto_p = proveedores_BG + isr_por_p1 + isr_por_p2 + ptu_por_p

#LARGO PLAZO
presta_banc_BG = Estado_prestamos_bancarios_15
total_pas_largo_p = presta_banc_BG
pasivo_total_BG = total_pas_corto_p + total_pas_largo_p

#CAPITAL CONTABLE

capital_cont_BG = Estado_capital_contribuido_15
capital_gan_BG = Estado_capital_ganado_15
uti_eje_BG = utilidad_neta_est_result
total_cap_cont = capital_cont_BG + capital_gan_BG + uti_eje_BG

#SUMA DE PASIVO Y CAPITAL
suma_P_C = pasivo_total_BG + total_cap_cont




balance_general = [
    ["BALANCE GENERAL", "", ""],
    ["ACTIVO", "", ""],
    ["Circulante", "", ""],
    ["Efectivo", f"{efectivo_BG:,.2f}", ""],
    ["Clientes", f"{clientes_BG:,.2f}", ""],
    ["Deudores Diversos", f"{deudores_div_BG:,.2f}", ""],
    ["Funcionarios y Empleados", f"{func_emp_BG:,.2f}", ""],
    ["Inventario de Materiales", f"{inv_materiales_BG:,.2f}", ""],
    ["Inventario de Producto Terminado", f"{inv_prod_term_BG:,.2f}", ""],
    ["Total de Activos Circulantes:", "", f"{total_AC :,.2f}"], 
    ["", "", ""],
    ["No Circulante", "", ""],
    ["Terreno", f"{terreno_BG:,.2f}", ""],
    ["Planta y Equipo", f"{planta_equipo_BG:,.2f}", ""],
    ["Depreciación Acumulada", f"{dp_acum_BG:,.2f}", ""],
    ["Total Activos No Circulante", "", f"{total_ANC:,.2f}"],
    ["", "", ""],
    ["ACTIVO TOTAL", "", f"{activo_total_BG:,.2f}"],
    ["", "", ""],
    ["PASIVO", "", ""],
    ["Corto Plazo", "", ""],
    ["Proveedores", f"{proveedores_BG:,.2f}",""],
    ["Documentos por Pagar", f"{isr_por_p1:,.2f}", ""],
    ["ISR por Pagar", f"{isr_por_p2:,.2f}", ""],
    ["PTU por Pagar", f"{ptu_por_p:,.2f}", ""],
    ["Total de Pasivo Corto Plazo:", "", f"{total_pas_corto_p:,.2f}"],
    ["", "", ""],
    ["Largo Plazo", "", ""],
    ["Préstamos Bancarios", f"{presta_banc_BG:,.2f}", ""],
    ["Total de Pasivo Largo Plazo:", "", f"{total_pas_largo_p:,.2f}"],
    ["", "", ""],
    ["PASIVO TOTAL", "", f"{pasivo_total_BG:,.2f}"],
    ["", "", ""],
    ["CAPITAL CONTABLE", "", ""],
    ["Capital Contribuido", f"{capital_cont_BG :,.2f}", ""],
    ["Capital Ganado", f"{capital_gan_BG:,.2f}", ""],
    ["Utilidad del Ejercicio", f"{uti_eje_BG:,.2f}", ""],
    ["Total de Capital Contable", "", f"{total_cap_cont:,.2f}"],
    ["", "", ""],
    ["SUMA DE PASIVO Y CAPITAL", "", f"{suma_P_C:,.2f}"]
]

balance_general_tabla = tabulate(
    balance_general,
    headers=["Descripción", "Importe"],
    tablefmt="grid"
)
print(balance_general_tabla)
