import json
import subprocess as s


class Chatbot():
    def __init__(self, nome):
        try:
            memoria = open(nome + '.json', 'r')
        except FileNotFoundError:
            memoria = open(nome + '.json', 'w')
            memoria.write('[["Will", "Alfredo"],{"oi": "Olá, qual o seu nome?", "tchau": "Tchau Tchau!"}]')
            memoria.close()
            memoria = open(nome + '.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None, ]

    def escuta(self, frase=None):
        if frase == None:
            frase = input('>: ')
        frase = str(frase)
        # frase = str(input('> '))
        frase = frase.lower()
        return frase

    def pensa(self, frase):

        if frase.lower() in self.frases:
            aaa = self.frases[frase]
            return aaa

        if frase.lower() == 'aprende':
            return 'Digite a frase: '
        # Responde frases que dependem do histórico
        ultimaFrase = self.historico[-1]
        if ultimaFrase == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Digite a frase: ':
            self.chave = frase
            return 'Digite a resposta: '
        if ultimaFrase == 'Digite a resposta: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido!'

        try:
            resp = str(eval(frase))
            return resp
        except:
            pass
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
            self.gravaMemoria()

        return frase + nome

    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):
        if 'executa' in frase:
            comando = frase.replace('executa', '')
            try:
                s.Popen(comando)
            except FileNotFoundError:
                s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)
