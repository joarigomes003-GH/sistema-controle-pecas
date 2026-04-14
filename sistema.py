from colorama import Fore, Style, init
init(autoreset=True)

pecas = []
caixas = []
caixa_atual = []

while True:
    print(Fore.CYAN + "\n====== MENU ======")
    print(Fore.BLUE + "1 - Cadastrar peça")
    print(Fore.BLUE + "2 - Listar peças")
    print(Fore.BLUE + "3 - Remover peça")
    print(Fore.BLUE + "4 - Listar caixas fechadas")
    print(Fore.BLUE + "5 - Relatório final")
    print(Fore.YELLOW + "0 - Sair")

    opcao = input(Fore.YELLOW + "\nEscolha uma opção: ")

    # 1 - CADASTRAR PEÇA
    if opcao == "1":
        print(Fore.CYAN + "\n=== Cadastro de Peça ===")

        id_peca = input(Fore.YELLOW + "Digite o ID da peça: ")
        peso = float(input(Fore.YELLOW + "Digite o peso: "))
        cor = input(Fore.YELLOW + "Digite a cor: ").lower()
        comprimento = float(input(Fore.YELLOW + "Digite o comprimento: "))

        aprovado = True
        motivos = []

        # Validação
        if peso < 95 or peso > 105:
            aprovado = False
            motivos.append("Peso fora do padrão")

        if cor not in ["azul", "verde"]:
            aprovado = False
            motivos.append("Cor inválida")

        if comprimento < 10 or comprimento > 20:
            aprovado = False
            motivos.append("Comprimento fora do padrão")

        peca = {
            "id": id_peca,
            "peso": peso,
            "cor": cor,
            "comprimento": comprimento,
            "status": "Aprovada" if aprovado else "Reprovada",
            "motivos": motivos
        }

        pecas.append(peca)

        if aprovado:
            caixa_atual.append(peca)

            if len(caixa_atual) == 10:
                caixas.append(caixa_atual)
                caixa_atual = []
                print(Fore.GREEN + "\nCaixa fechada com 10 peças!")

            print(Fore.GREEN + "Peça APROVADA e armazenada!")

        else:
            print(Fore.RED + "\nPeça REPROVADA!")
            print(Fore.RED + "Motivos:", ", ".join(motivos))

    # 2 - LISTAR PEÇAS
    elif opcao == "2":
        print(Fore.CYAN + "\n=== Lista de Peças ===")

        if not pecas:
            print(Fore.RED + "Nenhuma peça cadastrada.")
        else:
            for p in pecas:
                print(Fore.WHITE + "\nID:", p["id"])
                if p["status"] == "Aprovada":
                    print(Fore.GREEN + "Status:", p["status"])
                else:
                    print(Fore.RED + "Status:", p["status"])
                    print(Fore.RED + "Motivos:", ", ".join(p["motivos"]))

    # 3 - REMOVER PEÇA
    elif opcao == "3":
        print(Fore.CYAN + "\n=== Remover Peça ===")

        id_remover = input(Fore.YELLOW + "Digite o ID da peça para remover: ")
        encontrada = False

        for p in pecas:
            if p["id"] == id_remover:
                pecas.remove(p)
                encontrada = True
                print(Fore.GREEN + "Peça removida com sucesso!")
                break

        if not encontrada:
            print(Fore.RED + "Peça não encontrada.")

    # 4 - LISTAR CAIXAS FECHADAS
    elif opcao == "4":
        print(Fore.CYAN + "\n=== Caixas Fechadas ===")

        if not caixas:
            print(Fore.RED + "Nenhuma caixa fechada ainda.")
        else:
            for i, caixa in enumerate(caixas, start=1):
                print(Fore.GREEN + f"Caixa {i} - {len(caixa)} peças")

    # 5 - RELATÓRIO FINAL
    elif opcao == "5":
        print(Fore.CYAN + "\n=== RELATÓRIO FINAL ===")

        aprovadas = sum(1 for p in pecas if p["status"] == "Aprovada")
        reprovadas = sum(1 for p in pecas if p["status"] == "Reprovada")

        motivos_contagem = {}

        for p in pecas:
            for m in p["motivos"]:
                if m in motivos_contagem:
                    motivos_contagem[m] += 1
                else:
                    motivos_contagem[m] = 1

        print(Fore.GREEN + f"Peças aprovadas: {aprovadas}")
        print(Fore.RED + f"Peças reprovadas: {reprovadas}")

        print(Fore.YELLOW + "\nMotivos de reprovação:")
        for motivo, qtd in motivos_contagem.items():
            print(Fore.RED + f"{motivo}: {qtd}")

        print(Fore.CYAN + f"\nCaixas utilizadas: {len(caixas)}")

    # SAIR
    elif opcao == "0":
        print(Fore.YELLOW + "\nSaindo do sistema...")
        break

    else:
        print(Fore.RED + "Opção inválida! Tente novamente.")  
