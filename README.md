# Proyecto Análisis de Datos del Embalse La Baells


## 📊 Descripción

Este proyecto realiza un análisis de datos históricos del embalse **La Baells**, centrándose en la evolución del volumen embalsado a lo largo del tiempo. Se aplican técnicas de:

- Limpieza de datos
- Análisis estadístico
- Visualización gráfica
- Detección de periodos de sequía

---

## 📁 Estructura del Proyecto

```
baells_proyecto/
│
├── src/
│   ├── main.py               # Punto de entrada principal
│   └── modules/
│       ├── cargador_datos.py
│       ├── ejercicio1.py
│       ├── ejercicio2.py
│       ├── ejercicio3.py
│       ├── ejercicio4.py
│       ├── ejercicio5.py
│       └── analisis.py
│
├── tests/                    # Tests unitarios
├── doc/                      # Documentación HTML generada
├── screenshots/              # Capturas de pantalla
├── img/                      # Imágenes generadas
├── README.md                 # Este archivo
├── LICENSE                   # Licencia del proyecto
├── requirements.txt          # Dependencias necesarias
├── .pylintrc                 # Reglas para pylint
└── setup.cfg                 # Configuración para tests y otros
```

---

## ⚙️ Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd baells_proyecto
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
# Activar:
# Windows
.env\Scriptsctivate
# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar análisis

- Todos los ejercicios:

```bash
python src/main.py
```

- Hasta un ejercicio específico (ej. hasta el 3):

```bash
python src/main.py -ex 3
```

- Mostrar ayuda:

```bash
python src/main.py -h
```

---

## 🧪 Testing y Cobertura

- Ejecutar tests:

```bash
pytest tests/
```

- Ejecutar tests con cobertura:

```bash
pytest --cov=src tests/
```

---

## 📸 Resultados

Las capturas de pantalla se encuentran en la carpeta `screenshots/`. Las gráficas generadas se guardan automáticamente en `img/`.

---

## Generación de documentación

La documentación HTML se genera automáticamente a partir de los docstrings de las funciones utilizando la herramienta **pdoc**.

Para generar la documentación, ejecuta el siguiente comando desde la raíz del proyecto:

```bash
pdoc --html src/modules --output-dir doc --force
---

## ✅ Linter

Revisar la calidad del código con pylint:

```bash
pylint src/modules
```

Las reglas están definidas en el archivo `.pylintrc`.

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Ver archivo `LICENSE` para más detalles.

---

## 👤 Autor

**Manuel Rojas García**  
Proyecto académico de análisis y visualización de datos.

---

## ⚠️ Notas Técnicas

- No se deben usar rutas absolutas.
- Toda funcionalidad está organizada modularmente.
- El fichero `main.py` gestiona la ejecución de los ejercicios.
- Las imágenes generadas se almacenan en la carpeta `img/`.
