# Lista Adjacencia

lista_adj = {}
direcional = False
def main():
    linhas = open("venv/grafo.txt", "r")
    count_linha = 0
    for linha in linhas:
        if count_linha == 0:
            vertices = linha.strip().split(",")
            numero_vertices = len(vertices)
            for i in range(0, numero_vertices):
                vertice = vertices[i]
                lista_adj[vertice] = []

        else:
            vertices = linha.strip().split("-")

            origem = vertices[0]
            destino = vertices[1]

            lista_adj[origem].append(destino)
            if direcional == False:
                lista_adj[destino].append(origem)


        count_linha += 1
    print(lista_adj)

if __name__ == '__main__':
    main()