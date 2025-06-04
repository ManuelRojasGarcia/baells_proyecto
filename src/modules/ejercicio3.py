"""
Módulo: ejercicio3

Este módulo realiza un análisis temporal y gráfico del porcentaje de volumen embalsado.

Autor: Manuel Rojas García
"""

import os
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

# pylint: disable=invalid-name
def toYearFraction(date: datetime) -> float:
    """
    Convierte una fecha datetime a su representación decimal de año.
    Por ejemplo, 1 de julio de 2025 ≈ 2025.5

    Args:
        date (datetime): Fecha a convertir.

    Returns:
        float: Año en formato decimal.
    """
    year_start = datetime(year=date.year, month=1, day=1)
    year_end = datetime(year=date.year + 1, month=1, day=1)
    year_elapsed = (date - year_start).total_seconds()
    year_duration = (year_end - year_start).total_seconds()
    fraction = year_elapsed / year_duration
    return date.year + fraction

def ejecutar_analisis_temporal(df: pd.DataFrame, nombre_alumno: str) -> None:
    """
    Ejecuta análisis temporal del volumen embalsado para el ejercicio 3.

    Pasos realizados:
    - Convierte la columna 'dia' a datetime y ordena el dataframe por fecha.
    - Limpia y convierte la columna 'nivell_perc' a numérica, eliminando valores no convertibles.
    - Agrupa los datos por mes calculando la media del porcentaje embalsado.
    - Muestra número de datos, fecha más antigua y más reciente.
    - Genera y guarda un gráfico con la evolución mensual del porcentaje de volumen embalsado.
    - El gráfico tiene título y subtítulo con el nombre del alumno.

    Args:
        df (pd.DataFrame): DataFrame limpio y filtrado.
        nombre_alumno (str): Nombre completo del alumno para el subtítulo y archivo.
    """
    # Crear carpeta img si no existe
    if not os.path.exists("img"):
        os.makedirs("img")

    # Convertir columna 'dia' a datetime
    df['dia'] = pd.to_datetime(df['dia'], errors='coerce', dayfirst=True)
    df = df.dropna(subset=['dia'])
    df = df.sort_values('dia')

    # Mostrar info
    n_datos = len(df)
    fecha_min = df['dia'].iloc[0]
    fecha_max = df['dia'].iloc[-1]
    print(f"Número de datos: {n_datos}")
    print(f"Fecha más antigua: {fecha_min.strftime('%Y-%m-%d')}")
    print(f"Fecha más reciente: {fecha_max.strftime('%Y-%m-%d')}")

    # Asegurar que 'nivell_perc' es numérica y limpiar NaNs
    df['nivell_perc'] = pd.to_numeric(df['nivell_perc'], errors='coerce')
    df = df.dropna(subset=['nivell_perc'])

    # Agrupar por mes y calcular media
    df_monthly = df.set_index('dia').resample('ME')['nivell_perc'].mean().reset_index()

    # Crear gráfico
    plt.figure(figsize=(12, 6))
    plt.plot(df_monthly['dia'], df_monthly['nivell_perc'], marker='o', linestyle='-', markersize=4)

    # Título y etiquetas
    plt.suptitle(nombre_alumno, fontsize=10, y=0.95)
    plt.title("Evolución del porcentaje del volumen del embalse La Baells", pad=20)
    plt.xlabel("Fecha")
    plt.ylabel("Porcentaje de volumen (%)")

    # Configurar ticks y grid
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0, 0, 1, 0.9])

    # Guardar gráfico
    nombre_formateado = nombre_alumno.lower().replace(' ', '_')
    plt.savefig(f"img/labaells_{nombre_formateado}.png")
    plt.close()
