import numpy as np

# Função para ler um vetor de dimensão qualquer
def ler_vetor(nome, dim=None):
    while True:
        try:
            valores = list(map(float, input(f"Digite as coordenadas do vetor {nome} separadas por espaço ou vírgula: ").replace(',', ' ').split()))
            if dim is not None and len(valores) != dim:
                print(f"Você deve digitar exatamente {dim} números.")
                continue
            return np.array(valores)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

# Função para soma e subtração de vetores
def soma_subtracao(v1, v2):
    return v1 + v2, v1 - v2

# Função para produto escalar
def produto_escalar(v1, v2):
    return np.dot(v1, v2)

# Função para produto misto (produto vetorial seguido de escalar)
def produto_misto(a, b, c):
    return np.dot(a, np.cross(b, c))

# === Programa Principal ===

print("=== Operações com Vetores ===\n")

# Adição e Subtração
print(">>> Adição e Subtração de Vetores")
vet1 = ler_vetor('1')
vet2 = ler_vetor('2')
if len(vet1) != len(vet2):
    print("Erro: Os vetores devem ter o mesmo número de dimensões.")
else:
    soma, sub = soma_subtracao(vet1, vet2)
    print("Resultado da Adição:", soma)
    print("Resultado da Subtração:", sub)

# Produto Escalar
print("\n>>> Produto Escalar")
vet1 = ler_vetor('1')
vet2 = ler_vetor('2')
if len(vet1) != len(vet2):
    print("Erro: Os vetores devem ter o mesmo número de dimensões.")
else:
    escalar = produto_escalar(vet1, vet2)
    print("Resultado do Produto Escalar:", escalar)

# Produto Misto
print("\n>>> Produto Misto (a · (b × c))")
a = ler_vetor('a', 3)
b = ler_vetor('b', 3)
c = ler_vetor('c', 3)
misto = produto_misto(a, b, c)
print("Resultado do Produto Misto:", misto)
