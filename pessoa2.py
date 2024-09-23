import json

print("Inserting questions into questions_dict...")
# Load json file
with open('questions.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
# Crear un diccionario a partir de los datos
question_dict = {
    f"Q{i+1}": {
        "question": item["Question"],
        "options": item["options"],
        "answer": item.get("answer") or item.get("Resposta")  # manejar 'answer' o 'Resposta'
    }
    for i, item in enumerate(data)
}

# Imprimir el diccionario con formato legible
print(json.dumps(question_dict, indent=4, ensure_ascii=False))