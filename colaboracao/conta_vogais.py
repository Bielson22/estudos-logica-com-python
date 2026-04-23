# Desafio 8: Contador de Vogais
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = sum(1 for letra in frase if letra in vogais)

print(f"A frase contém {contador} vogais.")
