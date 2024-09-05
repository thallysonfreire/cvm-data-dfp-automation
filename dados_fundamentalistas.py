import os
import requests
import zipfile
import logging
from typing import List
import pandas as pd

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Constantes
URL_BASE = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
ANOS = range(2010, 2023)
DIRETORIO = r'C:\\Users\\thallysonfreire\\developer\\github\\dados_balancos_empresas'


# Função para baixar arquivos ZIP
def baixar_arquivos_zip(anos: range, url_base: str, diretorio: str) -> None:


    os.chdir(diretorio)
    for ano in anos:
        url = f'{url_base}dfp_cia_aberta_{ano}.zip'
        arquivo_destino = f"dfp_cia_aberta_{ano}.zip"

        try:
            logging.info(f'Baixando arquivo: {url}')
            response = requests.get(url)
            response.raise_for_status()  # Verifica se houve erro na requisição
            with open(arquivo_destino, 'wb') as file:
                file.write(response.content)

        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao baixar o arquivo {url}: {e}")


# Função para processar arquivos ZIP
def processar_arquivos_zip(diretorio: str) -> List[pd.DataFrame]:


    lista_demonstracoes = []
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.zip'):

            try:
                with zipfile.ZipFile(arquivo, 'r') as arquivo_zip:
                    ano = arquivo[-8:-4]
                    logging.info(f'Processando arquivo ZIP: {arquivo}')
                    for planilha in arquivo_zip.namelist():
                        if planilha.endswith('.csv'):
                            demonstracao = pd.read_csv(arquivo_zip.open(planilha), sep=";", decimal=",",
                                                       encoding='ISO-8859-1', chunksize=1000)
                            
                            df = pd.concat(demonstracao, ignore_index=True)
                            df["tipo_doc"] = "dfp"
                            lista_demonstracoes.append(df)

            except zipfile.BadZipFile:
                logging.warning(f"Arquivo ZIP inválido: {arquivo}")

            except Exception as e:
                logging.error(f"Erro ao processar {arquivo}: {e}")

    return lista_demonstracoes


# Função para limpar e transformar os dados
def limpar_dados(lista_demonstracoes: List[pd.DataFrame]) -> pd.DataFrame:


    base_dados = pd.concat(lista_demonstracoes)
    
    # Dividindo a coluna 'GRUPO_DFP' em duas colunas
    base_dados[['con_ind', 'tipo_dem']] = base_dados['GRUPO_DFP'].str.split("-", expand=True)
    
    # Limpeza de colunas desnecessárias
    base_dados.drop(columns=['ST_CONTA_FIXA', 'COLUNA_DF', 'GRUPO_DFP'], inplace=True)
    
    # Filtrando registros
    base_dados = base_dados[base_dados['ORDEM_EXERC'] != 'PENÚLTIMO']
    
    # Ajustando tipos
    base_dados['con_ind'] = base_dados['con_ind'].str.strip().astype(str)
    base_dados['tipo_dem'] = base_dados['tipo_dem'].str.strip()

    return base_dados

# Função para extrair dados específicos de uma empresa (ex: WEG S.A.)
def extrair_dados_empresa(df: pd.DataFrame, empresa: str, tipo_dem: str, conta: str) -> pd.DataFrame:


    return df[
        (df['DENOM_CIA'] == empresa) &
        (df['tipo_dem'] == tipo_dem) &
        (df['tipo_doc'] == 'dfp') &
        (df['DS_CONTA'] == conta) &
        (df['con_ind'] == 'DF Consolidado')
    ]


# Execução do fluxo
if __name__ == "__main__":
    baixar_arquivos_zip(ANOS, URL_BASE, DIRETORIO)
    
    lista_demonstracoes = processar_arquivos_zip(DIRETORIO)
    
    if lista_demonstracoes:
        base_dados = limpar_dados(lista_demonstracoes)
        
        # Extraindo dados da WEG S.A.
        weg_dre = extrair_dados_empresa(base_dados, "WEG S.A.", "Demonstração do Resultado", 
                                        "Receita de Venda de Bens e/ou Serviços")
        logging.info(f'Dados extraídos da WEG S.A.: \n{weg_dre}')
    else:
        logging.warning('Nenhum dado foi processado.')
