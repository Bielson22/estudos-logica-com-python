# Desafio 7: Gerador de Senhas
import random
import string

tamanho = int(input("Digite o tamanho da senha desejada: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for i in range(tamanho))

print(f"Sua senha segura: {senha}")
