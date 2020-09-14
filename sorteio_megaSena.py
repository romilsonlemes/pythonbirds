import random
numeros_sorteados = []
for ps in range(1,16):
    try:
        #numero = random.randint(1,25) // LotoFacil
        numeros_sorteados.append(random.randint(1,25))
        # print(ps, numero)
    except ValueError:
        print('Ocorreu um erro nos numeros sorteados.')

numeros_sorteados.sort()
print(f'Numeros Sorteados:  {numeros_sorteados}')
