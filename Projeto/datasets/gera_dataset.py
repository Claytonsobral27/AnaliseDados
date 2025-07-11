import random 
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd 
from faker import Faker



pasta_datasets = Path(__file__).parent / "datasets" #Caminho do projeto

pasta_datasets.mkdir(parents=True, exist_ok=True) #valida se a pasta existe .

LOJAS = [
 
            {"estado": "SP" , "cidade": "São paulo", 
            "vendedores":["Ana Oliveira", "Lucas Pereira"]},
             {"estado": "MG" , "cidade": "Belo Horizonte", 
            "vendedores":["Carlos Silva", "Fernanda Costa"]},
             {"estado": "RJ" , "cidade": "Rio de Janeiro", 
            "vendedores":["Juliana Almeida", "Pedro Souza"]},
             {"estado": "RS" , "cidade": "Porto Alegre", 
            "vendedores":["Mariana Gomes", "Roberto Ferreira"]},
             {"estado": "SC" , "cidade": "FLorianópolis", 
            "vendedores":["Gabriela Santos", "Tiago lima"]},
            
]

PRODUTOS =[
          

        {"Nome:": "Smartphone Samsung Galaxy", "id": 0 , "preco":25000},
        {"Nome:": "Nootbook Dell Inspiron", "id": 1 , "preco":4500},
        {"Nome:": "Table Apple ipad", "id": 2 , "preco":3000},
        {"Nome:": "Smartwatch", "id":3 , "preco":12000},
        {"Nome:": "Fone de Ouvido Sony", "id": 4 , "preco":600},
        {"Nome:": "Cabo USB-C", "id": 5 , "preco":100},



]

FORMA_PAGTO =["cartão de crédito", "boleto", "pix" , "dinheiro"]

GENERO = ["male", "female", "outro"]

compras = []


for _ in range(2000):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)
    hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )

    genero_cliente = random.choice(GENERO)
    genero_nome = genero_cliente if genero_cliente in ["male", "female"] else random.choice(["male", "female"])
   

fake = Faker('pt_BR')

genero_nome = 'masculino'  # ou 'feminino'

if genero_nome == 'masculino':
    nome_cliente = f"{fake.first_name_male()} {fake.last_name()}"
elif genero_nome == 'feminino':
    nome_cliente = f"{fake.first_name_female()} {fake.last_name()}"
else:
    nome_cliente = fake.name()  # aleatório

print(nome_cliente)



forma_pagamento = random.choice(FORMA_PAGTO)

compras.append({
        "data": hora_compra,
        "id_compra": 0,
        "loja": loja["cidade"],
        "vendedor": vendedor,
        "produto": produto["Nome:"],
        "cliente_nome": nome_cliente,
        "cliente_genero": genero_cliente.replace("female", "feminino").replace("male", "masculino"),
        "forma_pagamento": forma_pagamento
    })




df_compras = pd.DataFrame(compras).set_index("data").sort_index()
df_compras["id_compra"] = [i for i in range(len(df_compras))]



df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)

print(df_compras)
