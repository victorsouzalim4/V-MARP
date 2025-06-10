import os
import zipfile

def compress_path(path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if os.path.isfile(path):
            # Apenas um arquivo
            zipf.write(path, arcname=os.path.basename(path))
        elif os.path.isdir(path):
            # Diretório inteiro
            for root, dirs, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, start=path)
                    zipf.write(full_path, arcname=relative_path)
        else:
            raise ValueError("O caminho fornecido não é um arquivo nem um diretório.")
