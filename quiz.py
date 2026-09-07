print("Seja muito bem-vindo ao quiz dos Conhecimentos Bíblicos")

resposta_usuario = input("Quer começar o quiz? (S/N): ").strip().upper()

if resposta_usuario != "S":
    quit()

score = 0
acertos = 0

print("Começando...")

perguntas = [
    {
        "pergunta": "Quantos livros tem na Bíblia?",
        "alternativas": ["A) 77", "B) 98", "C) 66", "D) 100"],
        "resposta": "C",
        "dificuldade": "Fácil",
    },
    {
        "pergunta": "Quem construiu a arca por ordem de Deus?",
        "alternativas": ["A) Moisés", "B) Noé", "C) Abraão", "D) Davi"],
        "resposta": "B",
        "dificuldade": "Fácil",
    },
    {
        "pergunta": "Qual foi o primeiro livro da Bíblia?",
        "alternativas": ["A) Êxodo", "B) Salmos", "C) Gênesis", "D) Mateus"],
        "resposta": "C",
        "dificuldade": "Fácil",
    },
    {
        "pergunta": "Quem derrotou o gigante Golias?",
        "alternativas": ["A) Davi", "B) Salomão", "C) Sansão", "D) Josué"],
        "resposta": "A",
        "dificuldade": "Fácil",
    },
    {
        "pergunta": "Qual era o nome da mãe de Jesus?",
        "alternativas": ["A) Marta", "B) Isabel", "C) Maria", "D) Raquel"],
        "resposta": "C",
        "dificuldade": "Fácil",
    },
    {
        "pergunta": "Quantos discípulos Jesus escolheu?",
        "alternativas": ["A) 7", "B) 10", "C) 12", "D) 14"],
        "resposta": "C",
        "dificuldade": "Médio",
    },
    {
        "pergunta": "Quem traiu Jesus por 30 moedas de prata?",
        "alternativas": ["A) Pedro", "B) Judas Iscariotes", "C) Tomé", "D) João"],
        "resposta": "B",
        "dificuldade": "Médio",
    },
    {
        "pergunta": "Qual foi o primeiro milagre de Jesus registrado no Evangelho de João?",
        "alternativas": [
            "A) Multiplicação dos pães",
            "B) Cura de um cego",
            "C) Transformação da água em vinho",
            "D) Ressurreição de Lázaro",
        ],
        "resposta": "C",
        "dificuldade": "Médio",
    },
    {
        "pergunta": "Quem recebeu os Dez Mandamentos de Deus?",
        "alternativas": ["A) Abraão", "B) Moisés", "C) Davi", "D) Josué"],
        "resposta": "B",
        "dificuldade": "Difícil",
    },
    {
        "pergunta": "Qual é o último livro da Bíblia?",
        "alternativas": ["A) Judas", "B) Atos", "C) Apocalipse", "D) Romanos"],
        "resposta": "C",
        "dificuldade": "Difícil",
    },
]

pontuacao_maxima = 0

for pergunta in perguntas:
    if pergunta["dificuldade"] == "Fácil":
        pontuacao_maxima += 1

    elif pergunta["dificuldade"] == "Médio":
        pontuacao_maxima += 2

    else:
        pontuacao_maxima += 3

for numero, pergunta in enumerate(perguntas, start=1):

    print(f"\nPergunta {numero}:")
    print(pergunta["pergunta"])
    print(f"Dificuldade: {pergunta['dificuldade']}")

    for alternativa in pergunta["alternativas"]:
        print(alternativa)

    resposta = input("Resposta: ").strip().upper()

    while resposta not in ["A", "B", "C", "D"]:
        print("Resposta inválida! Digite apenas A, B, C ou D.")
        resposta = input("Resposta: ").strip().upper()

    if pergunta["dificuldade"] == "Fácil":
        pontos = 1

    elif pergunta["dificuldade"] == "Médio":
        pontos = 2

    else:
        pontos = 3

    if resposta == pergunta["resposta"]:
        print(f"Correto! voce ganhou {pontos} ponto(s).")
        score += pontos
        acertos += 1
    else:
        print("Incorreto!")

    print(f"Pontuação: {score} pontos")

percentual = (score / pontuacao_maxima) * 100

print(f"Percentual: {percentual:.1f}%")

if percentual <= 20:
    print("Você precisa estudar um pouco mais!")

elif percentual <= 40:
    print("Bom trabalho! Continue estudando.")

elif percentual <= 60:
    print("Muito bom! Você conhece bastante!")

elif percentual <= 80:
    print("Excelente resultado!")

else:
    print("Perfeito! Você acertou todas!")


print("\nQuiz acabou!")

print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
print(f"Pontuação: {score} pontos")


gabarito = input("\nQuer ver o gabarito? (S/N): ").strip().upper()

if gabarito == "S":

    print("\n========== GABARITO ==========")

    for numero, pergunta in enumerate(perguntas, start=1):

        print(f"\nPergunta {numero}:")
        print(pergunta["pergunta"])

        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        print(f"Resposta correta: {pergunta['resposta']}")
