# Matriz Adjacencia

matriz = []
def main():
    linhas = open("venv/grafo.txt", "r")
    count_linha = 0
    for linha in linhas:
        # print(linha)
        if count_linha == 0:
            numero_vertices = len(linha.strip().split(","))
            print(linha)
            print(numero_vertices)
            # print(numero_vertices)
            for i in range(0, numero_vertices):
                lista = []
                for x in range(0, numero_vertices):
                    lista.append(0)
                matriz.append(lista)
                # matriz.append([0 for _ in range(0, numero_vertices)])
        count_linha += 1

    else:
        vertices = linha.strip().split("-")
        origem = vertices[0]
        destino = vertices[1]
        print(origem)
        print(destino)

    count_linha += 1

    # for i in range(0, numero_vertices):
    #    print(matriz[i])

if __name__ == '__main__':
    main()


