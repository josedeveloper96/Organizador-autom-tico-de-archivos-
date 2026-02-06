import os
import shutil
from pathlib import Path
from datetime import datetime

# Diccionario de categorías por tipo de archivo
CATEGORIAS = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Código': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
}

def organizar_por_tipo(directorio):
    """Organiza archivos por su extensión"""
    directorio = Path(directorio)
    
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
            shutil.move(str(archivo), str(carpeta_destino / archivo.name))
            print(f"Movido: {archivo.name} → {categoria}/")
        except Exception as e:
            print(f"Error al mover {archivo.name}: {e}")

def organizar_por_fecha(directorio):
    """Organiza archivos por año y mes de modificación"""
    directorio = Path(directorio)
    
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
            shutil.move(str(archivo), str(carpeta_destino / archivo.name))
            print(f"Movido: {archivo.name} → {año}/{mes}/")
        except Exception as e:
            print(f"Error: {e}")

def menu_principal():
    """Menú interactivo para el usuario"""
    print("\n=== ORGANIZADOR AUTOMÁTICO DE ARCHIVOS ===")
    print("1. Organizar por tipo de archivo")
    print("2. Organizar por fecha")
    print("3. Organizar por tipo Y fecha")
    print("4. Salir")
    
    return input("\nElige una opción: ")

def main():
    directorio = input("Ingresa la ruta del directorio a organizar: ")
    
    if not os.path.exists(directorio):
        print("El directorio no existe!")
        return
    
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            organizar_por_tipo(directorio)
            print("\n✓ Organización por tipo completada!")
        elif opcion == '2':
            organizar_por_fecha(directorio)
            print("\n✓ Organización por fecha completada!")
        elif opcion == '3':
            # Combinar ambas organizaciones
            print("Función combinada por implementar")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()