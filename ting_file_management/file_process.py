import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue) -> None:
    file_already_added = any(
        file["nome_do_arquivo"] == path_file for file in instance._data
    )
    if not file_already_added:
        file = txt_importer(path_file)
        file_formatted = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(file_formatted)
        print(file_formatted)


def remove(instance: Queue) -> None:
    if not len(instance):
        return print("Não há elementos")
    file_removed = instance.dequeue()
    print(f'Arquivo {file_removed["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance: Queue, position: int) -> None:
    if position > len(instance):
        return print("Posição inválida", file=sys.stderr)
    searched_file = instance.search(position)
    print(searched_file)
