import pandas as pd
from src.modules.ejercicio5 import calcula_periodos

def test_calcula_periodos():
    dias = pd.Series([2020.1, 2020.2, 2020.3, 2020.4, 2020.5])
    valores = [55, 45, 42, 65, 70]
    periodos = calcula_periodos(dias, valores, umbral=60)
    assert isinstance(periodos, list)
    assert len(periodos) >= 1
