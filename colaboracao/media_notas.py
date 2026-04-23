# Desafio 6: Média Escolar
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")
print("Aprovado!" if media >= 7 else "Recuperação.")
