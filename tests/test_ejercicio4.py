import pandas as pd
from src.modules.ejercicio4 import graficar_volumen_suavizado

def test_graficar_volumen_suavizado(tmp_path):
    df = pd.DataFrame({
        "dia": pd.date_range(start="2020-01-01", periods=1600, freq="D"),
        "nivell_perc": [40 + (i % 10) for i in range(1600)]
    })
    valores = graficar_volumen_suavizado(df, "Test Alumno")
    assert len(valores) == 1600
