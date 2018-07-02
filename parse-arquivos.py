import os
import json

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

def write_arquivo(nome_arquivo, linhas):

    arquivo_path = "C:\\Users\\jabo\\Desktop\\mapeamento dos arquivos (dados sensíveis)\\arquivos gerados\\"
    archive = {}
    archive["name"] = nome_arquivo
    archive["variables"] = []
    position_start = 0

    print("\n################# "+nome_arquivo + "\n")

    for linha in linhas:

        variable = {}

        name, size, restrictive, description = linha.split(',', maxsplit=3)

        variable["name"] = name
        variable["size"] = size
        variable["restrictive"] = restrictive
        variable["description"] = str(description).strip(' " ')

        fields = linha.split(',')

        field_size = fields[1]

        variable["position_init"] = position_start
        variable["position_end"] = position_end = (position_start + int(field_size))

        position_start = position_end

        archive["variables"].append(variable)

    with open(arquivo_path + nome_arquivo, 'w') as write_file:
        json.dump(archive, write_file, indent=4, ensure_ascii=False)

    print(json.dumps(archive, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    parse_arquivo()
