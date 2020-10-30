# o programa faz a letra 'R' percorrer um tabuleiro, de acordo a escolha do usuário,
# d (direita), e (esquerda), c (cima), b(baixo).

class movimento:
    def direita(self):
        for p, chao in enumerate(cenario):
            for i, v in enumerate(chao):
                if v == 'R':
                    try:
                        chao[i] = '_'
                        chao[i+1] = 'R'
                        break
                    except:
                        chao[i] = 'R'
                        print('\nVocê encontrou uma parede! Não é possivel avançar nesta direção\n')
                        return cenario
            if cenario[p][i] == 'R':
                break
        return cenario

    def esquerda(self):
        for p, chao in enumerate(cenario):
            for i, v in enumerate(chao):
                if v == 'R':
                    if v in chao[0]:
                        print('\nVocê encontrou uma parede! Não é possivel avançar nesta direção\n')
                    else:
                        chao[i] = '_'
                        chao[i-1] = 'R'
                        break
            if cenario[p][i-1] == 'R':
                break
        return cenario

    def cima(self):
        for p, chao in enumerate(cenario):
            for i, v in enumerate(chao):
                if v == 'R':
                    if v in cenario[0]:
                        print('\nVocê encontrou o Teto! Não é possivel avançar nesta direção\n')
                    else:
                        chao[i] = '_'
                        cenario[p-1][i] = 'R'
                        break
            if cenario[p-1][i] == 'R':
                break
        return cenario

    def baixo(self):
        for p, chao in enumerate(cenario):
            for i, v in enumerate(chao):
                if v == 'R':
                    try:
                        chao[i] = '_'
                        cenario[p+1][i] = 'R'
                        break
                    except:
                        cenario[p][i] = 'R'
                        print('\nVocê encontrou o chão! Não é possivel avançar nesta direção\n')
                        return cenario
            if cenario[p+1][i] == 'R':
                break
        return cenario

    def acao(self,a):
        self.a = a
        if a == 'd':
            self.direita()
        elif a == 'b':
            self.baixo()
        elif a == 'e':
            self.esquerda()
        elif a == 'c':
            self.cima()


cenario = [['R','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_'],
           ['_','_','_','_']]

jogada = movimento()
while True:
    for i in cenario:
        print(i)
    a = input('Digite uma ação: \nd(p/ direita) e(p/ esquerda) \nb(p/ baixo) c(p/ cima) x(p/ sair): ').strip().lower()
    if a == 'x':
        break
    jogada.acao(a)

