# (ALGORITMO DE DIJKSTRA - CAP 7 - PG 156)
# É usado para encontrar o caminho mais curto de um nó inicial para todos os outros nós em um grafo.
# Encontrar o caminho mais curto em um grafo ponderado, onde os pesos das arestas representam custos ou distâncias. 


# Representar as arestas e seus pesos no grafo
grafo['inicio'] = {} # Tabela hash para armazenar os vizinhos do nó inicial (basicamente guarda outras tabelas hash)
grafo['inicio']['A'] = 6
grafo['inicio']['B'] = 2

# Visualizar todos os vizinhos do nó inicial
print grafo['inicio'].keys()  # Saída: ['A', 'B']

# Visualizar os pesos das arestas (do nó inicial para seus vizinhos)
print(grafo['inicio']['A'])  # Saída: 6 -> Peso da aresta do nó 'inicio' para o nó 'A'
print(grafo['inicio']['B'])  # Saída: 2 -> Peso da aresta do nó 'inicio' para o nó 'B'


# Adicionar o restante dos vétices e seus vizinhos ao grafo
grafo['A'] = {} # Tabela hash, vizinhos de A
grafo['A']['fim'] = 1
grafo['B'] = {} # Tabela hash, vizinhos de B
grafo['B']['A'] = 3
grafo['B']['fim'] = 5
grafo['fim'] = {} # Não tem vizinhos, pois é o nó final


# Precisamos de mais uma tabela hash para armazenar os custos de cada nó a partir do nó inicial
infinito = float("inf") # Representa um valor infinito para nós que ainda não

custos = {} # Tabela hash para armazenar os custos de cada nó a partir do nó inicial
custos['A'] = 6
custos['B'] = 2
custos['fim'] = infinito


# Precisamos de mais uma tabela hash para armazenar os pais de cada nó
pais = {} # Tabela hash para armazenar os pais de cada nó
pais['A'] = 'inicio'
pais['B'] = 'inicio'
pais['fim'] = None # O nó final não tem pai

# Precisamos de uma lista para armazenar os nós já processados
processados = [] # Lista para armazenar os nós já processados

nodo = ache_no_custo_mais_baixo(custos) # Função que encontra o nó com o menor custo ainda não processado (o "relaxado")
while nodo is not None: # Enquanto houver nós a serem processados (ou seja, nem todos os nós foram processados)
    custo = custos[nodo] # Obter o custo do nó atual
    vizinhos = grafo[nodo] # Obter os vizinhos do nó atual
    for n in vizinhos.keys(): # Para cada vizinho do nó atual
        novo_custo = custo + vizinhos[n] # Calcular o novo custo para o vizinho
        if custos[n] > novo_custo: # Se o novo custo for menor que o custo atual do vizinho
            custos[n] = novo_custo # Atualizar o custo do vizinho
            pais[n] = nodo # Atualizar o pai do vizinho
    processados.append(nodo) # Marcar o nó atual como processado
    nodo = ache_no_custo_mais_baixo(custos) # Encontrar o próximo nó com o menor custo ainda não processado


def ache_no_custo_mais_baixo(custos):
    menor_custo = float("inf") # Inicializar o menor custo como infinito
    nodo_mais_barato = None # Inicializar o nó mais barato como None
    for nodo in custos: # Para cada nó nos custos
        custo = custos[nodo] # Obter o custo do nó
        if custo < menor_custo and nodo not in processados: # Se o custo for menor que o menor custo e o nó não foi processado
            menor_custo = custo # Atualizar o menor custo
            nodo_mais_barato = nodo # Atualizar o nó mais barato
    return nodo_mais_barato # Retornar o nó mais barato encontrado