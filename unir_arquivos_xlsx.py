import os
import pandas as pd
import pyautogui

# Inicio do programa
if __name__ == "__main__":

    # listar todos arquivos do diretório atual
    diretorioAtual = os.getcwd()
    arquivos = os.listdir(diretorioAtual)

    # filtrar apenas arquivos xlsx
    arquivosXlsx = [arquivo for arquivo in arquivos if arquivo.lower().endswith(".xlsx")]

    # verificando se possui arquivos xlsx no diretório
    if arquivosXlsx != []:
        # criação de uma lista para armazenar os DataFrames
        lista_dfs = []

        # fazendo união dos arquivos xlsx
        for arquivo in arquivosXlsx:
            dados = pd.read_excel(arquivo)
            lista_dfs.append(dados)

        # usando o método concat para unir os DataFrames da lista
        planilhaUnificada = pd.concat(lista_dfs, ignore_index=True)

        # salvando o arquivo xlsx unificado
        planilhaUnificada.to_excel('arquivo_unificado.xlsx', engine='xlsxwriter')

    else:
        pyautogui.alert(text='Não foi localizado nenhum arquivo xlsx nesse diretório...', title='Aviso', button="Fechar")
        quit()

# fim do programa
pyautogui.alert(text='Concluído com sucesso!', title='Aviso', button="Fechar")
