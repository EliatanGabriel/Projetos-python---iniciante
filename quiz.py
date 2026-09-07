print("Seja muito bem-vindo ao quiz dos Conhecimentos Bíblicos")
resposta_usuario = input("Quer começar o quiz? (S/N): ").strip().upper()

if resposta_usuario != "S":
    quit()

score = 0

print("Começando... \n")

# PERGUNTA 1
print("Pergunta 1:")
print("""
Quantos livros tem na Bíblia?

A) 77
B) 98
C) 66
D) 100
""")

resposta_1 = input("Resposta: ").strip().upper()

while resposta_1 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_1 = input("Resposta: ").strip().upper()

if resposta_1 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta era C) 66")

print(f"Pontuação atual: {score}/1")

# PERGUNTA 2
print("Pergunta 2:")
print("""
Quem construiu a arca por ordem de Deus?

A) Moisés
B) Noé
C) Abraão
D) Davi
""")

resposta_2 = input("Resposta: ").strip().upper()

while resposta_2 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_2 = input("Resposta: ").strip().upper()

if resposta_2 == "B":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é B) Noé")

print(f"Pontuação atual: {score}/2")

# PERGUNTA 3
print("Pergunta 3:")
print("""
Qual foi o primeiro livro da Bíblia?

A) Êxodo
B) Salmos
C) Gênesis
D) Mateus
""")

resposta_3 = input("Resposta: ").strip().upper()

while resposta_3 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_3 = input("Resposta: ").strip().upper()

if resposta_3 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é C) Gênesis")

print(f"Pontuação atual: {score}/3")

# PERGUNTA 4
print("Pergunta 4:")
print("""
Quem derrotou o gigante Golias?

A) Davi
B) Salomão
C) Sansão
D) Josué
""")

resposta_4 = input("Resposta: ").strip().upper()

while resposta_4 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_4 = input("Resposta: ").strip().upper()

if resposta_4 == "A":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é A) Davi")

print(f"Pontuação atual: {score}/4")


# PERGUNTA 5
print("Pergunta 5:")
print("""
Qual era o nome da mãe de Jesus?

A) Marta
B) Isabel
C) Maria
D) Raquel
""")

resposta_5 = input("Resposta: ").strip().upper()

while resposta_5 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_5 = input("Resposta: ").strip().upper()

if resposta_5 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é C) Maria")

print(f"Pontuação atual: {score}/5")


# PERGUNTA 6
print("Pergunta 6:")
print("""
Quantos discípulos Jesus escolheu?

A) 7
B) 10
C) 12
D) 14
""")

resposta_6 = input("Resposta: ").strip().upper()

while resposta_6 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_6 = input("Resposta: ").strip().upper()

if resposta_6 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é C) 12")

print(f"Pontuação atual: {score}/6")

# PERGUNTA 7
print("Pergunta 7:")
print("""
Quem traiu Jesus por 30 moedas de prata?

A) Pedro
B) Judas Iscariotes
C) Tomé
D) João
""")

resposta_7 = input("Resposta: ").strip().upper()

while resposta_7 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_7 = input("Resposta: ").strip().upper()

if resposta_7 == "B":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é B) Judas Iscariotes")

print(f"Pontuação atual: {score}/7")

# PERGUNTA 8
print("Pergunta 8:")
print("""
Qual foi o primeiro milagre de Jesus registrado no Evangelho de João?

A) Multiplicação dos pães
B) Cura de um cego
C) Transformação da água em vinho
D) Ressurreição de Lázaro
""")

resposta_8 = input("Resposta: ").strip().upper()

while resposta_8 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_8 = input("Resposta: ").strip().upper()

if resposta_8 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é C) Transformação da água em vinho")

print(f"Pontuação atual: {score}/8")

# PERGUNTA 9
print("Pergunta 9:")
print("""
Quem recebeu os Dez Mandamentos de Deus?

A) Abraão
B) Moisés
C) Davi
D) Josué
""")

resposta_9 = input("Resposta: ").strip().upper()

while resposta_9 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_9 = input("Resposta: ").strip().upper()

if resposta_9 == "B":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é B) Moisés")

print(f"Pontuação atual: {score}/9")

# PERGUNTA 10
print("Pergunta 10:")
print("""
Qual é o último livro da Bíblia?

A) Judas
B) Atos
C) Apocalipse
D) Romanos
""")

resposta_10 = input("Resposta: ").strip().upper()

while resposta_10 not in ["A", "B", "C", "D"]:
    print("Resposta inválida! Digite apenas A, B, C ou D.")
    resposta_10 = input("Resposta: ").strip().upper()

if resposta_10 == "C":
    print("Correto")
    score += 1

else:
    print("Incorreto")
    print("A resposta correta é C) Apocalipse")

print(f"Pontuação atual: {score}/10")

# PONTUAÇÃO
print("\nQuiz acabou!")
print(f"Você acertou {score} de 10 perguntas.")
print(f"Pontuação: {score}/10")

if score <= 3:
    print("Você precisa estudar um pouco mais!")

elif score <= 6:
    print("Bom trabalho! Continue estudando.")

elif score <= 8:
    print("Muito bom! Você conhece bastante!")

elif score == 9:
    print("Excelente resultado!")

else:
    print("Perfeito! Você acertou todas!")
