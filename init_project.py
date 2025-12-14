import os

folders = [
    "data/raw/tortuga",
    "data/raw/catarina",
    "data/raw/hormiga",
    "data/raw/gato",
    "data/raw/perro",

    "data/processed/train",
    "data/processed/val",
    "data/processed/test",

    "notebooks",

    "src/data",
    "src/models",
    "src/training",
    "src/evaluation",

    "models",
    "results"
]

files = [
    "notebooks/CNNriesgo.ipynb",

    "src/config.py",

    "src/data/downloader.py",
    "src/data/preprocess.py",
    "src/data/split.py",

    "src/models/cnn_model.py",

    "src/training/train.py",

    "src/evaluation/evaluate.py",

    "src/predict.py",

    "models/best_model.h5",
    "results/metrics.txt",

    "requirements.txt",
    ".env",
    ".gitignore",
    "README.md"
]

def create_structure():
    # Crear carpetas
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Crear archivos vacíos
    for file in files:
        dir_name = os.path.dirname(file)
        if dir_name:  # ← CLAVE: solo si hay directorio
            os.makedirs(dir_name, exist_ok=True)

        if not os.path.exists(file):
            open(file, "w").close()

    print("✅ Estructura del proyecto CNN creada correctamente")

if __name__ == "__main__":
    create_structure()
