import os
import pandas as pd

# Pedir carpeta raíz y nombre base
carpeta_raiz = input("📁 Ingresa la ruta de la carpeta donde están los archivos: ").strip()
nuevo_nombre_base = input("📝 Ingresa el nuevo nombre base para los archivos: ").strip()

# Lista temporal para recolectar rutas de todos los archivos
todos_los_archivos = []

# Recorrer todas las carpetas y subcarpetas
for carpeta_actual, subcarpetas, archivos in os.walk(carpeta_raiz):
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_actual, archivo)
        todos_los_archivos.append((carpeta_actual, archivo, ruta_completa))

# 📌 Ordenar archivos primero por carpeta y luego por nombre
todos_los_archivos.sort(key=lambda x: (x[0].lower(), x[1].lower()))

# Lista para historial
historial = []

contador = 1
for carpeta_actual, archivo, ruta_vieja in todos_los_archivos:
    nombre, extension = os.path.splitext(archivo)
    nuevo_nombre = f"{nuevo_nombre_base}_{contador}{extension}"
    ruta_nueva = os.path.join(carpeta_actual, nuevo_nombre)

    try:
        os.rename(ruta_vieja, ruta_nueva)
        print(f"✅ {archivo} → {nuevo_nombre}")
        historial.append([archivo, nuevo_nombre, carpeta_actual])
        contador += 1
    except Exception as e:
        print(f"⚠️ No se pudo renombrar {archivo}: {e}")

# Guardar historial en Excel
df = pd.DataFrame(historial, columns=["Nombre Original", "Nuevo Nombre", "Carpeta"])
archivo_historial = os.path.join(carpeta_raiz, "historial_renombrado.xlsx")
df.to_excel(archivo_historial, index=False)

print(f"\n📊 Historial guardado en: {archivo_historial}")
print("🎉 Renombrado completado con éxito.")
