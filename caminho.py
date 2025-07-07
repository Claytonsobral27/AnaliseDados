import os 
import shutil 
import subprocess
import datetime as dt

data_atual = dt.datetime.now().strftime("%d-%m-%Y")

origem = r'C:/Users/silvclay/Desktop/' + data_atual
destino = r'C:/Users/silvclay/Desktop/teste'
#caso queira o nome exato do arquivo
#nome_arquivo_desejado = 'arquivo.txt'


print(origem)

# if os.path.exists(origem):
#     arquivos = os.listdir(origem)
#     for arquivo in arquivos:
#         if arquivo.lower().startswith('abd') and arquivo.lower().endswith('.dat'):
#             caminho_arquivo = os.path.join(origem, arquivo)
#             if os.path.isfile(caminho_arquivo):
#                 shutil.copy(caminho_arquivo, destino)
#                 print(f'Arquivo copiado: {arquivo}')
# else:
#     print("Diretório de origem não encontrado.")