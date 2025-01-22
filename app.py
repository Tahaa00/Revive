from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure for symptoms and follow-up questions
symptoms_data = {
    'headache': {
        'questions': [
            {
                'question': 'Is the headache severe?',
                'answers': {
                    'yes': 'You might have a migraine. Consider seeing a doctor.',
                    'no': 'Try resting and drinking water.'
                }
            }
        ]
    },
    'fever': {
        'questions': [
            {
                'question': 'Do you have chills?',
                'answers': {
                    'yes': 'You might have the flu. Consider seeing a doctor.',
                    'no': 'Monitor your temperature and rest.'
                }
            }
        ]
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_symptom = request.form.get('symptom')
        return redirect(url_for('questions', symptom=selected_symptom))
    return render_template('index.html', symptoms=symptoms_data.keys())

@app.route('/questions/<symptom>', methods=['GET', 'POST'])
def questions(symptom):
    if symptom not in symptoms_data:
        return redirect(url_for('index'))

    questions = symptoms_data[symptom]['questions']
    if request.method == 'POST':
        answer = request.form.get('answer')
        return render_template('solution.html', solution=questions[0]['answers'][answer])

    return render_template('questions.html', symptom=symptom, question=questions[0]['question'], answers=questions[0]['answers'].keys())

if __name__ == '__main__':
    app.run(debug=True) 