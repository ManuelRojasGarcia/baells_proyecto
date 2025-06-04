"""
Módulo: ejercicio1

Este módulo muestra un análisis exploratorio básico de los datos del embalse La Baells.

Autor: Manuel Rojas García
"""

def mostrar_eda(df):
    """
    Muestra un análisis exploratorio básico del DataFrame del embalse.

    Incluye:
    - Nombres de columnas
    - Primeras cinco filas del conjunto de datos
    - Información general del DataFrame (tipos de datos y nulos)

    Args:
        df (pandas.DataFrame): DataFrame con los datos del embalse.
    """
    print("Columnas disponibles en el conjunto de datos:")
    print(df.columns.tolist())

    print("\n Primeras 5 filas del DataFrame:")
    print(df.head())

    print("\n Resumen general del DataFrame:")
    df.info()
