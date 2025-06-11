import lmdb

def store_file_data(file_path, file_authorization, txn):
    """
    Armazena os caminhos dos arquivos e suas autorizações no banco LMDB.
    O valor é armazenado como b'1' (True) ou b'0' (False).
    """
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