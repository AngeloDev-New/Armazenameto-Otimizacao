import random
from datetime import datetime, timedelta

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

def getClientesQuery(qtd):
    query = "INSERT INTO Clientes (id, nome, telefone, email) VALUES\n"
    for i in range(1, qtd + 1):
        nome = next(nome_aleatorio)
        telefone = next(numero_aleatorio)
        email = nome.lower().replace(" ", ".") + f"@{next(dominio_aleatorio)}.com"
        query += f"    ({i}, '{nome}', '{telefone}', '{email}'),\n"
    return query.rstrip(',\n') + ';\n'

def getFuncionariosQuery(qtd):
    query = "INSERT INTO Funcionarios (id, nome, telefone, email, cargo, salario, data_contratacao) VALUES\n"
    for i in range(1, qtd + 1):
        nome = next(nome_aleatorio)
        telefone = next(numero_aleatorio)
        email = nome.lower().replace(" ", ".") + f"@{next(dominio_aleatorio)}.com"
        cargo = random.choice(cargos)
        salario = round(random.uniform(1500, 5000), 2)
        data = get_data_aleatoria()
        query += f"    ({i}, '{nome}', '{telefone}', '{email}', '{cargo}', {salario}, '{data}'),\n"
    return query.rstrip(',\n') + ';\n'

def getServicosQuery(qtd):
    query = "INSERT INTO Servicos (id, descricao, preco_base) VALUES\n"
    for i in range(1, qtd + 1):
        descricao = random.choice(descricoes_servicos)
        preco = round(random.uniform(50, 500), 2)
        query += f"    ({i}, '{descricao}', {preco}),\n"
    return query.rstrip(',\n') + ';\n'

def getProdutosQuery(qtd):
    query = "INSERT INTO Produtos (id, nome, preco, estoque) VALUES\n"
    for i in range(1, qtd + 1):
        nome = random.choice(produtos_list)
        preco = round(random.uniform(20, 300), 2)
        estoque = random.randint(1, 100)
        query += f"    ({i}, '{nome}', {preco}, {estoque}),\n"
    return query.rstrip(',\n') + ';\n'

def getVeiculosQuery(qtd, max_cliente_id):
    query = "INSERT INTO Veiculos (id, placa, modelo, marca, ano, cliente_id) VALUES\n"
    for i in range(1, qtd + 1):
        placa = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3)) + '-' + ''.join(random.choices("0123456789", k=4))
        modelo = random.choice(modelos)
        marca = random.choice(marcas)
        ano = random.randint(2000, 2023)
        cliente_id = random.randint(1, max_cliente_id)
        query += f"    ({i}, '{placa}', '{modelo}', '{marca}', {ano}, {cliente_id}),\n"
    return query.rstrip(',\n') + ';\n'

def getOSQuery(qtd, max_funcionario_id, max_veiculo_id):
    query = "INSERT INTO Ordens_de_Servico (id, data_abertura, data_fechamento, status, funcionario_id, veiculo_id) VALUES\n"
    for i in range(1, qtd + 1):
        abertura = get_data_aleatoria()
        fechamento = get_data_aleatoria()
        status = random.choice(status_list)
        funcionario_id = random.randint(1, max_funcionario_id)
        veiculo_id = random.randint(1, max_veiculo_id)
        query += f"    ({i}, '{abertura}', '{fechamento}', '{status}', {funcionario_id}, {veiculo_id}),\n"
    return query.rstrip(',\n') + ';\n'

def getFOSQuery(qtd, max_funcionario_id, max_os_id):
    query = "INSERT INTO Funcionarios_OS (funcionario_id, os_id) VALUES\n"
    for _ in range(qtd):
        funcionario_id = random.randint(1, max_funcionario_id)
        os_id = random.randint(1, max_os_id)
        query += f"    ({funcionario_id}, {os_id}),\n"
    return query.rstrip(',\n') + ';\n'

def getSOSQuery(qtd, max_servico_id, max_os_id):
    query = "INSERT INTO Servicos_OS (servico_id, os_id, preco_final) VALUES\n"
    for _ in range(qtd):
        servico_id = random.randint(1, max_servico_id)
        os_id = random.randint(1, max_os_id)
        preco = round(random.uniform(50, 500), 2)
        query += f"    ({servico_id}, {os_id}, {preco}),\n"
    return query.rstrip(',\n') + ';\n'

def getPOSQuery(qtd, max_produto_id, max_os_id):
    query = "INSERT INTO Produtos_OS (produto_id, os_id, quantidade) VALUES\n"
    for _ in range(qtd):
        produto_id = random.randint(1, max_produto_id)
        os_id = random.randint(1, max_os_id)
        quantidade = random.randint(1, 10)
        query += f"    ({produto_id}, {os_id}, {quantidade}),\n"
    return query.rstrip(',\n') + ';\n'

def getPagamentosQuery(qtd, max_os_id):
    query = "INSERT INTO Pagamentos (os_id, valor_pago, forma_pagamento, data_pagamento) VALUES\n"
    for _ in range(qtd):
        os_id = random.randint(1, max_os_id)
        valor = round(random.uniform(100, 1500), 2)
        forma = random.choice(formas_pagamento)
        data = get_data_aleatoria()
        query += f"    ({os_id}, {valor}, '{forma}', '{data}'),\n"
    return query.rstrip(',\n') + ';\n'

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
CREATE DATABASE IF NOT EXISTS mecanica;
USE mecanica;

CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
   
 nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(30),
    email VARCHAR(100),
    endereco VARCHAR(255),
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Veiculos (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    placa VARCHAR(10) NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    cor VARCHAR(30),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Servicos (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    preco_base DECIMAL(10,2) NOT NULL,
    tempo_estimado VARCHAR(20)
);

CREATE TABLE Produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    preco_venda DECIMAL(10,2) NOT NULL,
    quantidade_estoque INT DEFAULT 0
);

CREATE TABLE Funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2),
    data_admissao DATE
);

CREATE TABLE Ordens_de_Servico (
    id_os INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_veiculo INT NOT NULL,
    data_entrada DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_saida DATETIME,
    status VARCHAR(30) DEFAULT 'Aberta',
    observacoes TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_veiculo) REFERENCES Veiculos(id_veiculo)
);

CREATE TABLE Servicos_OS (
    id_os INT NOT NULL,
    id_servico INT NOT NULL,
    valor_cobrado DECIMAL(10,2),
    quantidade INT DEFAULT 1,
    PRIMARY KEY (id_os, id_servico),
    FOREIGN KEY (id_os) REFERENCES Ordens_de_Servico(id_os),
    FOREIGN KEY (id_servico) REFERENCES Servicos(id_servico)
);

CREATE TABLE Produtos_OS (
    id_os INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT DEFAULT 1,
    valor_unitario DECIMAL(10,2),
    PRIMARY KEY (id_os, id_produto),
    FOREIGN KEY (id_os) REFERENCES Ordens_de_Servico(id_os),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

CREATE TABLE Funcionarios_OS (
    id_os INT NOT NULL,
    id_funcionario INT NOT NULL,
    funcao_na_os VARCHAR(100),
    PRIMARY KEY (id_os, id_funcionario),
    FOREIGN KEY (id_os) REFERENCES Ordens_de_Servico(id_os),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionarios(id_funcionario)
);

CREATE TABLE Pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_os INT NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    forma_pagamento VARCHAR(50),
    data_pagamento DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'Pendente',
    FOREIGN KEY (id_os) REFERENCES Ordens_de_Servico(id_os)
); 
'''
    salvar_query_em_arquivo(init, "./db/0_init.sql")
    salvar_query_em_arquivo(getClientesQuery(qtd_clientes), "./db/1_clientes.sql")
    salvar_query_em_arquivo(getFuncionariosQuery(qtd_funcionarios), "./db/2_funcionarios.sql")
    salvar_query_em_arquivo(getServicosQuery(qtd_servicos), "./db/3_servicos.sql")
    salvar_query_em_arquivo(getProdutosQuery(qtd_produtos), "./db/4_produtos.sql")
    salvar_query_em_arquivo(getVeiculosQuery(qtd_veiculos, qtd_clientes), "./db/5_veiculos.sql")
    salvar_query_em_arquivo(getOSQuery(qtd_os, qtd_funcionarios, qtd_veiculos), "./db/6_ordens.sql")
    salvar_query_em_arquivo(getFOSQuery(qtd_fos, qtd_funcionarios, qtd_os), "./db/7_funcionarios_os.sql")
    salvar_query_em_arquivo(getSOSQuery(qtd_sos, qtd_servicos, qtd_os), "./db/8_servicos_os.sql")
    salvar_query_em_arquivo(getPOSQuery(qtd_pos, qtd_produtos, qtd_os), "./db/9_produtos_os.sql")
    salvar_query_em_arquivo(getPagamentosQuery(qtd_pagamentos, qtd_os), "./db/99_pagamentos.sql")

    print("Todos os arquivos foram gerados com IDs consistentes.")
