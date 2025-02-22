import sqlite3 as conector
from Utility import *
from Objects import Personagem

DB = 'OPdata'

def conectar_banco():
    conexao = conector.connect(DB)
    conexao.execute("PRAGMA foreign_keys = on")
    return conexao

def tabela_personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        table_personagem = '''CREATE TABLE IF NOT EXISTS Personagem (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            especie TEXT NOT NULL,
                            origem TEXT NOT NULL,
                            grupo TEXT NOT NULL,
                            titulo TEXT NOT NULL,
                            haki TEXT NOT NULL,
                            akuma_no_mi TEXT NOT NULL);'''

        cursor.execute(table_personagem)
        conexao.commit()

    finally:
        cursor.close()
        conexao.close()

def tabela_AkumaNoMi():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        table_akuma_no_mi = '''CREATE TABLE IF NOT EXISTS Akuma_no_mi(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT NOT NULL,
                            nome TEXT NOT NULL,
                            status TEXT NOT NULL);'''

        cursor.execute(table_akuma_no_mi)
        conexao.commit()
    finally:
        cursor.close()
        conexao.close()

def salvar_personagem_no_banco(cursor, personagem):
    cursor.execute('''INSERT INTO Personagem (nome, especie, origem, grupo, titulo, haki, akuma_no_mi)
                    VALUES (?,?,?,?,?,?,?);''',
                   (personagem.nome, personagem.especie, personagem.origem, personagem.grupo, personagem.titulo,
                    personagem.haki, personagem.akuma_no_mi))

def salvar_akuma_no_mi_no_banco(cursor, akuma_no_mi):
    cursor.execute('''INSERT INTO Akuma_no_mi (tipo, nome, status)
                    VALUES (?,?,?);''',
                   (akuma_no_mi.tipo, akuma_no_mi.nome, akuma_no_mi.status))

def Criar_personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        while True:
            espacamento("Inserção de personagem")
            nome = tratar_nome()
            especie = validar_especie()
            origem = validar_origem()
            grupo = validar_grupo()
            titulo = validar_titulo()
            haki = validar_haki()
            akuma_no_mi_nome, akuma_no_mi_tipo = tratar_akuma_no_mi()

            # Corrigir aqui para salvar akuma_no_mi corretamente
            akuma_no_mi = f"{akuma_no_mi_tipo}: {akuma_no_mi_nome}"

            personagem = Personagem(nome, especie, origem, grupo, titulo, haki, akuma_no_mi)
            cursor.execute('''INSERT INTO Personagem (nome, especie, origem, grupo, titulo, haki, akuma_no_mi)
                              VALUES (?, ?, ?, ?, ?, ?, ?);''',
                           (personagem.nome, personagem.especie, personagem.origem,
                            personagem.grupo, personagem.titulo, personagem.haki, personagem.akuma_no_mi))
            conexao.commit()
            print(f"O personagem {personagem.nome} foi criado com sucesso!")

            if perguntar_sim_nao("Deseja criar outro personagem? (S/N): ") == "N":
                break

    finally:
        cursor.close()
        conexao.close()

def Alterar_personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        while True:
            espacamento("Alterar personagem")
            print("[1] - Alterar Nome\n"
                  "[2] - Alterar Espécie\n"
                  "[3] - Alterar Origem\n"
                  "[4] - Alterar Grupo\n"
                  "[5] - Alterar Título\n"
                  "[6] - Alterar Haki\n"
                  "[7] - Alterar Akuma no mi\n"
                  "[8] - Sair\n")

            opcao = input("Escolha a opção: ").strip()

            if opcao == "1":
                u_id = tratar_id(cursor)
                u_nome = tratar_nome()

                cursor.execute("UPDATE Personagem SET nome = ? WHERE id = ?;", (u_nome, u_id))
                conexao.commit()
                print(f"Nome alterado com sucesso!\nNovo nome: {u_nome}\n")

            elif opcao == "2":
                u_id = tratar_id(cursor)
                u_especie = validar_especie()

                cursor.execute("UPDATE Personagem Set especie = ? WHERE id = ?;",(u_especie, u_id))
                conexao.commit()
                print(f"Espécie alterada com sucesso!\nNova espécie: {u_especie}\n")

            elif opcao == "3":
                u_id = tratar_id(cursor)
                u_origem = validar_origem()

                cursor.execute("UPDATE Personagem Set origem = ? WHERE id = ?;", (u_origem, u_id))
                conexao.commit()
                print(f"Origem alterada com sucesso!\nNova Origem: {u_origem}\n")

            elif opcao == "4":
                u_id = tratar_id(cursor)
                u_grupo = validar_grupo()

                cursor.execute("UPDATE Personagem Set grupo = ? WHERE id = ?;", (u_grupo, u_id))
                conexao.commit()
                print(f"Grupo alterado com sucesso!\nNovo Grupo: {u_grupo}\n")

            elif opcao == "5":
                u_id = tratar_id(cursor)
                u_titulo = validar_titulo()

                cursor.execute("UPDATE Personagem Set título = ? WHERE id = ?;", (u_titulo, u_id))
                conexao.commit()
                print(f"Título alterado com sucesso!\nNovo título: {u_titulo}\n")

            elif opcao == "6":
                u_id = tratar_id(cursor)
                u_haki = validar_haki()

                cursor.execute("UPDATE Personagem Set haki = ? WHERE id = ?;", (u_haki, u_id))
                conexao.commit()
                print(f"Haki alterado com sucesso!\nNovo Haki: {u_haki}\n")

            elif opcao == "7":
                u_id = tratar_id(cursor)
                u_akuma_no_mi = tratar_akuma_no_mi()

                cursor.execute("UPDATE Personagem Set akuma_no_mi = ? WHERE id = ?;", (u_akuma_no_mi, u_id))
                conexao.commit()
                print(f"Akuma no mi alterada com sucesso!\nNova Akuma no mi: {u_akuma_no_mi}\n")

            elif opcao == "8":
                break

            else:
                print("Opção inválida. Tente novamente")

    except conector.DatabaseError as err:
        print(f"Erro no banco de dados: {err}")
    except ValueError as err:
        print(f"Erro de valor: {err}")

    finally:
        cursor.close()
        conexao.close()

def Remover_Personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        while True:
            espacamento("Remover personagem")
            print("[1] - Remover Personagem\n"
                  "[2] - Sair\n")

            opcao = input("Escolha a opção: ").strip()

            if opcao == "1":
                d_id = tratar_id(cursor)
                if verificar_id_existe(cursor, d_id):
                    comando_delete = '''DELETE FROM Personagem WHERE id = ?;'''
                    cursor.execute(comando_delete, (d_id,))
                    conexao.commit()
                    print(f"Personagem com o ID {d_id} foi removido da lista.")
                else:
                    print(f"Personagem com o ID {d_id} não encontrado.")


            elif opcao == "2":
                break
            else:
                print("Opção inexistente, tente novamente!")
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        cursor.close()
        conexao.close()

def Consultar_Personagem():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        while True:
            print("[1] - Lista de personagem \n"
                  "[2] - Sair\n")

            opcao = input("Escolha a opção desejada: ""\n").strip()
            if opcao == "1":
                r_personagem = '''SELECT id, nome, especie, origem, grupo, titulo, haki, akuma_no_mi
                                  FROM Personagem ORDER BY id;'''
                cursor.execute(r_personagem)
                data_personagem = cursor.fetchall()
                if not data_personagem:
                    print("Nenhum personagem encontrado.")
                else:
                    for data in data_personagem:
                        print(f"ID: {data[0]} | Nome: {data[1]} | Espécie: {data[2]}\n"
                              f"Origem: {data[3]} | Grupo: {data[4]} | Título: {data[5]}\n"
                              f"Haki: {data[6]} | Akuma no mi: {data[7]}\n")

            elif opcao == "2":
                break
            else:
                print("Opção inexistente, tente novamente!\n")
    except conector.DatabaseError as err:
        print("Erro de banco de dados", err)

    finally:
        cursor.close()
        conexao.close()











