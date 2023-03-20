import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fazendo uma requisição GET para a página
url = "https://www.undp.org/pt/brazil/idhm-munic%C3%ADpios-2010"
r = requests.get(url)
response = requests.get(url)
if response.status_code == 200:
    print('A requisição foi bem-sucedida!')
else:
    print('A requisição falhou. Código de status:', response.status_code)

# Criando um objeto BeautifulSoup a partir do conteúdo da página
soup = BeautifulSoup(r.content, 'html.parser')

# Encontrando a tabela que contém os dados que queremos extrair
tabela = soup.find('table', {'class': 'tableizer-table'})

# Encontrando todas as linhas da tabela
linhas = tabela.find_all('tr')

# listas para os nomes dos municípios e seus respectivos IDHs
nomes = []
idhs = []

# Lista de siglas dos estados do Nordeste
siglas_nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

# Loop para iterar sobre as siglas do Nordeste e filtrar as linhas correspondentes
for sigla in siglas_nordeste:
    for linha in linhas:
        colunas = linha.find_all('td')
        if len(colunas) > 0 and sigla in colunas[1].text.strip():
            nome_municipio = colunas[1].text.strip()
            idh_municipio = colunas[2].text.strip()
            nomes.append(nome_municipio)
            idhs.append(idh_municipio)

# Dicionário com as listas de nomes e IDHs
dados = {'Município': nomes, 'IDH-M': idhs}

df = pd.DataFrame(dados)

print(df)

# Salvando os Dados Numa Planilha do Excel
df.to_excel('dados.xlsx')