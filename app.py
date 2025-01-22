from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for symptoms and questions
symptoms = {
    "headache": [
        {"question": "Is the pain severe?", "answers": ["Yes", "No"]},
        {"question": "Do you have a fever?", "answers": ["Yes", "No"]}
    ],
    "cough": [
        {"question": "Is it a dry cough?", "answers": ["Yes", "No"]},
        {"question": "Do you have a sore throat?", "answers": ["Yes", "No"]}
    ]
}

solutions = {
    "headache": "Take a pain reliever and rest.",
    "cough": "Stay hydrated and rest."
}

@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms.keys())

@app.route('/questions', methods=['POST'])
def get_questions():
    symptom = request.json.get('symptom')
    return jsonify(symptoms.get(symptom, []))

@app.route('/solution', methods=['POST'])
def get_solution():
    symptom = request.json.get('symptom')
    # Logic to deduce condition and solution can be expanded here
    return jsonify({"solution": solutions.get(symptom, "Consult a doctor.")})

if __name__ == '__main__':
    app.run(debug=True) 