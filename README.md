<h1 align="center">Algoritmo de indexação de documentos</h1>

## Sobre o projeto

Foram desenvolvidos 2 módulos Python:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato *TXT*) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

## Tecnologias utilizadas

- [Python](https://www.python.org/) - Linguagem de programação interpretada de alto nível.
- [Pytest](https://docs.pytest.org/en/7.2.x/) - Framework de testes em Python.

## Funcionalidades

- Manipular arquivos de texto;
- Identificar ocorrências de termos nos arquivos.

## Instalação

```bash
# Clonar Projeto
$ git clone git@github.com:lucas-da-silva/google-algorithm.git

# Entrar no diretório
$ cd google-algorithm

# Criar ambiente virtual e ativá-lo
$ python3 -m venv .venv && source .venv/bin/activate

# Instalar dependências
$ python3 -m pip install -r dev-requirements.txt

# Executar testes
$ python3 -m pytest
```

## Estrutura do projeto

```
$PROJECT_ROOT
|   # Arquivos estáticos para documentos
├── statics
|   # Arquivos de testes
├── tests
|   |   # Testes da classe PriorityQueue
|   └── priority_queue
|   # Módulo de gerenciamento de arquivos
├── ting_file_management
|   # Módulo de busca de palavras em documentos
└── ting_word_searches
```

## Autor

- [@lucas-da-silva](https://github.com/lucas-da-silva)
