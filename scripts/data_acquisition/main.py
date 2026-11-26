"""Carga del conjunto de datos METABRIC desde Kaggle.

Descarga el archivo "Breast Cancer METABRIC.csv" del dataset
gunesevitan/breast-cancer-metabric con kagglehub, valida su estructura
y lo guarda en data/raw/metabric.csv.

Uso (desde la raíz del repositorio):
    pip install "kagglehub[pandas-datasets]"
    python scripts/data_acquisition/main.py
"""

from pathlib import Path

import kagglehub
from kagglehub import KaggleDatasetAdapter

DATASET = "gunesevitan/breast-cancer-metabric"
ARCHIVO = "Breast Cancer METABRIC.csv"

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "data" / "raw" / "metabric.csv"

COLUMNAS_OBJETIVO = ["Overall Survival (Months)", "Overall Survival Status"]


def cargar_datos():
    """Descarga el CSV desde Kaggle y lo devuelve como DataFrame."""
    return kagglehub.dataset_load(KaggleDatasetAdapter.PANDAS, DATASET, ARCHIVO)


def validar(df):
    """Verifica que los datos tengan la estructura esperada."""
    faltantes = [c for c in COLUMNAS_OBJETIVO + ["Patient ID"] if c not in df.columns]
    if faltantes:
        raise ValueError(f"Faltan columnas en el archivo descargado: {faltantes}")
    if df["Patient ID"].duplicated().any():
        raise ValueError("Hay identificadores de paciente duplicados.")


def resumen(df):
    """Imprime un resumen corto de los datos cargados."""
    con_objetivo = df.dropna(subset=COLUMNAS_OBJETIVO)
    tasa_eventos = (con_objetivo["Overall Survival Status"] == "Deceased").mean()

    print(f"Registros: {df.shape[0]} | Variables: {df.shape[1]}")
    print(f"Pacientes con tiempo y estado de supervivencia: {len(con_objetivo)}")
    print(f"Tasa de eventos (muerte): {tasa_eventos:.1%}")
    print("\nVariables con más datos faltantes (%):")
    print((df.isna().mean() * 100).sort_values(ascending=False).head(5).round(2).to_string())


def main():
    df = cargar_datos()
    validar(df)
    resumen(df)

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SALIDA, index=False)
    print(f"\nDatos guardados en: {SALIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()