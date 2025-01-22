from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structure for symptoms and follow-up questions
symptoms_data = {
    'headache': {
        'questions': [
            {
                'question': 'Is the headache severe?',
                'answers': {
                    'yes': {
                        'follow_up': 'Do you have any visual disturbances (e.g., blurriness, flashing lights)?',
                        'follow_up_answers': {
                            'yes': 'You might have a migraine. Consider seeing a doctor.',
                            'no': 'Try resting and drinking water.'
                        }
                    },
                    'no': {
                        'follow_up': 'Have you experienced nausea or vomiting?',
                        'follow_up_answers': {
                            'yes': 'Consider consulting a healthcare professional.',
                            'no': 'Try to stay hydrated and rest.'
                        }
                    }
                }
            }
        ]
    },
    'fever': {
        'questions': [
            {
                'question': 'Do you have chills?',
                'answers': {
                    'yes': {
                        'follow_up': 'Have you experienced any body aches?',
                        'follow_up_answers': {
                            'yes': 'You might have the flu. Consider seeing a doctor.',
                            'no': 'Monitor your temperature and rest.'
                        }
                    },
                    'no': {
                        'follow_up': 'Have you had any recent travel or exposure to sick individuals?',
                        'follow_up_answers': {
                            'yes': 'Consider consulting a healthcare professional.',
                            'no': 'Keep monitoring your symptoms.'
                        }
                    }
                }
            }
        ]
    },
    'cough': {
        'questions': [
            {
                'question': 'Is it a dry cough?',
                'answers': {
                    'yes': {
                        'follow_up': 'Do you have a sore throat?',
                        'follow_up_answers': {
                            'yes': 'Stay hydrated and consider throat lozenges.',
                            'no': 'Monitor your symptoms and rest.'
                        }
                    },
                    'no': {
                        'follow_up': 'Are you experiencing shortness of breath?',
                        'follow_up_answers': {
                            'yes': 'Seek medical attention immediately.',
                            'no': 'Stay hydrated and monitor your symptoms.'
                        }
                    }
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
        follow_up_question = questions[0]['answers'][answer]['follow_up']
        follow_up_answers = questions[0]['answers'][answer]['follow_up_answers']
        return render_template('follow_up.html', question=follow_up_question, answers=follow_up_answers)

    return render_template('questions.html', symptom=symptom, question=questions[0]['question'], answers=questions[0]['answers'].keys())

if __name__ == '__main__':
    app.run(debug=True) 