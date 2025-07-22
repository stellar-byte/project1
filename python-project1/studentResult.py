from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def student_score():
    return render_template('studentScore.html')

@app.route('/result', methods=["POST"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template('resultPage.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)