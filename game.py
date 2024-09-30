import json
import random

def load_questions(file_path):
    print("Inserting questions into questions_dict...")
    # Load json file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Crear un diccionario a partir de los datos
    question_dict = {
        f"Q{i + 1}": {
            "question": item["Question"],
            "options": item["options"],
            "answer": item.get("answer") or item.get("Resposta")  # manejar 'answer' o 'Resposta'
        }
        for i, item in enumerate(data)
    }

    # Imprimir el diccionario con formato legible
    return question_dict

def get_user_response(questions_dict):
    perguntas_selecionadas = random.sample(list(questions_dict.items()), 5) #isto vai dar q1,q3,q7,q2 etc

    respostas = {}

    for i in perguntas_selecionadas: #o i é um desses q1, q2, etc, que são a key do dicionario
        questao_idx = i[0]
        questao_escrita = i[1]['question']

        opcoes_idx = i[1]
        opcoes_escritas = i[1]['options']

        resposta = input(f"{questao_escrita}\ {opcoes_escritas}\ Introduza a sua resposta: ")

        respostas[questao_idx] = resposta

    return respostas

def check_answers(questions_dict, answers_dict):
    right_answers = 0

    for i in answers_dict: #o i é um desses q1, q2, etc, que são a key do dicionario
        questao_idx = i[0]
        answer = answers_dict[i]
        right_answer = questions_dict[i]['answer'][0]
        if answer == right_answer:
            right_answers+=1
    return right_answers

def scores(right_answers):
    total = 5
    final_score = (right_answers / total) * 20
    return final_score


if __name__ == "__main__":
    questions = load_questions("questions.json")
    answers = get_user_response(questions)
    right_answers = check_answers(questions, answers)
    print("O seu resultado é é: ", scores(right_answers))


