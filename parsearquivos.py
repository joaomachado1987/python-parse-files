import os
from parse.write_file import write_arquivo

def parse_arquivo():

    dir_arquivos = "C:\\Users\\jabo\\Desktop\\mapeamento dos arquivos (dados sensíveis)\\arquivos\\"

    name_arquivos = os.listdir(dir_arquivos)

    arquivos_name_list = [dir_arquivos + name_arquivo for name_arquivo in name_arquivos]

    for arquivos_name in arquivos_name_list:
        with open(arquivos_name, "r", encoding='utf-8') as arquivo:
            nome_arquivo = arquivo.name.split('\\')[-1].strip('.txt')
            linhas = arquivo.readlines()

            linhas_strip = [linha.strip('\n') for linha in linhas]

            write_arquivo(nome_arquivo, linhas_strip)

if __name__ == '__main__':
    parse_arquivo()
