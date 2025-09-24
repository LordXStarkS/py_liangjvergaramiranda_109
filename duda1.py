import pandas as pd
import random
import datetime
import calendar
import os

# ========== GENERADOR DE DATOS ==================
def fecha_aleatoria_cuatrimestre(anio=2024):
    bloques = [(1, 4), (5, 8), (9, 12)]
    inicio_mes, fin_mes = random.choice(bloques)
    mes = random.randint(inicio_mes, fin_mes)
    _, dias_en_mes = calendar.monthrange(anio, mes)
    dia = random.randint(1, dias_en_mes)
    return datetime.date(anio, mes, dia)

def generar_datos(num_registros=1000, anio=2024, nombre_archivo="ventas_generadas.xlsx"):
    departamentos = ["Lima", "Arequipa", "Cusco", "Trujillo", "Piura", "Iquitos", "Chiclayo", "Tacna", "Puno", "Ayacucho"]
    laboratorios = ["Lab Clínico A", "Lab Clínico B", "Lab Clínico C", "Lab Clínico D", "Lab Clínico E"]
    medicamentos = ["Paracetamol", "Ibuprofeno", "Amoxicilina", "Diclofenaco", "Aspirina", "Omeprazol", "Metformina",
        "Losartán", "Atorvastatina", "Loratadina", "Clorfenamina", "Naproxeno", "Salbutamol", "Dexametasona"]
    sucursales = ["Sucursal1", "Sucursal2", "Sucursal3", "Sucursal4"]
    categorias = ["Analgésico", "Antibiótico", "Antihistamínico", "Antiácido", "Hipoglucemiante"]
    presentaciones = ["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Suspensión"]
    requiere_receta = ["Sí", "No"]
    vendedores = ["Juan Pérez", "María García", "Carlos Fernández", "Ana López"]
    metodos_pago = ["Efectivo", "Tarjeta", "Seguro"]
    clientes = ["Cliente Frecuente", "Nuevo Cliente", "Cliente VIP", "Sin Registro"]

    registros = []
    for i in range(num_registros):
        fecha = fecha_aleatoria_cuatrimestre(anio)
        departamento = random.choice(departamentos)
        sucursal = random.choice(sucursales)
        medicamento = random.choice(medicamentos)
        laboratorio = random.choice(laboratorios)
        cantidad = random.randint(1, 10)
        precio_unitario = round(random.uniform(5, 100), 2)
        total = round(cantidad * precio_unitario, 2)
        categoria = random.choice(categorias)
        presentacion = random.choice(presentaciones)
        receta = random.choice(requiere_receta)
        vendedor = random.choice(vendedores)
        hora_venta = f"{random.randint(8, 22)}:{random.randint(0, 59):02d}"
        metodo_pago = random.choice(metodos_pago)
        descuento = round(random.uniform(0, 10), 2) if random.random() < 0.3 else 0
        cliente = random.choice(clientes)

        registros.append([
            i + 1, fecha.strftime("%Y-%m-%d"), departamento, sucursal, medicamento, laboratorio, cantidad, precio_unitario, total,
            categoria, presentacion, receta, vendedor, hora_venta, metodo_pago, descuento, cliente
        ])

    df = pd.DataFrame(registros, columns=[
        "ID", "Fecha Venta", "Departamento", "Sucursal", "Medicamento", "Laboratorio", "Cantidad Vendida", "Precio Unitario", "Total Venta",
        "Categoría", "Presentación", "Requiere Receta", "Vendedor", "Hora Venta", "Método de Pago", "Descuento", "Cliente"
    ])
    
    df.to_excel(nombre_archivo, index=False)
    print(f"✅ Datos generados en: {nombre_archivo}")


# ========== BUSCADOR Y REPORTES ==================
def cargar_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        print("❌ No se encontró el archivo.")
        return None
    return pd.read_excel(nombre_archivo)

def buscar_por_mes(df, mes):
    df["Fecha Venta"] = pd.to_datetime(df["Fecha Venta"])
    return df[df["Fecha Venta"].dt.month == mes]

def buscar_por_cliente(df, cliente):
    return df[df["Cliente"].str.contains(cliente, case=False)]

def reporte_cuatrimestral(df):
    df["Fecha Venta"] = pd.to_datetime(df["Fecha Venta"])
    df["Mes"] = df["Fecha Venta"].dt.month
    condiciones = [
        (df["Mes"].between(1,4)),
        (df["Mes"].between(5,8)),
        (df["Mes"].between(9,12))
    ]
    nombres = ["Ene-Abr", "May-Ago", "Sep-Dic"]
    df["Cuatrimestre"] = pd.cut(df["Mes"], bins=[0,4,8,12], labels=nombres)
    return df.groupby("Cuatrimestre")["Total Venta"].sum()

def reporte_anual(df):
    df["Fecha Venta"] = pd.to_datetime(df["Fecha Venta"])
    df["Año"] = df["Fecha Venta"].dt.year
    return df.groupby("Año")["Total Venta"].sum()


# ========== MENÚ PRINCIPAL ==================
while True:
    print("\n📊 MENÚ DE REPORTES 📊")
    print("1) Generar nuevo archivo de ventas")
    print("2) Buscar ventas por mes")
    print("3) Buscar ventas por cliente")
    print("4) Generar reporte cuatrimestral")
    print("5) Generar reporte anual")
    print("6) Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        generar_datos()
    elif opcion in ["2","3","4","5"]:
        archivo = input("Nombre del archivo a abrir (ej: ventas_generadas.xlsx): ")
        df = cargar_archivo(archivo)
        if df is None:
            continue

        if opcion == "2":
            mes = int(input("Número de mes (1-12): "))
            resultado = buscar_por_mes(df, mes)
            print(resultado)

        elif opcion == "3":
            cliente = input("Nombre del cliente: ")
            resultado = buscar_por_cliente(df, cliente)
            print(resultado)

        elif opcion == "4":
            resultado = reporte_cuatrimestral(df)
            print(resultado)

        elif opcion == "5":
            resultado = reporte_anual(df)
            print(resultado)

    elif opcion == "6":
        print("Hasta luego 👋")
        break
    else:
        print("❌ Opción no válida")
