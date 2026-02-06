"""
ORGANIZADOR AUTOMÁTICO DE ARCHIVOS
Organiza archivos por tipo, fecha y tamaño automáticamente
Autor: Tu Nombre
Fecha: 2025
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


# Diccionario de categorías por tipo de archivo
CATEGORIAS = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.ico'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt', '.rtf'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Código': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.json', '.xml'],
    'Ejecutables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
    'Otros': []  # Para archivos que no coincidan con ninguna categoría
}


def organizar_por_tipo(directorio):
    """Organiza archivos por su extensión en carpetas de categorías"""
    directorio = Path(directorio)
    
    if not directorio.exists():
        print("❌ El directorio no existe!")
        return
    
    print(f"\n📂 Organizando archivos en: {directorio}")
    print("⏳ Procesando...\n")
    
    # Contadores para estadísticas
    archivos_movidos = 0
    categorias_usadas = {}
    
    for archivo in directorio.iterdir():
        # Saltar si es un directorio
        if archivo.is_dir():
            continue
            
        # Obtener extensión del archivo
        extension = archivo.suffix.lower()
        
        # Buscar categoría correspondiente
        categoria = 'Otros'
        for cat, extensiones in CATEGORIAS.items():
            if extension in extensiones:
                categoria = cat
                break
        
        # Crear carpeta de categoría si no existe
        carpeta_destino = directorio / categoria
        carpeta_destino.mkdir(exist_ok=True)
        
        # Mover archivo
        try:
            destino = carpeta_destino / archivo.name
            
            # Si ya existe un archivo con ese nombre, agregar número
            contador = 1
            while destino.exists():
                nombre_sin_ext = archivo.stem
                nuevo_nombre = f"{nombre_sin_ext}_{contador}{archivo.suffix}"
                destino = carpeta_destino / nuevo_nombre
                contador += 1
            
            shutil.move(str(archivo), str(destino))
            print(f"✓ {archivo.name} → {categoria}/")
            
            archivos_movidos += 1
            categorias_usadas[categoria] = categorias_usadas.get(categoria, 0) + 1
            
        except Exception as e:
            print(f"❌ Error al mover {archivo.name}: {e}")
    
    # Mostrar resumen
    print(f"\n{'='*50}")
    print("✅ ¡Organización completada!")
    print(f"{'='*50}")
    print(f"📊 Archivos organizados: {archivos_movidos}")
    print("\n📁 Distribución por categoría:")
    for categoria, cantidad in categorias_usadas.items():
        print(f"   • {categoria}: {cantidad} archivos")
    print(f"{'='*50}\n")


def organizar_por_fecha(directorio):
    """Organiza archivos por año y mes de modificación"""
    directorio = Path(directorio)
    
    if not directorio.exists():
        print("❌ El directorio no existe!")
        return
    
    print(f"\n📅 Organizando archivos por fecha en: {directorio}")
    print("⏳ Procesando...\n")
    
    archivos_movidos = 0
    
    for archivo in directorio.iterdir():
        if archivo.is_dir():
            continue
        
        # Obtener fecha de modificación
        timestamp = archivo.stat().st_mtime
        fecha = datetime.fromtimestamp(timestamp)
        
        # Crear estructura de carpetas: Año/Mes
        año = fecha.strftime('%Y')
        mes = fecha.strftime('%m - %B')
        
        carpeta_destino = directorio / año / mes
        carpeta_destino.mkdir(parents=True, exist_ok=True)
        
        # Mover archivo
        try:
            destino = carpeta_destino / archivo.name
            
            # Manejar duplicados
            contador = 1
            while destino.exists():
                nombre_sin_ext = archivo.stem
                nuevo_nombre = f"{nombre_sin_ext}_{contador}{archivo.suffix}"
                destino = carpeta_destino / nuevo_nombre
                contador += 1
            
            shutil.move(str(archivo), str(destino))
            print(f"✓ {archivo.name} → {año}/{mes}/")
            archivos_movidos += 1
            
        except Exception as e:
            print(f"❌ Error al mover {archivo.name}: {e}")
    
    # Mostrar resumen
    print(f"\n{'='*50}")
    print("✅ ¡Organización por fecha completada!")
    print(f"📊 Archivos organizados: {archivos_movidos}")
    print(f"{'='*50}\n")


def organizar_combinado(directorio):
    """Organiza por tipo primero, luego por fecha dentro de cada categoría"""
    directorio = Path(directorio)
    
    if not directorio.exists():
        print("❌ El directorio no existe!")
        return
    
    print(f"\n🔄 Organizando archivos (Tipo + Fecha) en: {directorio}")
    print("⏳ Procesando...\n")
    
    archivos_movidos = 0
    
    for archivo in directorio.iterdir():
        if archivo.is_dir():
            continue
        
        # Obtener extensión
        extension = archivo.suffix.lower()
        
        # Determinar categoría
        categoria = 'Otros'
        for cat, extensiones in CATEGORIAS.items():
            if extension in extensiones:
                categoria = cat
                break
        
        # Obtener fecha
        timestamp = archivo.stat().st_mtime
        fecha = datetime.fromtimestamp(timestamp)
        año = fecha.strftime('%Y')
        mes = fecha.strftime('%m - %B')
        
        # Crear estructura: Categoría/Año/Mes
        carpeta_destino = directorio / categoria / año / mes
        carpeta_destino.mkdir(parents=True, exist_ok=True)
        
        # Mover archivo
        try:
            destino = carpeta_destino / archivo.name
            
            # Manejar duplicados
            contador = 1
            while destino.exists():
                nombre_sin_ext = archivo.stem
                nuevo_nombre = f"{nombre_sin_ext}_{contador}{archivo.suffix}"
                destino = carpeta_destino / nuevo_nombre
                contador += 1
            
            shutil.move(str(archivo), str(destino))
            print(f"✓ {archivo.name} → {categoria}/{año}/{mes}/")
            archivos_movidos += 1
            
        except Exception as e:
            print(f"❌ Error al mover {archivo.name}: {e}")
    
    # Mostrar resumen
    print(f"\n{'='*50}")
    print("✅ ¡Organización combinada completada!")
    print(f"📊 Archivos organizados: {archivos_movidos}")
    print(f"{'='*50}\n")


def menu_principal():
    """Menú interactivo para el usuario"""
    print("\n" + "="*50)
    print("   ORGANIZADOR AUTOMÁTICO DE ARCHIVOS")
    print("="*50)
    print("1. Organizar por tipo de archivo")
    print("2. Organizar por fecha")
    print("3. Organizar por tipo Y fecha")
    print("4. Salir")
    print("="*50)
    
    return input("\nElige una opción: ")


def main():
    """Función principal del programa"""
    print("\n🚀 Bienvenido al Organizador Automático de Archivos")
    print("💡 Tip: Haz un respaldo antes de organizar archivos importantes\n")
    
    while True:
        opcion = menu_principal()
        
        if opcion == '4':
            print("\n👋 ¡Hasta luego! Mantén tus archivos organizados 📁")
            break
        
        if opcion not in ['1', '2', '3']:
            print("❌ Opción no válida. Intenta de nuevo.")
            continue
        
        # Pedir directorio
        directorio = input("\nIngresa la ruta del directorio a organizar: ").strip()
        
        # Quitar comillas si las tiene
        directorio = directorio.strip('"').strip("'")
        
        # Verificar si el directorio existe
        if not os.path.exists(directorio):
            print(f"❌ El directorio '{directorio}' no existe.")
            continue
        
        # Confirmar acción
        print(f"\n⚠️  Se organizarán todos los archivos en: {directorio}")
        confirmar = input("¿Deseas continuar? (s/n): ")
        
        if confirmar.lower() != 's':
            print("❌ Operación cancelada")
            continue
        
        # Ejecutar función según opción
        if opcion == '1':
            organizar_por_tipo(directorio)
        elif opcion == '2':
            organizar_por_fecha(directorio)
        elif opcion == '3':
            organizar_combinado(directorio)


if __name__ == "__main__":
    main()
