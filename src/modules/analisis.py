"""
Módulo: analisis

Este módulo forma parte del análisis de datos del embalse La Baells.

Autor: Manuel Rojas García
"""

import pandas as pd

def volumen_medio(datos):
    """
    Calcula el volumen medio a partir de la columna 'Volumen'.

    Args:
        datos (pd.DataFrame): DataFrame con una columna 'Volumen'.

    Returns:
        float: Volumen medio calculado.
    """
    return datos["Volumen"].astype(float).mean()

def volumen_por_anio(datos):
    """
    Agrupa el DataFrame por año y calcula el volumen medio por año.

    Args:
        datos (pd.DataFrame): DataFrame con columnas 'Fecha' y 'Volumen'.

    Returns:
        pd.Series: Volumen medio por año.
    """
    datos["Año"] = datos["Fecha"].dt.year
    datos["Volumen"] = pd.to_numeric(datos["Volumen"], errors="coerce")
    return datos.groupby("Año")["Volumen"].mean()

def volumen_maximo_minimo(datos):
    """
    Obtiene el volumen máximo y mínimo a partir de la columna 'Volumen'.

    Args:
        datos (pd.DataFrame): DataFrame con columna 'Volumen'.

    Returns:
        tuple: Volumen máximo y mínimo como (max, min).
    """
    volumenes = pd.to_numeric(datos["Volumen"], errors="coerce")
    return volumenes.max(), volumenes.min()
