import random

def get_user_response(questions_dict):
    perguntas_selecionadas = random.sample(list(questions_dict.items()), 5) #isto vai dar q1,q3,q7,q2 etc

    respostas = {}

    for i in perguntas_selecionadas: #o i é um desses q1, q2, etc, que são a key do dicionario
        questao_idx = i[0]
        questao_escrita = i[1]['question']

        opcoes_idx = i[1]
        opcoes_escritas = i[1]['options']

        resposta = input(f"{questao_escrita}\ {opcoes_escritas}\ Introduza a sua resposta: ")

        respostas[questao_escrita[i]] = resposta

    return respostas

