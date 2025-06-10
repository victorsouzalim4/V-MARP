import lmdb

def store_file_data(db_path, file_path, file_authorization):
    """
    Armazena os caminhos dos arquivos e suas autorizações no banco LMDB.
    O valor é armazenado como b'1' (True) ou b'0' (False).
    """
    env = lmdb.open(db_path, map_size=10**9)  # Até 1GB de banco

    with env.begin(write=True) as txn:
        value = b"1" if file_authorization else b"0"
        txn.put(file_path.encode(), value)

def get_file_authorization(db_path, file_path):
    """
    Recupera a autorização de um arquivo específico.
    Retorna True se autorizado, False se não, ou None se a chave não existir.
    """
    env = lmdb.open(db_path, readonly=True)

    with env.begin() as txn:
        value = txn.get(file_path.encode())

    if value is None:
        return None
    return value == b"1"