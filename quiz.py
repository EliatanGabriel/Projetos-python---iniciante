print("Seja muito bem-vindo ao quiz dos Conhecimentos Bíblicos")

resposta_usuario = input("Quer começar o quiz? (S/N): ").strip().upper()

if resposta_usuario != "S":
    quit()

score = 0

print("Começando...")

perguntas = [
    "Quantos livros tem na Bíblia?",
    "Quem construiu a arca por ordem de Deus?",
    "Qual foi o primeiro livro da Bíblia?",
    "Quem derrotou o gigante Golias?",
    "Qual era o nome da mãe de Jesus?",
    "Quantos discípulos Jesus escolheu?",
    "Quem traiu Jesus por 30 moedas de prata?",
    "Qual foi o primeiro milagre de Jesus registrado no Evangelho de João?",
    "Quem recebeu os Dez Mandamentos de Deus?",
    "Qual é o último livro da Bíblia?"
]

respostas_corretas = [
    "C",
    "B",
    "C",
    "A",
    "C",
    "C",
    "B",
    "C",
    "B",
    "C"
]

alternativas = [
    ["A) 77", "B) 98", "C) 66", "D) 100"],
    ["A) Moisés", "B) Noé", "C) Abraão", "D) Davi"],
    ["A) Êxodo", "B) Salmos", "C) Gênesis", "D) Mateus"],
    ["A) Davi", "B) Salomão", "C) Sansão", "D) Josué"],
    ["A) Marta", "B) Isabel", "C) Maria", "D) Raquel"],
    ["A) 7", "B) 10", "C) 12", "D) 14"],
    ["A) Pedro", "B) Judas Iscariotes", "C) Tomé", "D) João"],
    ["A) Multiplicação dos pães", "B) Cura de um cego", "C) Transformação da água em vinho", "D) Ressurreição de Lázaro"],
    ["A) Abraão", "B) Moisés", "C) Davi", "D) Josué"],
    ["A) Judas", "B) Atos", "C) Apocalipse", "D) Romanos"]
]

for numero, pergunta in enumerate(perguntas, start=1):

    print(f"\nPergunta {numero}:")
    print(pergunta)

    for alternativa in alternativas[numero - 1]:
        print(alternativa)

    resposta = input("Resposta: ").strip().upper()

    while resposta not in ["A", "B", "C", "D"]:
        print("Resposta inválida! Digite apenas A, B, C ou D.")
        resposta = input("Resposta: ").strip().upper()

    if resposta == respostas_corretas[numero - 1]:
        print("Correto!")
        score += 1
    else:
        print("Incorreto!")

    print(f"Pontuação atual: {score}/{numero}")

print("\nQuiz acabou!")
print(f"Você acertou {score} de {len(perguntas)} perguntas.")
print(f"Pontuação: {score}/{len(perguntas)}")

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
