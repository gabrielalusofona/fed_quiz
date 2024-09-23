import json

print("Inserting questions into questions_dict...")
# Load json file
with open('questions.json', 'r') as file:
    data = json.load(file)
    
# Create a question dictionary with only the questions
question_dict = {
    # List comprehension
    # [ expression for a_value in a_collection if condition ]
    f"Q{i+1}": item["Question"] for i, item in enumerate(data["questions"])
}

print("Questions successfully inserted into questions_dict")