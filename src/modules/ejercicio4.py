"""
Módulo: ejercicio4

Este módulo genera una gráfica comparativa entre el volumen embalsado original
y una señal suavizada usando el filtro de Savitzky-Golay.

Autor: Manuel Rojas García
"""

import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter

def graficar_volumen_suavizado(df, nombre_alumno):
    """
    Genera una gráfica comparando la señal original y una versión suavizada del volumen embalsado.

    - Ordena los datos por fecha.
    - Aplica suavizado con filtro Savitzky-Golay.
    - Genera una gráfica con título personalizado.
    - Guarda la imagen en la carpeta 'img'.

    Args:
        df (pd.DataFrame): DataFrame con columna 'nivell_perc' y 'dia'.
        nombre_alumno (str): Nombre del alumno que aparecerá en la gráfica.

    Returns:
        np.ndarray: Señal suavizada.
    """
    if not os.path.exists("img"):
        os.makedirs("img")

    df = df.sort_values("dia")
    df["nivell_perc"] = pd.to_numeric(df["nivell_perc"], errors="coerce")
    df = df.dropna(subset=["nivell_perc"])

    # Señal original
    y = df["nivell_perc"].values

    # Señal suavizada con Savgol
    y_smooth = savgol_filter(y, window_length=1500, polyorder=3)

    plt.figure(figsize=(12, 6))
    plt.plot(df["dia"], y, label="Original", alpha=0.5)
    plt.plot(df["dia"], y_smooth, label="Suavizado", linewidth=2)
    plt.title("Volumen embalsado: señal original y suavizada")
    plt.xlabel("Fecha")
    plt.ylabel("Porcentaje de volumen (%)")
    plt.legend()
    plt.grid(True)
    plt.suptitle(nombre_alumno, fontsize=10, y=0.93)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"img/labaells_smoothed_{nombre_alumno.lower().replace(' ', '_')}.png")
    plt.close()

    return y_smooth
