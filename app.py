from flask import Flask, request, jsonify
from paraphrase import paraphrase
from predict import get_answers
import os

app = Flask(__name__)

# Paths to the files
QUESTIONS_FILE = "term_sheet_questions.txt"
DATA_FILE = os.path.join("data", "termsheet.txt")

# Load questions from term_sheet_questions.txt
def load_questions():
    with open(QUESTIONS_FILE, "r") as f:
        questions = [line.strip() for line in f.readlines() if line.strip()]
    return questions

# Load content from termsheet.txt
def load_termsheet():
    with open(DATA_FILE, "r") as f:
        content = f.read()
    return content

@app.route("/predict", methods=["POST"])
def predict():
    # Load the questions dynamically
    questions = load_questions()
    
    # Load the content of termsheet.txt
    context = load_termsheet()

    # Get answers using the loaded questions and context
    answers = get_answers(questions, context)
    
    # Create response
    response = [{"question": q, "answer": answers[q]} for q in questions]
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
