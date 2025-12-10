# etl_projeto_DIO.py
import os
from pathlib import Path
import logging
from logging import handlers
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# CONFIGURAÇÕES / PATHS
# --------------------------------
BASE_DIR = Path(__file__).parent
DADOS_PATH = BASE_DIR / "dados" / "clientes.xlsx"
OUTPUT_DIR = BASE_DIR / "output"
IMGS_DIR = BASE_DIR / "imgs"
LOGS_DIR = BASE_DIR / "logs"

OUTPUT_DIR.mkdir(exist_ok=True)
IMGS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "mensagens_clientes.xlsx"
LOG_FILE = LOGS_DIR / "etl.log"

# --------------------------------
# LOGGING (arquivo + console)
# --------------------------------
logger = logging.getLogger("etl_logger")
logger.setLevel(logging.INFO)
logger.handlers = []  # remove handlers duplicados

fmt = logging.Formatter("%(asctime)s — %(levelname)s — %(message)s")

# handler arquivo
file_handler = handlers.RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3, encoding="utf-8")
file_handler.setFormatter(fmt)
logger.addHandler(file_handler)

# handler console
console_handler = logging.StreamHandler()
console_handler.setFormatter(fmt)
logger.addHandler(console_handler)

# --------------------------------
# 1. EXTRAÇÃO
# --------------------------------
def extrair_dados(caminho_planilha: Path) -> pd.DataFrame:
    logger.info("Extraindo dados...")
    if not caminho_planilha.exists():
        logger.error(f"Arquivo de entrada não encontrado: {caminho_planilha}")
        raise FileNotFoundError(caminho_planilha)
    df = pd.read_excel(caminho_planilha)
    logger.info(f"Registros extraídos: {len(df)}")
    return df

# --------------------------------
# 2. TRANSFORMAÇÃO (regras "inteligentes")
# --------------------------------
def gerar_mensagem_inteligente(linha: pd.Series) -> str:
    nome = str(linha.get("nome", "")).strip()
    gasto = linha.get("gasto_mensal", 0) or 0
    produto = str(linha.get("produto_interesse", "")).lower()
    email = str(linha.get("email", "")).lower()

    # Regras: ordem importa (prioridade)
    try:
        gasto_val = float(gasto)
    except Exception:
        gasto_val = 0

    # Regra premium (gasto muito alto)
    if gasto_val >= 10000:
        return f"Olá {nome}! Você é um cliente premium. Temos benefícios exclusivos e uma consultoria de investimentos. Entre em contato!"

    # Regra gasto alto
    if gasto_val >= 3000:
        return f"Olá {nome}! Pelo seu gasto mensal de R${gasto_val:.2f}, recomendamos nossos planos premium com vantagens em investimentos."

    # Regra produto cartão
    if "cart" in produto or "cartão" in produto or "cartao" in produto:
        return f"Olá {nome}! Como você demonstrou interesse em cartões, que tal conhecer nossas opções com cashback e aumento de limite?"

    # Regra email gmail -> sugerir app mobile
    if email.endswith("@gmail.com"):
        return f"Olá {nome}! Já baixou nosso app mobile? Clientes que usam o app têm promoções exclusivas."

    # Regra gasto médio
    if gasto_val >= 500:
        return f"Olá {nome}! Temos ofertas que podem otimizar seus gastos mensais. Veja nossas opções."

    # fallback
    return f"Olá {nome}! Obrigado por ser nosso cliente. Temos ofertas personalizadas que podem te interessar."

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transformando dados...")
    df = df.copy()

    # Garantir colunas básicas existam
    expected_cols = ["id", "nome", "email", "gasto_mensal", "produto_interesse"]
    for c in expected_cols:
        if c not in df.columns:
            logger.warning(f"Coluna esperada não encontrada: {c}. Preenchendo valores vazios.")
            df[c] = ""

    # Converter gasto_mensal para numérico
    df["gasto_mensal"] = pd.to_numeric(df["gasto_mensal"], errors="coerce").fillna(0)

    # Nova coluna de mensagem
    df["mensagem_marketing"] = df.apply(gerar_mensagem_inteligente, axis=1)

    logger.info("Transformação finalizada.")
    return df

# --------------------------------
# 3. CARREGAMENTO
# --------------------------------
def carregar_dados(df: pd.DataFrame, caminho_saida: Path):
    logger.info("Salvando arquivo final...")
    df.to_excel(caminho_saida, index=False)
    logger.info(f"Arquivo salvo: {caminho_saida}")

# --------------------------------
# 4. GERA GRÁFICOS / VISUALIZAÇÕES
# --------------------------------
def gerar_graficos(df: pd.DataFrame):
    logger.info("Gerando gráficos...")

    # Gasto total por produto
    try:
        grouped = df.groupby(df["produto_interesse"].fillna("Não informado"))["gasto_mensal"].sum().sort_values(ascending=False)
        plt.figure(figsize=(8, 5))
        grouped.plot(kind="bar")
        plt.title("Gasto total por produto")
        plt.xlabel("Produto")
        plt.ylabel("Total gasto (R$)")
        plt.tight_layout()
        img1 = IMGS_DIR / "gasto_por_produto.png"
        plt.savefig(img1)
        plt.close()
        logger.info(f"Gráfico salvo: {img1}")
    except Exception as e:
        logger.exception("Falha ao gerar gráfico gasto por produto: %s", e)

    # Histograma de gastos
    try:
        plt.figure(figsize=(8, 5))
        df["gasto_mensal"].plot(kind="hist", bins=10)
        plt.title("Distribuição de gasto mensal")
        plt.xlabel("Gasto (R$)")
        plt.tight_layout()
        img2 = IMGS_DIR / "hist_gastos.png"
        plt.savefig(img2)
        plt.close()
        logger.info(f"Gráfico salvo: {img2}")
    except Exception as e:
        logger.exception("Falha ao gerar histograma de gastos: %s", e)

# --------------------------------
# EXECUÇÃO PRINCIPAL
# --------------------------------
def executar_etl():
    logger.info("=== INÍCIO DO ETL ===")
    df = extrair_dados(DADOS_PATH)
    df_tratado = transformar_dados(df)
    carregar_dados(df_tratado, OUTPUT_FILE)
    gerar_graficos(df_tratado)
    logger.info("=== ETL FINALIZADO ===")

if __name__ == "__main__":
    executar_etl()
