import pandas as pd
from src.modules.ejercicio2 import ejercicio2_filtrado_y_limpieza

def test_filtrado_y_limpieza():
    data = {
        "Embalse": ["Embassament de La Baells", "Otro"],
        "Volumen": [50, None],
        "Fecha": ["01/01/2020", None]
    }
    df = pd.DataFrame(data)
    df_filtrado = ejercicio2_filtrado_y_limpieza(df)
    assert not df_filtrado.empty
    assert "volum" in df_filtrado.columns
