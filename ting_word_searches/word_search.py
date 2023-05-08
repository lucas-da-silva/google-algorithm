from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue) -> list[dict]:
    files = instance._data
    filtered_files = []

    for file in files:
        file_occurrences = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, line in enumerate(file["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }
        if file_occurrences["ocorrencias"]:
            filtered_files.append(file_occurrences)

    return filtered_files


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
