import os
import pandas as pd

#listar todos arquivos do diretório atual
diretorioAtual = os.getcwd()
arquivos = os.listdir(diretorioAtual)

#filtrar apenas arquivos xlsx
arquivosXlsx = [arquivo for arquivo in arquivos if arquivo.lower().endswith(".xlsx")]

#criação do dataframe, para armazenar as planilhas unidas
planilhaUnificada = pd.DataFrame()

#fazendo união dos arquivos xlsx
for arquivo in arquivosXlsx:
    dados = pd.read_excel(arquivo)
    planilhaUnificada = planilhaUnificada.append(dados)
 
print("Salvando...") 

#salvamento do arquivo xlsx unificado
planilhaUnificada.to_excel('arquivo_unificado.xlsx', engine='xlsxwriter')
