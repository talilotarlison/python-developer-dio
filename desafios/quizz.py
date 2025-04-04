questoes_acertadas = 0;
# https://www.freecodecamp.org/portuguese/news/o-metodo-index-para-listas-em-python-como-obter-o-indice-de-um-item-em-uma-lista/
perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "respostas": [
            {"opcao": "Paris", "correto": True},
            {"opcao": "Londres", "correto": False},
            {"opcao": "Berlim", "correto": False}
        ]
    },
    {
        "pergunta": "Qual é a fórmula química da água?",
        "respostas": [
            {"opcao": "H2O", "correto": True},
            {"opcao": "CO2", "correto": False},
            {"opcao": "O2", "correto": False}
        ]
    },
    {
        "pergunta": "Quem escreveu 'Dom Casmurro'?",
        "respostas": [
            {"opcao": "Machado de Assis", "correto": True},
            {"opcao": "José de Alencar", "correto": False},
            {"opcao": "Clarice Lispector", "correto": False}
        ]
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "respostas": [
            {"opcao": "Júpiter", "correto": False},
            {"opcao": "Saturno", "correto": False},
            {"opcao": "Terra", "correto": True}
        ]
    },
    {
        "pergunta": "Qual é a moeda oficial do Japão?",
        "respostas": [
            {"opcao": "Iene", "correto": True},
            {"opcao": "Won", "correto": False},
            {"opcao": "Dólar", "correto": False}
        ]
    }
]

def verifica_alternativa_correta(questoes,alternativa):
    global questoes_acertadas;
    for questao in questoes:
        if questoes.index(questao) == alternativa:
            if questao["correto"] == True:
                questoes_acertadas = questoes_acertadas + 1;
        

def start_quizz():
    for index in range(len(perguntas)):
        placar_questoes(index,len(perguntas));
        print(perguntas[index]["pergunta"]);
        for resposta in perguntas[index]["respostas"]:
            print(f'{perguntas[index]["respostas"].index(resposta)} - {resposta["opcao"]}')
            #(resposta["correto"])
        resposta = int(input("Qual alternativa correta?"))
        verifica_alternativa_correta(perguntas[index]["respostas"],resposta)

def placar_questoes(index, total_questoes):
    print(f"Questao {index + 1 } / {total_questoes}")

def verifica_aprovacao(nota):
   return True if nota >=3 else False


def main():
    print("Prova de conhecimentos Gerais.")
    start_quizz();
    print("Fim do teste, Seu resultado foi:")
    print(f'Questoes acertadas: {questoes_acertadas}')
    resultado = 'Aprovado' if verifica_aprovacao(questoes_acertadas) else 'Reprovado';
    print(f'Voce foi: {resultado}')
    exit()
    return 0;

main()
