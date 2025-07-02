# V-MARP - Victor’s Mapping Algorithm with Recursive Pruning

**V-MARP** (Victor’s Mapping Algorithm with Recursive Pruning) é um algoritmo de varredura e compactação de diretórios baseado em duas passagens de busca em profundidade (*DFS*), utilizando validações armazenadas em banco de dados **LMDB** para aplicar **poda lógica** em diretórios validados.

---

## 🧠 Visão Geral do Algoritmo

O V-MARP opera em duas etapas principais:

### 🔹 Etapa 1: Varredura e Validação Inferida (Pré-processamento)
- Realiza uma **busca em profundidade (DFS)** completa na árvore de diretórios.
- Cada **folha** (arquivo ou diretório sem filhos) é validada com base na **data limite**.
- A validação de **diretórios internos** é **inferida**: um diretório é considerado válido **somente se todos os seus filhos forem válidos**.
- As validações são armazenadas em banco de dados **LMDB**, associadas ao caminho completo de cada item.

### 🔹 Etapa 2: Varredura com Poda Lógica
- Realiza uma segunda DFS utilizando os dados persistidos no LMDB.
- Quando encontra um **diretório validado**, o algoritmo o **compacta diretamente** e **ignora seus filhos**, aplicando **poda lógica recursiva**.
- Isso acelera consideravelmente a análise em grandes estruturas hierárquicas.

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.8+
- [LMDB](https://pypi.org/project/lmdb/)
- Permissões de leitura no diretório alvo

### Instalação

```bash
git clone https://github.com/victorsouzalim4/V-MARP.git
cd V-MARP
pip install -r requirements.txt
```

### Execução

Configure o diretório e a data de corte em `main.py`:

```python
dir = '[SEU DIRETORIO]'
date = datetime.strptime("2024-01-01", "%Y-%m-%d").date()
```

Execute:

```bash
python main.py
```

Saídas geradas:
- `output.txt`: estrutura dos diretótios
- `file_mapping.lmdb`: banco de validações persistidas

---

## 📁 Estrutura do Projeto

```
V-MARP/
│
├── Utils/
│   ├── tree_scanner.py       # Etapa 1: DFS com validação e retropropagação
│   ├── DFS_Zip.py            # Etapa 2: DFS com poda lógica e compactação
│   └── data_base_function.py # Funções de acesso ao LMDB
│
├── main.py                   # Ponto de entrada da aplicação
├── requirements.txt
├── output.txt
└── README.md
```

---

## ✅ Funcionalidades

- ✅ Validação recursiva de diretórios com backtracking
- ✅ Armazenamento eficiente com LMDB
- ✅ Poda lógica na segunda varredura
- ✅ Suporte a arquivos compactados (.zip)
- ✅ Modularização clara

---

## 🛠️ Melhorias Futuras

- Interface CLI com `argparse`
- Logs estruturados com `logging`
- Exportação em JSON ou CSV
- Execução paralela em grandes volumes
- Interface Web ou dashboard local

---

## 📄 Licença

Este projeto é de código aberto e está licenciado sob os termos da **MIT License**.
