import json


class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            memoria.write('["Will", "Alfredo"]')
            memoria.close()
            memoria = open(nome + '.json', 'r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []

    def escuta(self):
        frase = str(input('> '))
        frase = frase.lower()
        return frase

    def pensa(self, frase):
        self.frases = {'oi': 'Olá, qual o seu nome? ', 'tchau': 'Tchau Tchau!'}

        if frase.lower() in self.frases:
            return self.frases[frase]

        # if frase == 'oi':
        #    return 'Olá, qual o seu nome?'
        if self.historico[-1] == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        # if frase.lower() == 'tchau':
        #    return 'Tchau Tchau..'
        return 'Não entendi...'

    def pegaNome(self, nome):
        nome = nome.lower()
        if 'o meu nome é' in nome:
            nome = nome[14:]
        return nome.title()

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'E aí '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            memoria = open(self.nome + '.json', 'w')
            json.dump(self.conhecidos, memoria)
            memoria.close()
        return frase + nome

    def fala(self, frase):
        print(frase)
        self.historico.append(frase)
