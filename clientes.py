from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"

def cria_novo_cliente():

    nome = input('Nome Completo: ')
    numero = input('Número de Contato: ')
    morada = input('Morada: ')
    Nmorada =input('Nº de morada: ')
    cp = input('Código Postal: ')
    nif = input('NIF: ')
    mail = input('Email: ')

    novo_cliente = {"Nome": nome,
                    "Número de Contato": numero,
                    "Morada": morada,
                    "Nº de Morada": Nmorada,
                    "Código Postal": cp,
                    "NIF": nif,
                    "Email": mail}
    
    return novo_cliente

def imprime_lista_de_clientes(lista_de_clientes):

  imprime_lista(cabecalho="Lista de Clientes", lista=lista_de_clientes)