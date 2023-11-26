import pickle

from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas

from veiculos import nome_ficheiro_lista_de_veiculos

def carrega_as_listas_dos_ficheiros():

    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return  lista_de_veiculos, lista_de_clientes, lista_de_faturas

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):

    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")



