import argparse
import pandas as pd
from modules.cargador_datos import cargar_datos
from modules.ejercicio1 import mostrar_eda
from modules.ejercicio2 import ejercicio2_filtrado_y_limpieza
from modules.ejercicio3 import ejecutar_analisis_temporal
from modules.ejercicio4 import graficar_volumen_suavizado
from modules.ejercicio5 import guardar_resultados, calcula_periodos

def main():
    parser = argparse.ArgumentParser(description="Ejecuta los ejercicios del proyecto.")
    parser.add_argument('-ex', '--ejercicio', type=int, help='Número de ejercicio hasta el que ejecutar (1-5)')
    args = parser.parse_args()

    df = cargar_datos()

    hasta = args.ejercicio if args.ejercicio else 5

    if hasta >= 1:
        print("=== EJERCICIO 1 ===")
        mostrar_eda(df)

    if hasta >= 2:
        print("\n=== EJERCICIO 2 ===")
        df_filtrado = ejercicio2_filtrado_y_limpieza(df)
        print(df_filtrado.head())
    else:
        df_filtrado = None

    if hasta >= 3:
        print("\n=== EJERCICIO 3 ===")
        if df_filtrado is None:
            df_filtrado = ejercicio2_filtrado_y_limpieza(df)
        ejecutar_analisis_temporal(df_filtrado, "Manuel Rojas Garcia")

    if hasta >= 4:
        print("\n=== EJERCICIO 4 ===")
        if df_filtrado is None:
            df_filtrado = ejercicio2_filtrado_y_limpieza(df)
        valores_suavizados = graficar_volumen_suavizado(df_filtrado, "Manuel Rojas Garcia")

    if hasta >= 5:
        print("\n=== EJERCICIO 5 ===")
        if df_filtrado is None:
            df_filtrado = ejercicio2_filtrado_y_limpieza(df)

        guardar_resultados(df_filtrado, "Manuel Rojas Garcia")

        # Asegurarse de que 'dia' está en formato datetime
        df_filtrado['dia'] = pd.to_datetime(df_filtrado['dia'], errors='coerce', dayfirst=True)

        # Convertir fechas a formato decimal
        from modules.ejercicio3 import toYearFraction
        dias_decimal = df_filtrado['dia'].map(toYearFraction)

        # Detectar periodos de sequía
        periodos = calcula_periodos(dias_decimal, valores_suavizados)
        
        print("\nPeriodos de sequía detectados (valores decimales):")
        for i, periodo in enumerate(periodos, start=1):
            print(f"  Periodo {i}: {periodo[0]:.2f} a {periodo[1]:.2f}")

        # Guardar resultados en CSV
        import csv, os
        os.makedirs("resultados", exist_ok=True)
        with open("resultados/periodos_sequia.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Inicio (decimal)", "Fin (decimal)"])
            writer.writerows(periodos)
        print("\nPeriodos de sequía guardados en 'resultados/periodos_sequia.csv'")

if __name__ == "__main__":
    main()