# Armazenar nome e profissão do usuário
nome = input("Digite seu nome: ")
profissao = input("Digite sua profissão: ")

# Se a profissão for "Estudante", perguntar onde estuda
if profissao.lower() == "estudante":
    faculdade_escola = input("Em qual faculdade/escola você estuda? ")
    print(f"O usuário {nome} é um {profissao} e estuda na instituição {faculdade_escola}.")
else:
    print(f"O usuário {nome} é um {profissao}.")
