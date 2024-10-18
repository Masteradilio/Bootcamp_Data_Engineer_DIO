# Sistema Bancário

import textwrap

def menu():
    menu = '''\n
=============== MENU ===============
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''
    return input(textwrap.dedent(menu)).lower()

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: R$"))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: \tR$ {saldo:.2f}")
    print("======================================")

def main():
    LIMITE_SAQUES = 3
    LIMITE_SAQUE_VALOR = 500.00

    saldo = 0.0
    limite = LIMITE_SAQUE_VALOR
    extrato = ""
    numero_saques = 0

    while True:
        opcao = menu()
        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'q':
            print("Obrigado por utilizar nossos serviços!")
            break
        else:
            print("Operação inválida! Por favor, selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
