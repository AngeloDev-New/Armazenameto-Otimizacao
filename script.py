import random
from datetime import datetime, timedelta
import os
def get_data_aleatoria():
    inicio = datetime.strptime("2015-01-01", "%Y-%m-%d")
    dias = random.randint(0, 365 * 9)
    data = inicio + timedelta(days=dias)
    return data.strftime("%Y-%m-%d")

nomes = ['Carlos Silva', 'Ana Souza', 'Pedro Oliveira', 'Mariana Costa', 'Lucas Pereira', 'Fernanda Rocha']
numeros = ['45991020304', '45998765432', '45991234567', '45997654321', '45993456789']
dominios = ['gmail', 'hotmail', 'yahoo', 'outlook']

cargos = ["Mecânico", "Atendente", "Gerente", "Auxiliar", "Supervisor"]
descricoes_servicos = ["Troca de óleo", "Alinhamento", "Balanceamento", "Revisão completa", "Troca de pastilhas"]
produtos_list = ["Filtro de óleo", "Pastilha de freio", "Pneu aro 15", "Bateria 60Ah", "Velas de ignição"]
modelos = ["Civic", "Corolla", "Uno", "Gol", "Palio", "Fiesta"]
marcas = ["Honda", "Toyota", "Fiat", "Volkswagen", "Ford"]
status_list = ["aberta", "em andamento", "concluída", "cancelada"]
formas_pagamento = ["dinheiro", "cartao", "pix", "boleto"]

# Geradores infinitos de nomes, números, domínios
def gerar_infinitamente(lista):
    while True:
        yield random.choice(lista)

nome_aleatorio = gerar_infinitamente(nomes)
numero_aleatorio = gerar_infinitamente(numeros)
dominio_aleatorio = gerar_infinitamente(dominios)

def salvar_query_em_arquivo(query, nome_arquivo):
    with open(nome_arquivo, 'a', encoding='utf-8') as f:
        f.write(query + "\n")
id_Cliente = 0
id_Funcionario = 0
id_Servico = 0
def getClientesQuery(qtd):
    global id_Cliente
    query = "INSERT INTO Clientes (id, nome, telefone, email) VALUES\n"
    for i in range(1, qtd + 1):
        nome = next(nome_aleatorio)
        telefone = next(numero_aleatorio)
        email = nome.lower().replace(" ", ".") + f"@{next(dominio_aleatorio)}.com"
        query += f"    ({id_Cliente+i}, '{nome}', '{telefone}', '{email}'),\n"
    id_Cliente+=qtd
    return query.rstrip(',\n') + ';\n'

def getFuncionariosQuery(qtd):
    global id_Funcionario
    query = "INSERT INTO Funcionarios (id, nome, telefone, email, cargo, salario, data_contratacao) VALUES\n"
    for i in range(1, qtd + 1):
        nome = next(nome_aleatorio)
        telefone = next(numero_aleatorio)
        email = nome.lower().replace(" ", ".") + f"@{next(dominio_aleatorio)}.com"
        cargo = random.choice(cargos)
        salario = round(random.uniform(1500, 5000), 2)
        data = get_data_aleatoria()
        query += f"    ({id_Funcionario+i}, '{nome}', '{telefone}', '{email}', '{cargo}', {salario}, '{data}'),\n"
    id_Funcionario+=qtd
    return query.rstrip(',\n') + ';\n'

def getServicosQuery(qtd):
    global id_Servico
    query = "INSERT INTO Servicos (id, descricao, preco_base) VALUES\n"
    for i in range(1, qtd + 1):
        descricao = random.choice(descricoes_servicos)
        preco = round(random.uniform(50, 500), 2)
        query += f"    ({id_Servico+i}, '{descricao}', {preco}),\n"
    id_Servico+=qtd
    return query.rstrip(',\n') + ';\n'
id_Produto=0
def getProdutosQuery(qtd):
    global id_Produto
    query = "INSERT INTO Produtos (id, nome, preco, estoque) VALUES\n"
    for i in range(1, qtd + 1):
        nome = random.choice(produtos_list)
        preco = round(random.uniform(20, 300), 2)
        estoque = random.randint(1, 100)
        query += f"    ({id_Produto+i}, '{nome}', {preco}, {estoque}),\n"
    id_Produto+=qtd
    return query.rstrip(',\n') + ';\n'
id_veiculo=0
def getVeiculosQuery(qtd, max_cliente_id):
    global id_veiculo
    query = "INSERT INTO Veiculos (id, placa, modelo, marca, ano, cliente_id) VALUES\n"
    for i in range(1, qtd + 1):
        placa = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3)) + '-' + ''.join(random.choices("0123456789", k=4))
        modelo = random.choice(modelos)
        marca = random.choice(marcas)
        ano = random.randint(2000, 2023)
        cliente_id = random.randint(1, max_cliente_id)
        query += f"    ({id_veiculo+i}, '{placa}', '{modelo}', '{marca}', {ano}, {cliente_id}),\n"
    id_veiculo+=qtd
    return query.rstrip(',\n') + ';\n'
id_OS = 0
def getOSQuery(qtd, max_funcionario_id, max_veiculo_id):
    global id_OS
    query = "INSERT INTO Ordens_de_Servico (id, data_abertura, data_fechamento, status, funcionario_id, veiculo_id) VALUES\n"
    for i in range(1, qtd + 1):
        abertura = get_data_aleatoria()
        fechamento = get_data_aleatoria()
        status = random.choice(status_list)
        funcionario_id = random.randint(1, max_funcionario_id)
        veiculo_id = random.randint(1, max_veiculo_id)
        query += f"    ({id_OS+i}, '{abertura}', '{fechamento}', '{status}', {funcionario_id}, {veiculo_id}),\n"
    id_OS+=qtd
    return query.rstrip(',\n') + ';\n'

def getFOSQuery(qtd, max_funcionario_id, max_os_id):
    query = "INSERT IGNORE INTO Funcionarios_OS (funcionario_id, os_id) VALUES\n"
    for _ in range(qtd):
        funcionario_id = random.randint(1, max_funcionario_id)
        os_id = random.randint(1, max_os_id)
        query += f"    ({funcionario_id}, {os_id}),\n"
    
    return query.rstrip(',\n') + ';\n'

def getSOSQuery(qtd, max_servico_id, max_os_id):
    query = "INSERT IGNORE INTO Servicos_OS (servico_id, os_id, preco_final) VALUES\n"
    for _ in range(qtd):
        servico_id = random.randint(1, max_servico_id)
        os_id = random.randint(1, max_os_id)
        preco = round(random.uniform(50, 500), 2)
        query += f"    ({servico_id}, {os_id}, {preco}),\n"
    return query.rstrip(',\n') + ';\n'

def getPOSQuery(qtd, max_produto_id, max_os_id):
    query = "INSERT IGNORE INTO Produtos_OS (produto_id, os_id, quantidade) VALUES\n"
    for _ in range(qtd):
        produto_id = random.randint(1, max_produto_id)
        os_id = random.randint(1, max_os_id)
        quantidade = random.randint(1, 10)
        query += f"    ({produto_id}, {os_id}, {quantidade}),\n"
    return query.rstrip(',\n') + ';\n'

def getPagamentosQuery(qtd, max_os_id):
    query = "INSERT IGNORE INTO Pagamentos (os_id, valor_pago, forma_pagamento, data_pagamento) VALUES\n"
    for _ in range(qtd):
        os_id = random.randint(1, max_os_id)
        valor = round(random.uniform(100, 1500), 2)
        forma = random.choice(formas_pagamento)
        data = get_data_aleatoria()
        query += f"    ({os_id}, {valor}, '{forma}', '{data}'),\n"
    return query.rstrip(',\n') + ';\n'
def caststr(chars,i):
    chars_int = len(str(i))
    return ('0'*(chars-chars_int))+str(i)
if __name__ == "__main__":
    qtd_clientes = 50000
    qtd_funcionarios = 1000
    qtd_servicos = 500
    qtd_produtos = 5000
    qtd_veiculos = 120000
    qtd_os = 4000000
    qtd_fos = 8000000
    qtd_sos = 8000000
    qtd_pos = 6000000
    qtd_pagamentos = 4000000
    init = '''
DROP DATABASE IF EXISTS mecanica;
CREATE DATABASE mecanica;
USE mecanica;
SET GLOBAL max_allowed_packet=134217728;

CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(30),
    email VARCHAR(100)
);

CREATE TABLE Funcionarios (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(30),
    email VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10,2),
    data_contratacao DATE
);

CREATE TABLE Servicos (
    id INT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    preco_base DECIMAL(10,2) NOT NULL
);

CREATE TABLE Produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL
);

CREATE TABLE Veiculos (
    id INT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL,
    modelo VARCHAR(50),
    marca VARCHAR(50),
    ano INT,
    cliente_id INT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
);

CREATE TABLE Ordens_de_Servico (
    id INT PRIMARY KEY,
    data_abertura DATE,
    data_fechamento DATE,
    status VARCHAR(30),
    funcionario_id INT,
    veiculo_id INT,
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id),
    FOREIGN KEY (veiculo_id) REFERENCES Veiculos(id)
);

CREATE TABLE Funcionarios_OS (
    funcionario_id INT,
    os_id INT,
    PRIMARY KEY (funcionario_id, os_id),
    FOREIGN KEY (funcionario_id) REFERENCES Funcionarios(id),
    FOREIGN KEY (os_id) REFERENCES Ordens_de_Servico(id)
);

CREATE TABLE Servicos_OS (
    servico_id INT,
    os_id INT,
    preco_final DECIMAL(10,2),
    PRIMARY KEY (servico_id, os_id),
    FOREIGN KEY (servico_id) REFERENCES Servicos(id),
    FOREIGN KEY (os_id) REFERENCES Ordens_de_Servico(id)
);

CREATE TABLE Produtos_OS (
    produto_id INT,
    os_id INT,
    quantidade INT,
    PRIMARY KEY (produto_id, os_id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(id),
    FOREIGN KEY (os_id) REFERENCES Ordens_de_Servico(id)
);

CREATE TABLE Pagamentos (
    os_id INT,
    valor_pago DECIMAL(10,2),
    forma_pagamento VARCHAR(20),
    data_pagamento DATE,
    PRIMARY KEY (os_id, data_pagamento),
    FOREIGN KEY (os_id) REFERENCES Ordens_de_Servico(id)
);

'''
    os.system('mkdir -p db')
    salvar_query_em_arquivo(init, "./db/000_init.sql")

    for i,_ in enumerate(range(0, qtd_clientes, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getClientesQuery(5000), f"./db/001_{i}_clientes.sql")

    for i,_ in enumerate(range(0, qtd_funcionarios, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getFuncionariosQuery(5000), f"./db/002_{i}_funcionarios.sql")

    for i,_ in enumerate(range(0, qtd_servicos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getServicosQuery(5000), f"./db/003_{i}_servicos.sql")

    for i,_ in enumerate(range(0, qtd_produtos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getProdutosQuery(5000), f"./db/004_{i}_produtos.sql")

    for i,_ in enumerate(range(0, qtd_veiculos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getVeiculosQuery(5000, qtd_clientes), f"./db/005_{i}_veiculos.sql")

    for i,_ in enumerate(range(0, qtd_os, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getOSQuery(5000, qtd_funcionarios, qtd_veiculos), f"./db/006_{i}_ordens.sql")

    for i,_ in enumerate(range(0, qtd_fos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getFOSQuery(5000, qtd_funcionarios, qtd_os), f"./db/007_{i}_funcionarios_os.sql")

    for i,_ in enumerate(range(0, qtd_sos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getSOSQuery(5000, qtd_servicos, qtd_os), f"./db/008_{i}_servicos_os.sql")

    for i,_ in enumerate(range(0, qtd_pos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getPOSQuery(5000, qtd_produtos, qtd_os), f"./db/009_{i}_produtos_os.sql")

    for i,_ in enumerate(range(0, qtd_pagamentos, 5000)):
        i = caststr(8,i)
        salvar_query_em_arquivo(getPagamentosQuery(5000, qtd_os), f"./db/010_{i}_pagamentos.sql")


    print("Todos os arquivos foram gerados com IDs consistentes.")
