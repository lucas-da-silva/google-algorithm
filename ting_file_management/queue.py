from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self) -> None:
        self._data = list()

    def __len__(self) -> int:
        return len(self._data)

    def enqueue(self, value) -> None:
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index: int):
        if index < 0 or index >= len(self):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
