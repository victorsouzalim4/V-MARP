import lmdb

def store_file_data(db_path, file_path, file_authorization):
    """Armazena os caminhos dos arquivos e suas autorizações no banco LMDB."""
    env = lmdb.open(db_path, map_size=10**9)  # Define um tamanho máximo de 1GB para o banco

    with env.begin(write=True) as txn:
        txn.put(file_path.encode(), str(file_authorization).encode())  # Converte os dados para bytes

def get_file_authorization(db_path, file_path):
    """Recupera a autorização de um arquivo específico com base na chave (caminho do arquivo)."""
    env = lmdb.open(db_path, readonly=True)

    with env.begin() as txn:
        value = txn.get(file_path.encode())  # Recupera o valor associado à chave
    
    return value.decode() if value else None  # Retorna a autorização ou None se a chave não existir