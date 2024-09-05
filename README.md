# **CVM Financial Data Automation**

Este repositório contém um script automatizado em Python para download, extração e processamento de dados financeiros de empresas abertas, disponibilizados pela Comissão de Valores Mobiliários (CVM). O código utiliza as bibliotecas **Pandas** e **Requests** para realizar o processamento eficiente de arquivos `.zip` e `.csv`.

## **Índice**
- Contexto
- Funcionalidades
- Estrutura do Projeto
- Instalação
- Uso
- Contribuição
- Licença

## **Contexto**
Este projeto visa automatizar o processo de download e tratamento de dados financeiros de empresas abertas listadas na CVM. A partir dos dados processados, é possível realizar análises financeiras, como o desempenho de empresas ao longo dos anos, utilizando a biblioteca **Pandas**.

## **Funcionalidades**
- **Download automatizado:** Baixa arquivos `.zip` contendo dados financeiros (DFP - Demonstrações Financeiras Padronizadas) de empresas para o período de 2010 a 2023.
- **Extração e leitura:** Extrai e processa arquivos `.csv` diretamente dos arquivos `.zip`.
- **Limpeza e transformação dos dados:** Limpa e formata os dados de forma eficiente para análise.
- **Exemplo de análise:** Extrai dados financeiros específicos para a empresa *WEG S.A.*, como receita de venda de bens e/ou serviços.

## **Estrutura do Projeto**
```
CVM Financial Data Automation/
│
├── main.py                 # Script principal para download e processamento dos dados
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto
```
## **Instalação**
### **Pré-requisitos**
- **Python 3.8+**
- As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Para instalar as dependências, execute:
```
pip install -r requirements.txt
```
## **Bibliotecas utilizadas**
- **Requests:** Para realizar downloads de arquivos a partir da web.
- **Pandas:** Para manipulação e análise de dados.
- **Zipfile:** Para descompactar arquivos `.zip`.
- **Logging:** Para rastreamento de erros e status do processo.

# **Uso**
1. **Baixar o repositório:** Clone o repositório para sua máquina local:
```
git clone https://github.com/seu-usuario/cvm-financial-data-automation.git
cd cvm-financial-data-automation
```
2. **Executar o script:** Após instalar as dependências, execute o script `main.py`:
```
python main.py
```
3. **Dados processados:** O script irá baixar e processar os dados, criando um DataFrame consolidado com os dados financeiros das empresas.

4. **Exemplo de extração de dados:** Ao final do script, os dados financeiros da empresa *WEG S.A.* são filtrados e impressos no console. Este é apenas um exemplo, e você pode adaptar o código para analisar outras empresas ou contas financeiras específicas.

## **Contribuição**
Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum bug, sinta-se à vontade para abrir uma issue ou enviar um *pull request*.

### **Para contribuir:**
1. **Fork** o projeto.
2. Crie uma nova *branch* para sua funcionalidade:
```
git checkout -b feature/nova-funcionalidade
```
3. Envie suas alterações:
```
git commit -m 'Adiciona nova funcionalidade'
```
4. Envie para o repositório principal:
```
git push origin feature/nova-funcionalidade
```
5. Abra um *pull request* para revisão.

## **Licença**
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.