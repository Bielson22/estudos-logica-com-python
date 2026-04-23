# Projeto Open Source Simulado
# Este script recebe contribuições da comunidade

def saudar_usuario(nome):
    return f"Olá, {nome}! Bem-vindo ao projeto Open Source."

def calcular_contribuicao(commits):
    # Simulação de lógica que pode ser expandida por outros devs
    return commits * 10

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudar_usuario(nome))
