print("Seja muito bem-vindo ao quiz dos Conhecimentos Bíblicos")
resposta_usuario = input("Quer começar o quiz? (S/N): ").strip().upper()

if resposta_usuario.upper() != "S":
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

if resposta_1 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

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

if resposta_2 == "B":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

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

if resposta_3 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

# PERGUNTA 4
print("Pergunta 4:")
print("""
QQuem derrotou o gigante Golias?

A) Davi
B) Salomão
C) Sansão
D) Josué
""")

resposta_4 = input("Resposta: ").strip().upper()

if resposta_4 == "A":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")


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

if resposta_5 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")


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

if resposta_6 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

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

if resposta_7 == "B":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

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

if resposta_8 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")


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

if resposta_9 == "B":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

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

if resposta_10 == "C":
    print("Certa resposta")
    score += 1

else:
    print("Resposta errada")

# PONTUAÇÃO
print("\nQuiz acabou!")
print(f"Você acertou {score} de 10 perguntas.")
print(f"Pontuação: {score}/10")
