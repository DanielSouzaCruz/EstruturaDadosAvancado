# Matriz Adjacencia

indices = {}
matriz = []
direcional = True
def main():
    linhas = open("venv/grafo.txt", "r")
    count_linha = 0
    for linha in linhas:
        if count_linha == 0:
            vertices = linha.strip().split(",")
            numero_vertices = len(vertices)
            for i in range(0, numero_vertices):
                vertice = vertices[i]
                indices[vertice] = i
                lista = []
                for x in range(0, numero_vertices):
                    lista.append(0)
                matriz.append(lista)
        else:
            vertices = linha.strip().split("-")

            origem = vertices[0]
            destino = vertices[1]
            peso = int(vertices[2])

            indice_origem = indices[origem]
            indice_destino = indices[destino]

            matriz[indice_origem][indice_destino] = peso
            if direcional == False:
                matriz[indice_destino][indice_origem] = peso

        count_linha += 1

    print(indices)


    for i in range(0, numero_vertices):
        print(matriz[i])

if __name__ == '__main__':
    main()



