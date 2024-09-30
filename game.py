import json

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
    print(json.dumps(question_dict, indent=4, ensure_ascii=False))

def get_user_response(questions_dict):
    answers_dict = {}
    return answers_dict

def check_answers(questions_dict, answers_dict):
    right_answers = 0
    return right_answers

def scores(right_answers):
    new_value=0
    return new_value

if __name__ == "__main__":
    questions = load_questions("questions.json")
    answers = get_user_response(questions)
    right_answers = check_answers(answers)
    print("A sua nota é: ", scores(right_answers))


