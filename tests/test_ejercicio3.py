import pandas as pd
from src.modules.ejercicio3 import ejecutar_analisis_temporal

def test_ejecutar_analisis_temporal(tmp_path):
    df = pd.DataFrame({
        "dia": ["01/01/2020", "02/01/2020", "03/01/2020"],
        "nivell_perc": [50, 60, 70]
    })
    ejecutar_analisis_temporal(df, "Test Alumno")
    # Se espera que la función guarde un gráfico en img/, no retorna nada
