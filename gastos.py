import pickle
from gasto import Gasto

# Carregar dados salvos (se existirem)
try:
    with open('gastos.pkl', 'rb') as arquivo:
        gastos = pickle.load(arquivo)
except FileNotFoundError:
    gastos = []

def exibir_gastos():
    if not gastos:
        print("Nenhum gasto registrado.")
    else:
        gastos_ordenados = sorted(gastos, key=lambda gasto: gasto.prestacoes)
        total_gastos = 0

        for index, gasto in enumerate(gastos_ordenados):
            print(f"{index + 1}. Nome: {gasto.nome} | Prestações Restantes: {gasto.prestacoes} | Valor: R${gasto.valor:.2f}")
            total_gastos += gasto.valor

        print(f"\nTotal de Gastos: R${total_gastos:.2f}")

def adicionar_gasto():
    nome = input("Nome do gasto: ")
    prestacoes = int(input("Prestações restantes: "))
    valor = input("Valor da prestação: ").replace(',', '.')
    valor = float(valor)

    novo_gasto = Gasto(nome, prestacoes, valor)
    gastos.append(novo_gasto)
    print("Gasto adicionado com sucesso.")

    # Salvar os dados atualizados
    with open('gastos.pkl', 'wb') as arquivo:
        pickle.dump(gastos, arquivo)

def excluir_gasto():
    exibir_gastos()
    indice = int(input("Digite o número do gasto que deseja excluir: ")) - 1

    if 0 <= indice < len(gastos):
        gasto_excluido = gastos.pop(indice)
        print(f"Gasto '{gasto_excluido.nome}' excluído com sucesso.")
    else:
        print("Índice inválido.")

    # Salvar os dados atualizados
    with open('gastos.pkl', 'wb') as arquivo:
        pickle.dump(gastos, arquivo)

def atualizar_gastos():
    for gasto in gastos:
        gasto.prestacoes -= 1

        if gasto.prestacoes == 0:
            gastos.remove(gasto)
            print(f"O objetivo '{gasto.nome}' foi alcançado e removido.")

    # Salvar os dados atualizados
    with open('gastos.pkl', 'wb') as arquivo:
        pickle.dump(gastos, arquivo)

while True:
    print("\n--- Meus Gastos Mensais ---")
    print("1. Exibir gastos")
    print("2. Adicionar novo gasto")
    print("3. Excluir gasto")
    print("4. Atualizar gastos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_gastos()
    elif opcao == "2":
        adicionar_gasto()
    elif opcao == "3":
        excluir_gasto()
    elif opcao == "4":
        atualizar_gastos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")