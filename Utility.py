import re

def espacamento(msg):
    print("-" * 40)
    print(f'{msg:^40}')
    print("-" * 40)

def perguntar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ["S", "N"]:
            return resposta
        print("Opção inválida. Digite S ou N.")

def tratar_id(cursor):
    while True:
        try:
            u_id = int(input("Digite o ID do personagem: ").strip())
            if verificar_id_existe(cursor, u_id):
                return u_id
            print("Erro: ID não encontrado.")
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")

def tratar_nome():
    while True:
        nome = input("Digite o nome do Personagem: ").strip().title()
        if re.match("^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", nome):
            return nome
        else:
            print("O nome deve conter apenas caracteres alfabéticos e espaços.\n")

def verificar_id_existe(cursor, id_personagem):
    cursor.execute("SELECT 1 FROM Personagem WHERE id = ?;", (id_personagem,))
    return cursor.fetchone() is not None

def validar_especie():
    especies_validas = ["Humano","Mink","Homens-Peixe", "Sereianos", "Tontatta","Gigantes",
                        "Lunares","Outras Espécies"]
    while True:
        especie = input("Escolha a Espécie (Humano, Mink, Homens-Peixe, Sereianos, Tontatta, Gigantes,"
                        "Lunares, Outras Espécies): ").capitalize()
        if especie in especies_validas:
            return especie
        print("Espécie inválida. Tente novamente.")

def validar_origem():
    origens_validas = ["North blue", "South Blue", "East Blue","West Blue", "Grand line", "Red line",
                       "Governo Mundial","Skypie"]
    while True:
        origem = input("Escolha a Origem (North blue, South Blue, East Blue,West Blue, Grand line, Red line,"
                       "Governo Mundial,Skypie): ").capitalize()
        if origem in origens_validas:
            return origem
        print("Origem inválida. Tente novamente.")

def validar_grupo():
    grupos_validos = ["Piratas", "Marinha", "Revolucionarios", "Governo Mundial", "Civil", "Desconhecido"]
    while True:
        grupos = input("Escolha um Grupos (Piratas, Marinha, Revolucionarios, Governo Mundial, Civil, Desconhecido): ").capitalize()
        if grupos in grupos_validos:
            return grupos
        print("Grupos inválida. Tente novamente.")

def validar_titulo():
    titulos_validos = ["Yonkou", "Shichibukai","Capitão",f"Membro do grupo", ]
    while True:
        titulo = input("Escolha um Título (Yonkou, Shichibukai,Capitão, Membro do 'grupo'): ").capitalize()
        if titulo in titulos_validos:
            return titulo
        print("Título inválida. Tente novamente.")

def validar_haki():
    hakis_validos = ["Armamento","observador","Conquistador",]
    while True:
        haki = input("Escolha um Haki (Armamento, observador, Conquistador): ").capitalize()
        if haki in hakis_validos:
            return haki
        print("Haki inválido. Tente novamente")

def tratar_akuma_no_mi():
    tipos_validos = ["Paramecia", "Zoan", "Logia"]
    while True:
        tipo = input("Escolha um tipo de Akuma no mi (Paramecia, Zoan, Logia): ").capitalize()
        if tipo in tipos_validos:
            nome = input("Digite o nome da Akuma no mi: ").strip().title()
            return nome, tipo
        print("Tipo inválido. Tente novamente.")
