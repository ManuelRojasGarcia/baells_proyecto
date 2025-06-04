"""
Módulo: cargador_datos

Este módulo permite cargar datos del embalse La Baells desde un archivo CSV local.

Autor: Manuel Rojas García
"""

import os
import pandas as pd

RUTA_LOCAL = "datos/baells.csv"

def cargar_datos(ruta_local: str = RUTA_LOCAL) -> pd.DataFrame:
    """
    Carga los datos del embalse de La Baells desde un archivo CSV local.

    Args:
        ruta_local (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos del embalse.
    """
    if not os.path.exists(ruta_local):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_local}")

    # Separador como punto y coma
    df = pd.read_csv(ruta_local, sep=";", encoding="utf-8", on_bad_lines="skip")

    # Verifica las columnas
    print("Columnas encontradas:", df.columns)

    # Normalizamos el nombre si es necesario
    if "Estació" in df.columns:
        df = df[df["Estació"].str.contains("la Baells", case=False, na=False)]
    else:
        # Si hay solo una columna mal importada, dividirla
        df = pd.read_csv(ruta_local, sep=",", header=None, encoding="utf-8", on_bad_lines="skip")
        df.columns = ["Fecha", "Embalse", "Nivel", "Porcentaje", "Volumen"]
        df = df[df["Embalse"].str.contains("la Baells", case=False, na=False)]
        df["Fecha"] = pd.to_datetime(df["Fecha"], dayfirst=True)

    return df
