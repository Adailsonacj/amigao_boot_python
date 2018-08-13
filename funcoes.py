def resposta():
    resp = str(input('> '))
    resp = resp.upper()
    return resp


def pegaNome(nome):
    if 'O MEU NOME É' in nome.upper():
        nome = nome[13:]
    return nome.title()


def respondeNome(nome):
    return 'Muito prazer ' + nome

