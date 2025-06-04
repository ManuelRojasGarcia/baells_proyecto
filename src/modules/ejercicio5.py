"""
Módulo: ejercicio5

Este módulo guarda los resultados del análisis en archivos CSV y
detecta periodos de sequía en los datos suavizados.

Autor: Manuel Rojas García
"""

import os
import pandas as pd

def calcula_periodos(dias_decimal, valores_suavizados, umbral=60):
    """
    Calcula periodos donde valores_suavizados está por debajo del umbral.

    Args:
        dias_decimal (pd.Series o list): Lista con fechas en valor decimal.
        valores_suavizados (list or array): Valores suavizados (porcentaje).
        umbral (float): Umbral para definir sequía (por defecto 60%).

    Returns:
        List[List[float]]: Lista de periodos [inicio, fin] en valores decimales.
    """
    periodos = []
    inicio = None

    for i, valor in enumerate(valores_suavizados):
        if valor < umbral:
            if inicio is None:
                if hasattr(dias_decimal, 'iloc'):
                    inicio = dias_decimal.iloc[i]
                else:
                    inicio = dias_decimal[i]
        else:
            if inicio is not None:
                if hasattr(dias_decimal, 'iloc'):
                    fin = dias_decimal.iloc[i - 1]
                else:
                    fin = dias_decimal[i - 1]
                periodos.append([inicio, fin])
                inicio = None

    if inicio is not None:
        if hasattr(dias_decimal, 'iloc'):
            fin = dias_decimal.iloc[-1]
        else:
            fin = dias_decimal[-1]
        periodos.append([inicio, fin])

    return periodos

def guardar_resultados(df: pd.DataFrame, ruta: str = "resultados"):
    """
    Guarda el DataFrame limpio y su resumen estadístico en archivos CSV.

    Args:
        df (pd.DataFrame): DataFrame con los datos limpios a guardar.
        ruta (str): Directorio donde se guardarán los archivos (por defecto "resultados").
    """
    try:
        os.makedirs(ruta, exist_ok=True)

        # Guardar CSV limpio
        ruta_csv = os.path.join(ruta, "baells_limpio.csv")
        df.to_csv(ruta_csv, index=False)
        print(f"Archivo CSV limpio guardado en: {ruta_csv}")

        # Guardar resumen estadístico
        resumen = df.describe(include="all")
        ruta_resumen = os.path.join(ruta, "resumen_estadistico.csv")
        resumen.to_csv(ruta_resumen)
        print(
            f"Resumen estadístico guardado en: {ruta_resumen}"
        )

    except OSError as e:
        print(f"Error guardando resultados: {e}")
