import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    regular_priority = {
        "nome_do_arquivo": "",
        "qtd_linhas": 5,
        "linhas_do_arquivo": [],
    }
    high_priority = {
        "nome_do_arquivo": "",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [],
    }

    priority_queue.enqueue(regular_priority)
    priority_queue.enqueue(high_priority)
    priority_queue.enqueue(high_priority)
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 2

    removed_file = priority_queue.dequeue()
    assert removed_file == high_priority

    searched_file = priority_queue.search(0)
    assert searched_file == high_priority

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(200)
