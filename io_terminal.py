from tabulate import tabulate

def imprime_lista(cabecalho, lista):
    print(cabecalho)
    if (len(lista) == 0):
        print("Lista vazia")
    else:
        lista_a_imprimir = [["id"] + list(lista[0].keys())]
        lista_a_imprimir.extend([[id] + list(d.values()) for id, d in enumerate(lista)])
        print(tabulate(lista_a_imprimir, headers="firstrow", tablefmt='psql'))

def pause():
    input("Pressione ENTER para continuar...")

def pergunta_id(questao, lista, mostra_lista=False):
    if mostra_lista:
        imprime_lista(cabecalho="", lista=lista)
    while True:
        id = int(input(questao))
        if 0 <= id < len(lista):
            return id
        else:
            print(f"id inexistente. Tente de novo. Valores admitidos {0} - {len(lista)}")