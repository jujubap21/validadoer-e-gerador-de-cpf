import random
import re

print(
    "==========================================\n||      VALIDADOR E GERADOR DE CPF      ||\n=========================================="
)
print("O que deseja fazer?")


def validador():
    numeros = [int(digito) for digito in cpf if digito.isdigit()]

    formatacao = False
    quantidade_de_digitos = False
    primeira_validacao = False
    segunda_validacao = False

    if re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf):
        formatacao = True

    if len(numeros) == 11:
        quantidade_de_digitos = True

        soma_produtos = sum(a * b for a, b in zip(numeros[0:9], range(10, 1, -1)))
        digito_esperado = (soma_produtos * 10 % 11) % 10
        if numeros[9] == digito_esperado:
            primeira_validacao = True

        soma_produtos1 = sum(a * b for a, b in zip(numeros[0:10], range(11, 1, -1)))
        digito_esperado1 = (soma_produtos1 * 10 % 11) % 10
        if numeros[10] == digito_esperado1:
            segunda_validacao = True

        if (
            quantidade_de_digitos == True
            and formatacao == True
            and primeira_validacao == True
            and segunda_validacao == True
        ):
            print(
                f"------------------------------------------\nO CPF {cpf} é válido.\n------------------------------------------"
            )
        else:
            print(
                f"------------------------------------------\nO CPF {cpf} não é válido.\n------------------------------------------"
            )

    else:
        print(
            print(
                f"------------------------------------------\nO CPF {cpf} não é válido.\n------------------------------------------"
            )
        )


def gerador():
    while True:
        cpf = [random.randint(0, 9) for i in range(9)]
        if cpf != cpf[::-1]:
            break

    for i in range(9, 11):
        value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        cpf.append(digit)

    result = "".join(map(str, cpf))
    return result


escolha = int(
    input("1. Validar um CPF \n2. Gerar um CPF \n3. Sair \nDigite a sua escolha: ")
)
if escolha == 1:
    cpf = input("Digite um CPF: ")
    validador()
elif escolha == 2:
    cpf = gerador()
    print(
        f"------------------------------------------\nO CPF gerado é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n------------------------------------------"
    )
elif escolha == 3:
    quit

while escolha != 3:
    print("O que deseja fazer?")
    escolha = int(
        input("1. Validar um CPF \n2. Gerar um CPF \n3. Sair \nDigite a sua escolha: ")
    )
    if escolha == 1:
        cpf = input("Digite um CPF: ")
        validador()
    elif escolha == 2:
        cpf = gerador()
        print(
            f"------------------------------------------\nO CPF gerado é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n------------------------------------------"
        )
    elif escolha == 3:
        break
