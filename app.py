from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "quiz_secret_key"

# Quiz Questions
questions = [
    {
        "question": "What is the output of print(2**3)?",
        "options": ["5", "6", "8", "9"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used for function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is mutable?",
        "options": ["tuple", "list", "string", "int"],
        "answer": "list"
    },
    {
        "question": "Which library is used for data analysis?",
        "options": ["numpy", "pandas", "matplotlib", "flask"],
        "answer": "pandas"
    },
    {
        "question": "What does SQL stand for?",
        "options": [
            "Structured Query Language",
            "Simple Query Language",
            "Standard Question Language",
            "None"
        ],
        "answer": "Structured Query Language"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz", methods=["POST"])
def quiz():
    session["score"] = 0
    session["q_index"] = 0
    return redirect("/question")

@app.route("/question", methods=["GET", "POST"])
def question():
    q_index = session.get("q_index", 0)

    if request.method == "POST":
        selected = request.form.get("option")
        correct = questions[q_index]["answer"]

        if selected == correct:
            session["score"] += 1

        session["q_index"] += 1
        q_index = session["q_index"]

    if q_index >= len(questions):
        return redirect("/result")

    return render_template("quiz.html",
                           question=questions[q_index],
                           q_num=q_index + 1,
                           total=len(questions))

@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(questions)
    percentage = (score / total) * 100

    return render_template("result.html",
                           score=score,
                           total=total,
                           percentage=round(percentage, 2))

if __name__ == "__main__":
    app.run(debug=True)