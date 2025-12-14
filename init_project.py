import os

# ==============================
# CARPETAS DEL PROYECTO
# ==============================
folders = [
    "data",
    "data/processed",          # raw se genera con downloader.py

    "notebooks",

    "src/data",
    "src/training",

    "models",

    "test"                     # para predict.py
]

# ==============================
# ARCHIVOS DEL PROYECTO
# ==============================
files = [
    "notebooks/CNNriesgo.ipynb",

    "src/data/downloader.py",
    "src/data/preprocess.py",
    "src/data/split.py",

    "src/training/train.py",

    "test/predict.py",

    "requirements.txt",
    ".env",
    ".gitignore",
    "README.md"
]

# ==============================
# CREAR ESTRUCTURA
# ==============================
def create_structure():
    # Crear carpetas
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Crear archivos vacíos
    for file in files:
        dir_name = os.path.dirname(file)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        if not os.path.exists(file):
            open(file, "w", encoding="utf-8").close()

    print("✅ Estructura del proyecto CNN creada correctamente")

if __name__ == "__main__":
    create_structure()
