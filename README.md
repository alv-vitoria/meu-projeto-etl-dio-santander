<p align="center">
  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  
  <!-- Pandas -->
  <img src="https://img.shields.io/badge/Pandas-1.x-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  
  <!-- Matplotlib -->
  <img src="https://img.shields.io/badge/Matplotlib-Visualização-11557C?style=for-the-badge"/>
  
  <!-- Excel -->
  <img src="https://img.shields.io/badge/Excel-Automação-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
  
  <!-- GitHub -->
  <img src="https://img.shields.io/badge/GitHub-Projeto_Ativo-181717?style=for-the-badge&logo=github&logoColor=white"/>
  
  <!-- Status -->
  <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge"/>
</p>








## **🚀 Projeto ETL - Santander / DIO** 
*Explorando IA Generativa em um Pipeline de ETL com Python*

Este projeto implementa um pipeline completo de ETL (Extract, Transform, Load) utilizando Python, Pandas e engenharia de dados.

Além do fluxo principal, o projeto foi expandido com:

- Geração de mensagens personalizadas
- Regras inteligentes
- Logs estruturados
- Dashboard simples (gráfico)
- Ambiente virtual isolado
- Pipeline pronto para execução automática

## Estrutura do Projeto

```📂 projeto_etl/ ```

```├── dados/               # Arquivos de entrada (.xlsx)```

```├── imgs/                # Gráficos gerados pelo ETL```

```├── logs/                # Logs do processo ETL```

```├── output/              # Arquivos finais gerados (.xlsx)```

```├── etl_projeto_DIO.py   # Script principal do pipeline```

```├── requirements.txt     # Dependências do projeto```

```├── README.md            # Documentação```

```└── .gitignore           # Arquivos ignorados pelo Git ```

## Tecnologias utilizadas
- Python 3
- Pandas
- OpenPyXL
- Matplotlib
- Logging
- VS Code
- Virtual Environment (venv)

## Executando o projeto

1 - Ative o ambiente virtual
"source .venv/bin/activate"

2 - Instale as dependências
"pip install -r requirements.txt"

3 - Execute o ETL
"python3 etl_projeto_DIO.py"

## Resultados
O pipeline gera:

- Planilha final transformada
- Relatórios de logs
- Gráfico de distribuição dos clientes
- Mensagens e regras sobre o tipo de utilização de cada cliente

Exemplo de gráfico gerado: *Gráfico de Gasto total por Produto*
![Gráfico de Gasto total por Produto](https://raw.githubusercontent.com/alv-vitoria/meu-projeto-etl-dio-santander/refs/heads/main/imgs/gasto_por_produto.png)


## Regras sobre o tipo de utilização de cada cliente

- Clientes com gasto alto → mensagem premium
- Clientes do Gmail → sugestão de app mobile
- Compras com cartão → mensagem específica
- e muito mais…

## Objetivo do Projeto
Demonstrar conhecimentos aplicados sobre:

- ETL real com Python
- Organização de projeto
- Geração de insights e gráficos visuais
- Preparação para projetos de dados no mundo real

## Autora
Vitória Alvares dos Santos

Projeto do Bootcamp Santander/DIO 2025 - Ciência de Dados com Python
