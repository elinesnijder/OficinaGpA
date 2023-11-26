def cria_novo_cliente():
    """pede e recebe do ultilizador os dados de um novo clientes, guarda-os numa lista e então
      devolve essa lista
    """
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

    