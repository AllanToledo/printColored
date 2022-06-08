from random import Random

anteriores: list[str] = list()

for i in range(5):
    tentativa = input("Tentativa: ")
    resultado = ""
    for letra in tentativa:  # pega cada letra
        # processa a letra e adiciona a cor
        # .upper() -> transforma em maiúscula, não pode ser no resultado final, por que se não ele
        # perde os códigos de cores, então ao adicionar a letra eu já transformo para maiúscula
        resultado += f"\033[{Random().randint(31, 33)}m{letra.upper()}\033[0m"
    anteriores.append(resultado)  # adiciona o resultado na lista
    for anterior in anteriores:  # mostra tentativas anteriores (incluindo a nova)
        print(anterior)


        
