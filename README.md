# 📦 Projeto Banco de Dados Oficina Mecânica

Este projeto simula o banco de dados de uma **oficina mecânica**, contendo o registro de clientes, veículos, serviços, produtos, ordens de serviço, funcionários e pagamentos.

Foi desenvolvido para fins educacionais com o objetivo de praticar modelagem, manipulação e análise de dados com SQL. O ambiente é totalmente **automatizado com Docker**.

---

## ⚙️ Tecnologias

- MySQL 8
- Docker / Docker
- Python3
---

## 🚀 Como usar com Docker

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/mecanica-db.git
cd mecanica-db
```

### 2. Estrutura esperada

```
mecanica-db/
├── Dockerfile
├── README.md
├── DER_mecanica.png
├── requirements.txt
├── script.py
├── .gitignore
└── pdfs/
    ├── 0_init.pdf
    └── Projeto-2-2025.pdf
└── db/
    ├── 0_init.sql
    ├── 1_clientes.sql
    ├── 2_funcionarios.sql
    ├── 3_servicos.sql
    ├── 4_produtos.sql
    ├── 5_veiculos.sql
    ├── 6_ordens.sql
    ├── 7_funcionarios_os.sql
    ├── 8_servicos_os.sql
    ├── 9_produtos_os.sql
    └── 99_pagamentos.sql
```

### 3. Construir e rodar

```bash
docker build -t mecanica-db .
docker run -d -p 3306:3306 --name mecanica_container mecanica-db
```

A imagem criará o banco `mecanica` com todas as tabelas e dados inseridos automaticamente via `.sql` na pasta `/docker-entrypoint-initdb.d/`.

---

## 🧩 Estrutura do Banco de Dados

- **Clientes**: nome, telefone, e-mail, endereço, data do cadastro.
- **Veículos**: placa, modelo, ano, cor e vínculo com cliente.
- **Funcionários**: nome, cargo, salário e data de admissão.
- **Serviços**: descrição, preço base, tempo estimado.
- **Produtos**: nome, descrição, preço e estoque.
- **Ordens de Serviço (OS)**: cliente, veículo, data entrada/saída, status, observações.
- **Serviços_OS**: serviços executados em uma OS.
- **Produtos_OS**: produtos usados em uma OS.
- **Funcionários_OS**: funcionários que trabalharam em uma OS.
- **Pagamentos**: valor total, forma de pagamento, status e vínculo com OS.
![DER_mecanica.png](DER_mecanica.png)
---

## ❓ 15 Questões para Análise e Prática de SQL

1. **Listar todos os clientes que possuem veículos cadastrados.**
2. **Exibir os veículos do cliente 'João da Silva'.**
3. **Mostrar os serviços que custam mais de R$ 200,00.**
4. **Listar os produtos com menos de 5 unidades em estoque.**
5. **Obter as ordens de serviço em aberto.**
6. **Listar os funcionários que participaram de ordens de serviço.**
7. **Mostrar o total de ordens de serviço por cliente.**
8. **Calcular o valor total de cada ordem de serviço com base em serviços e produtos.**
9. **Exibir a soma dos pagamentos recebidos no mês atual.**
10. **Listar as ordens de serviço com pagamento pendente.**
11. **Mostrar a quantidade de serviços realizados por cada funcionário.**
12. **Listar os produtos mais utilizados nas ordens de serviço.**
13. **Exibir o valor médio dos serviços prestados.**
14. **Listar os veículos e seus respectivos clientes.**
15. **Obter a quantidade total de ordens de serviço por mês.**

---

## 🧑‍💻 Autor

Feito por AngeloDevNew — [Curso de Inteligência Artificial / Ciência de Dados / Banco de Dados].

---

## 📜 Licença

MIT — Sinta-se livre para usar, modificar e distribuir.