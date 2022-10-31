from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title="ITHub")

@app.route("/education")
def education():
    return render_template('education.html', title="Обучение")

@app.route('/callboard')
def callboard():
    return render_template('callboard.html', title="Доска объявлений")

if __name__=="__main__":
    app.run(debug=True)