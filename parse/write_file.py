import json

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
