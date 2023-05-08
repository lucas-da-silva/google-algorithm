from ting_file_management.queue import Queue


def build_file_occurrences(
    file: dict, word: str, include_content=False
) -> dict | None:
    file_occurrences = {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": [
            {"linha": index + 1, "conteudo": line}
            if include_content
            else {"linha": index + 1}
            for index, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ],
    }
    return file_occurrences if file_occurrences["ocorrencias"] else None


def exists_word(word: str, instance: Queue) -> list[dict]:
    files = instance._data
    return list(
        filter(None, [build_file_occurrences(file, word) for file in files])
    )


def search_by_word(word: str, instance: Queue) -> list[dict]:
    files = instance._data
    return list(
        filter(
            None,
            [
                build_file_occurrences(file, word, include_content=True)
                for file in files
            ],
        )
    )
