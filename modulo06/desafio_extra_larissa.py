import os
import shutil


def realizar_backup_modulo06():
  
   
    pasta_origem = os.path.dirname(os.path.abspath(__file__))


    pasta_destino = os.path.join(pasta_origem, "backup_arquivos")

    print(f" Pasta de Origem: {pasta_origem}")
    print(f" Pasta de Destino: {pasta_destino}\n")

   # Garante que a pasta de destino seja criada, caso ainda não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Diretório de destino criado em: '{pasta_destino}'")

  
    itens = os.listdir(pasta_origem)

    for item in itens:
        caminho_item_origem = os.path.join(pasta_origem, item)
        caminho_item_destino = os.path.join(pasta_destino, item)

   
        if os.path.isfile(caminho_item_origem):
        
            if item == os.path.basename(__file__):
                continue

            shutil.copy2(caminho_item_origem, caminho_item_destino)
            print(f"✓ Copiado: {item} -> backup_arquivos/")

    print("\n Backup do Módulo 06 concluído com sucesso!")


if __name__ == "__main__":
    realizar_backup_modulo06()