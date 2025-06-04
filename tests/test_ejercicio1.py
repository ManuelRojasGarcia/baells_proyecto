import pandas as pd
from src.modules.ejercicio1 import mostrar_eda

def test_mostrar_eda(capsys):
    df = pd.DataFrame({
        'col1': [1, 2, 3],
        'col2': [4, 5, 6]
    })
    mostrar_eda(df)
    captured = capsys.readouterr()
    assert "Columnas disponibles" in captured.out
