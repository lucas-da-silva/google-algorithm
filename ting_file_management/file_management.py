import sys


def txt_importer(path_file: str):
    if not path_file.endswith(".txt"):
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            texts = file.read()
        return texts.split("\n")
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
