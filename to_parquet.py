from pathlib import Path
import pandas as pd


def convert_csv_to_parquet(
    source_dir: Path = Path("data_subte"),
    target_dir: Path = Path("data_parquet"),
) -> None:
    """Convierte todos los CSV de `source_dir` a archivos Parquet en `target_dir`."""
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    if not source_dir.exists():
        print(f"[ERROR] No existe la carpeta de origen: {source_dir}")
        return

    csv_files = sorted(source_dir.glob("*.csv"))

    if not csv_files:
        print(f"[INFO] No se encontraron archivos CSV en: {source_dir}")
        return

    target_dir.mkdir(parents=True, exist_ok=True)

    converted = 0
    failed = 0

    print(f"[INFO] Se encontraron {len(csv_files)} CSV para convertir.")

    for csv_path in csv_files:
        parquet_path = target_dir / f"{csv_path.stem}.parquet"
        try:
            if "2021" in csv_path.stem:
                df = pd.read_csv(csv_path, delimiter=";", encoding="latin-1")
            else:
                df = pd.read_csv(csv_path, encoding="latin-1")
            
            if "historico_2" in csv_path.stem:
                df = df.sample(frac=0.2, random_state=42)
                            
            df.to_parquet(parquet_path, index=False)
            converted += 1
            print(f"[OK] {csv_path.name} -> {parquet_path.name}")
        except Exception as exc:
            failed += 1
            print(f"[ERROR] No se pudo convertir '{csv_path.name}': {exc}")

    print("\n[RESUMEN]")
    print(f"Convertidos: {converted}")
    print(f"Fallidos:    {failed}")
    print(f"Salida:      {target_dir.resolve()}")


if __name__ == "__main__":
    convert_csv_to_parquet()


