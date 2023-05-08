from ting_file_management.file_management import txt_importer
from ting_file_management.abstract_queue import AbstractQueue


def process(path_file: str, instance: AbstractQueue):
    file_already_added = any(
        data["nome_do_arquivo"] == path_file for data in instance._data
    )
    if not file_already_added:
        texts = txt_importer(path_file)
        text_formatted = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(texts),
            "linhas_do_arquivo": texts,
        }
        instance.enqueue(text_formatted)
        print(text_formatted)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
