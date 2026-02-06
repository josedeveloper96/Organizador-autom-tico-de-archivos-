# 📁 Organizador Automático de Archivos

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Mantén tus carpetas organizadas automáticamente** 🚀

Un script en Python que organiza tus archivos y documentos automáticamente por tipo, fecha o tamaño. ¡Adiós al caos digital!

[Características](#-características) •
[Instalación](#-instalación) •
[Uso](#-uso) •
[Ejemplos](#-ejemplos)

</div>

---

## 🌟 Características

### Organización por Tipo de Archivo
Clasifica automáticamente tus archivos en carpetas según su extensión:

- 📷 **Imágenes** - JPG, PNG, GIF, SVG, BMP
- 📄 **Documentos** - PDF, DOC, DOCX, TXT, XLSX, PPTX
- 🎬 **Videos** - MP4, AVI, MKV, MOV, WMV
- 🎵 **Audio** - MP3, WAV, FLAC, AAC
- 📦 **Comprimidos** - ZIP, RAR, 7Z, TAR, GZ
- 💻 **Código** - PY, JS, HTML, CSS, JAVA, CPP
- 📋 **Otros** - Todo lo que no encaje en las categorías anteriores

### Organización por Fecha
Estructura tus archivos por:
- 📅 **Año / Mes** - Organiza por fecha de modificación
- 🗓️ **Fecha de creación** - Agrupa por cuándo se crearon los archivos

### Organización por Tamaño (próximamente)
- 📊 Pequeños (< 1MB)
- 📊 Medianos (1MB - 100MB)
- 📊 Grandes (> 100MB)

---

## 🎯 ¿Por qué usar este organizador?

| Problema | Solución |
|----------|----------|
| 😵 Carpeta de Descargas desordenada | ✅ Organización automática por tipo |
| 🔍 No encuentras tus archivos | ✅ Todo clasificado en carpetas lógicas |
| ⏰ Pierdes tiempo organizando manualmente | ✅ Automatización en segundos |
| 📅 Necesitas agrupar por fechas | ✅ Organización cronológica automática |

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- Sistemas operativos: Windows, macOS, Linux

### Instalación Rápida

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/organizador-archivos.git

# Entra al directorio
cd organizador-archivos

# ¡Listo para usar! No requiere dependencias externas
```

---

## 💻 Uso

### Ejecución Básica

```bash
python organizador_archivos.py
```

### Menú Interactivo

Al ejecutar el script, verás este menú:

```
=== ORGANIZADOR AUTOMÁTICO DE ARCHIVOS ===
1. Organizar por tipo de archivo
2. Organizar por fecha
3. Organizar por tipo Y fecha
4. Salir

Elige una opción:
```

### Opciones Disponibles

#### 1️⃣ Organizar por Tipo

Agrupa archivos en carpetas según su extensión.

```
Ingresa la ruta del directorio: C:/Users/Tu/Downloads
```

**Antes:**
```
Downloads/
├── foto1.jpg
├── documento.pdf
├── video.mp4
├── cancion.mp3
└── archivo.zip
```

**Después:**
```
Downloads/
├── Imágenes/
│   └── foto1.jpg
├── Documentos/
│   └── documento.pdf
├── Videos/
│   └── video.mp4
├── Audio/
│   └── cancion.mp3
└── Comprimidos/
    └── archivo.zip
```

#### 2️⃣ Organizar por Fecha

Organiza archivos por año y mes de modificación.

**Resultado:**
```
Downloads/
├── 2024/
│   ├── 01 - January/
│   │   └── informe_enero.pdf
│   └── 12 - December/
│       └── foto_navidad.jpg
└── 2025/
    └── 02 - February/
        └── documento_reciente.docx
```

#### 3️⃣ Organización Combinada

Primero organiza por tipo, luego por fecha dentro de cada categoría.

---

## 📸 Ejemplos Visuales

### Caso de Uso 1: Carpeta de Descargas

**Escenario:** Tienes 150 archivos mezclados en tu carpeta de Descargas

```bash
python organizador_archivos.py
# Opción: 1
# Ruta: C:/Users/Tu/Downloads

✓ Organización completada!
  - 45 imágenes movidas
  - 32 documentos organizados
  - 18 videos clasificados
  - 12 archivos de audio agrupados
```

### Caso de Uso 2: Archivo Fotográfico

**Escenario:** Organizar fotos de varios años por fecha

```bash
python organizador_archivos.py
# Opción: 2
# Ruta: D:/Fotos

✓ Organización por fecha completada!
  Estructura creada: 2020-2025 / Mes
```

---

## 🛠️ Personalización

### Agregar Nuevas Categorías

Edita el diccionario `CATEGORIAS` en el código:

```python
CATEGORIAS = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'TuCategoria': ['.ext1', '.ext2', '.ext3'],  # ← Agrega aquí
}
```

### Cambiar Formato de Fecha

Modifica la línea de formato de fecha:

```python
# Formato actual: "01 - January"
mes = fecha.strftime('%m - %B')

# Otras opciones:
mes = fecha.strftime('%B')           # "January"
mes = fecha.strftime('%m')           # "01"
mes = fecha.strftime('%Y-%m')        # "2025-01"
```

---

## ⚠️ Consideraciones Importantes

### ✅ Seguridad
- El script **mueve** archivos (no los copia), así que asegúrate de tener respaldo
- Solo trabaja en el directorio que especifiques
- No modifica archivos, solo los reorganiza

### 🔒 Recomendaciones
- Prueba primero en una carpeta de prueba
- Haz respaldo de archivos importantes
- Revisa la estructura de carpetas generada

### 📝 Limitaciones
- No funciona con archivos en uso
- Requiere permisos de escritura en el directorio
- Los archivos con nombres duplicados pueden sobrescribirse

---

## 🗺️ Roadmap

Funcionalidades planeadas para futuras versiones:

- [ ] Organización por tamaño de archivo
- [ ] Interfaz gráfica (GUI)
- [ ] Modo "observador" (organiza automáticamente archivos nuevos)
- [ ] Filtros personalizables
- [ ] Función de deshacer cambios
- [ ] Registro de operaciones (logs)
- [ ] Organización por contenido (OCR, metadatos)
- [ ] Detección de duplicados
- [ ] Compresión automática de archivos grandes

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres mejorar este proyecto:

1. Haz un **Fork** del repositorio
2. Crea tu rama de características (`git checkout -b feature/NuevaCaracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un **Pull Request**

### Ideas de Contribución
- Nuevas categorías de archivos
- Mejoras en el menú interactivo
- Soporte para más idiomas
- Optimización del rendimiento
- Documentación adicional

---

## 📊 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| `pathlib` | Manejo moderno de rutas |
| `shutil` | Mover archivos entre directorios |
| `datetime` | Procesamiento de fechas |
| `os` | Operaciones del sistema operativo |

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License - Eres libre de usar, modificar y distribuir este software
```

---

## 👨‍💻 Autor

**Juan Jose Sanchez Aguirre**

- 🌐 Portfolio: [portafolio juan jose](https://josedeveloper96.github.io/portafolio.github.io/)
- 💼 LinkedIn: [juan jose sanchez aguirre](https://linkedin.com/in/tu-usuario)
- 🐙 GitHub: [@josedeveloper96](https://github.com/josedeveloper96)
- 📧 Email: juanzxable@gmail.com

---

## 🙏 Agradecimientos

- Inspirado en la necesidad de mantener organizadas las carpetas de descargas
- Gracias a la comunidad de Python por las excelentes bibliotecas
- A todos los que contribuyan a mejorar este proyecto

---

## 📈 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/organizador-archivos?style=social)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/organizador-archivos?style=social)
![GitHub issues](https://img.shields.io/github/issues/tu-usuario/organizador-archivos)

---

<div align="center">

**⭐ Si este proyecto te fue útil, dale una estrella! ⭐**

Hecho con ❤️ y ☕ por [Tu Nombre]

</div>

