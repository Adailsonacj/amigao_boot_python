from funcoes import *

print('Olá, qual é o seu nome?')

nome = pegaNome(resposta())
resp = respondeNome(nome)

print(resp)

while True:
    resp = resposta()
    if resp == 'TCHAU':
        break
    else:
        print('Digite outra coisa')
print('Tchau tchau!')
