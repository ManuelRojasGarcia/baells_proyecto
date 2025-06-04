"""
Módulo: ejercicio2

Este módulo limpia y filtra los datos del embalse La Baells
aplicando renombrado de columnas, normalización y filtrado por nombre.

Autor: Manuel Rojas García
"""

import pandas as pd

def ejercicio2_filtrado_y_limpieza(df):
    """
    Limpia y filtra el DataFrame según el ejercicio 2:
    - Renombra columnas al formato estándar.
    - Muestra valores únicos en la columna 'estacio'.
    - Normaliza nombres de embalses con expresiones regulares.
    - Filtra solo datos del embalse La Baells.
    - Convierte columnas a tipos adecuados.
    - Elimina filas con datos faltantes en 'volum' y 'dia'.
    
    Args:
        df (pd.DataFrame): DataFrame original con datos crudos.
        
    Returns:
        pd.DataFrame: DataFrame limpio y filtrado solo con La Baells.
    """
    renombrar = {
        "Dia": "dia",
        "Estació": "estacio",
        "Nivell absolut (msnm)": "nivell_msnm",
        "Percentatge volum embassat (%)": "nivell_perc",
        "Volum embassat (hm3)": "volum",
        "Fecha": "dia",  
        "Embalse": "estacio",
        "Nivel": "nivell_msnm",
        "Porcentaje": "nivell_perc",
        "Volumen": "volum"
    }

    # Renombrar solo las columnas existentes
    df = df.rename(columns={k: v for k, v in renombrar.items() if k in df.columns})

    print("Valores únicos en 'estacio':")
    print(df["estacio"].unique())

    # Limpieza nombre embalses con regex
    df["estacio"] = df["estacio"].str.replace(r"Embassament de\s*", "", regex=True)
    df["estacio"] = df["estacio"].str.replace(r"\s*\(.*\)", "", regex=True).str.strip()

    # Filtrado solo La Baells
    df_baells = df[df["estacio"].str.contains("Baells", case=False, na=False)].copy()

    # Convertir columnas a tipo adecuado
    df_baells["volum"] = pd.to_numeric(df_baells["volum"], errors="coerce")
    df_baells["dia"] = pd.to_datetime(df_baells["dia"], errors="coerce", dayfirst=True)
    df_baells = df_baells.dropna(subset=["volum", "dia"])

    return df_baells
