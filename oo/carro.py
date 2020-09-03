"""
Você deve criar uma classe carro que vai possuir dois atributos copostos por outras duas classes:

1º Motor
2º Direção
-> O motor terá a responsabilidade de controlar a velocidade.
   Ele oferece os seguintes atributos:
   1º Atributo de dado velocidade
   2º Método acelerar, que deverá incrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ele oferece os seguintes atributos:
   1º Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste.
   2º Método girar a direita
   3º Método girar a esquerda

         N
       O   L
         S

        Exemplo:
        # Testando o Motor
        >>> motor = Motor()
        >>> motor.velocidade
        0
        >>> motor.acelerar()
        >>> motor.velocidade
        1
        >>> motor.acelerar()
        >>> motor.velocidade
        2
        >>> motor.acelerar()
        >>> motor.velocidade
        3
        >>> motor.frear()
        >>> motor.velocidade
        1
        >>> motor.frear()
        >>> motor.velocidade
        0
        >>> # Testando  Direção
        >>> direcao = Direcao()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_direita()
        >>> direcao.valor
        'Norte'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Oeste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Sul'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Leste'
        >>> direcao.girar_a_esquerda()
        >>> direcao.valor
        'Norte'
        >>> carro = Carro(direcao, motor)
        >>> carro.calcular_velocidade
        0
        >>> carro.acelerar()
        >>> carro.calcular_velocidade
        1
        >>> carro.acelerar()
        >>> carro.calcular_velocidade
        2
        >>> carro.frear()
        >>> carro.calcular_velocidade
        0
        >>> carro.calcular_direcao()
        >>> 'Norte'
        >>> carro.girar_a_direita()
        >>> carro.girar_a_direcao()
        >>> 'Leste'
        >>> carro.girar_a_esquerda()
        >>> carro.girar_a_direcao()
        >>> 'Norte'
        >>> carro.girar_a_esquerda()
        >>> carro.girar_a_direcao()
        >>> 'Oeste'
        >>> carro.girar_a_esquerda()
        >>> carro.girar_a_direcao()
        >>> 'Sul'

"""
NORTE = 'Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao:
    rotacao_a_direita_dct = {
            NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
        }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        #self.valor= self.rotacao_a_direita_dct[self.valor]
        if self.valor   == NORTE:
            self.valor  = LESTE
        elif self.valor == LESTE:
            self.valor  = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


