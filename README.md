*Projeto ETL — Santander / DIO*

Explorando IA Generativa em um Pipeline de ETL com Python

Este projeto implementa um pipeline completo de ETL (Extract, Transform, Load) utilizando Python, Pandas e engenharia de dados.

Além do fluxo principal, o projeto foi expandido com:

Geração de mensagens personalizadas
Regras inteligentes
Logs estruturados
Dashboard simples (gráfico)
Ambiente virtual isolado
Pipeline pronto para execução automática

*Estrutura do Projeto*

├── dados/               # Arquivos de entrada em xlsx
├── imgs/                # Gráficos gerados
├── logs/                # Logs do processo ETL
├── output/              # Saída final do ETL em xlsx
├── etl_projeto_DIO.py   # Código principal
├── requirements.txt     # Dependências
├── README.md            # Documentação
└── .gitignore

Tecnologias utilizadas:
- Python 3
- Pandas
- OpenPyXL
- Matplotlib
- Logging
- VS Code
- Virtual Environment (venv)

Como executar o projeto:

1 - Ative o ambiente virtual
"source .venv/bin/activate"

2 - Instale as dependências
"pip install -r requirements.txt"

3 - Execute o ETL
"python3 etl_projeto_DIO.py"

*Resultados*
O pipeline gera:

- Planilha final transformada

- Relatórios de logs

- Gráfico de distribuição dos clientes

- Mensagens e regras sobre o tipo de utilização de cada cliente

Exemplo de gráfico:
![Gráfico de Gasto total por Produto](https://raw.githubusercontent.com/alv-vitoria/meu-projeto-etl-dio-santander/refs/heads/main/imgs/gasto_por_produto.png)

Regras sobre o tipo de utilização de cada cliente:

- Clientes com gasto alto → mensagem premium

- Clientes do Gmail → sugestão de app mobile

- Compras com cartão → mensagem específica

- e muito mais…


*Objetivo do Projeto*
Demonstrar conhecimentos aplicados sobre:

- ETL real com Python
- Organização de projeto
- Geração de insights e gráficos visuais
- Preparação para projetos de dados no mundo real

Autora:
Vitória Alvares dos Santos

Projeto do Bootcamp Santander/DIO 2025 - Ciência de Dados com Python