<p align="center">
<img src="https://raw.githubusercontent.com/alv-vitoria/meu-projeto-etl-dio-santander/refs/heads/main/imgs/bannerdio.png" 
  height="299px" 
  alt="Banner do Projeto ETL">
</p>


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

Este projeto implementa um pipeline completo de ETL (Extract, Transform, Load) utilizando Python, Pandas, logs estruturados, regras inteligentes e geração de gráfico automatizado, simulando um fluxo real usado por empresas no tratamento de dados.

O objetivo é demonstrar domínio em:
- Estruturação de pipelines
- Transformação de dados com regras inteligentes
- Geração de gráficos
- Boas práticas com logs e diretórios
- Ambiente Python profissional


## 📁 Estrutura do Projeto
```
─── projeto_etl/
├── dados/               # Arquivos de entrada (.xlsx)
├── imgs/                # Gráficos gerados pelo ETL
├── logs/                # Logs do processo ETL
├── output/              # Arquivos finais gerados (.xlsx)
├── etl_projeto_DIO.py   # Script principal do pipeline
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
└── .gitignore           # Arquivos ignorados pelo Git
 ```

## 🧠 Funcionalidades do Projeto

O pipeline foi ampliado para incluir recursos avançados:

- Geração de mensagens personalizadas
- Regras inteligentes para cada tipo de cliente
- Logs estruturados e organizados
- Dashboard simples (gráficos gerados automaticamente)
- Ambiente virtual isolado (venv)
- Pipeline pronto para execução automática

### 🟦 ETAPA 1 — Extração
- Leitura automática da planilha de clientes.


### 🟧 ETAPA 2 — Transformação
- Aplicação de regras inteligentes:
- Gasto alto → mensagem premium
- Email Gmail → sugestão de usar o app mobile
- Interesse em cartão → mensagem específica
- Mensagens personalizadas simulando IA generativa (sem usar modelos externos)


### 🟥 ETAPA 3 — Carregamento  
A saída final é salva em:  
```output/mensagens_clientes.xlsx```

**Logs estruturados**  
O processo inteiro gera logs profissionais em:  
```logs/etl.log```


**Gráfico automático**  
Um gráfico com a distribuição de gastos por produto é salvo em:  
```imgs/gasto_por_produto.png```

*Exemplo:*
<p align="center">
  <img src="https://raw.githubusercontent.com/alv-vitoria/meu-projeto-etl-dio-santander/refs/heads/main/imgs/gasto_por_produto.png"
       alt="Gráfico de Gasto Total por Produto"
       height="320px"
       style="border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.4);">
</p>



## 🪛 Tecnologias utilizadas  
| Tecnologia     | Descrição                      |
| -------------- | ------------------------------ |
| **Python 3**   | Linguagem principal do projeto |
| **Pandas**     | Manipulação de dados           |
| **OpenPyXL**   | Leitura e escrita em Excel     |
| **Matplotlib** | Geração de gráficos            |
| **Logging**    | Sistema de logs                |
| **Venv**       | Ambiente virtual               |
| **VS Code**    | Desenvolvimento                |


## ▶ Como executar o projeto  
1 - Ative o ambiente virtual  
```"source .venv/bin/activate"```

2 - Instale as dependências  
```"pip install -r requirements.txt"```

3 - Execute o ETL  
```"python3 etl_projeto_DIO.py"```


## ⚙️ O pipeline gera automaticamente:
- Planilha final transformada
- Relatórios de logs
- Gráfico de distribuição dos clientes
- Mensagens e regras sobre o tipo de utilização de cada cliente

## 🎯 Objetivo do Projeto
- Criar um pipeline ETL profissional em Python
- Aplicar regras de negócio inteligentes
- Gerar gráficos úteis para tomada de decisão
- Preparação para projetos de dados no mundo real

## ✨ Autora
Vitória Alvares dos Santos  
*Projeto do Bootcamp Santander/DIO - Ciência de Dados com Python (2025)*
