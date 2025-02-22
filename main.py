from Objects import *
from Database import *
from Utility import *

def main():
    print("Programa iniciado")  # Log para verificar a execução
    while True:
        tabela_personagem()
        tabela_AkumaNoMi()
        espacamento("Menu principal")
        print("1 - Criação de Dados")
        print("2 - Alteração de Dados")
        print("3 - Remoção de Dados")
        print("4 - Consulta de Dados")
        print("5 - Sair\n")

        try:
            opcao = int(input("Selecione a opção desejada (1-5): ").strip())
            print(f"Opção escolhida: {opcao}")  # Log para ver o que o usuário escolheu
            if opcao == 1:
                Criar_personagem()
            elif opcao == 2:
                Alterar_personagem()
            elif opcao == 3:
                Remover_Personagem()
            elif opcao == 4:
                Consultar_Personagem()
            elif opcao == 5:
                print("Programa encerrado.")
                break
            else:
                print("Opção inválida. Escolha entre 1 e 5.\n")
        except ValueError:
            print("Entrada inválida. Escolha entre 1 e 5.\n")

if __name__ == "__main__":
    main()
