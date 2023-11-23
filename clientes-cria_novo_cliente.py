def cria_novo_cliente():
    nome = input('Nome Completo: ')
    numero = input('Número de Contato: ')
    morada = input('Morada: ')
    Nmorada =input('Nº de morada: ')
    cp = input('Código Postal: ')
    nif = input('NIF: ')
    mail = input('Email: ')

    N_cliente = (f" Nome: {nome}\n Número de Contato: {numero}\n Morada: {morada}\n Nº de Morada: {Nmorada}\n Código Postal: {cp}\n NIF: {nif}\n Email: {mail}")
    
    return N_cliente