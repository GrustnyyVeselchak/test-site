from flask import Flask, render_template, url_for, request, flash, session, redirect

app = Flask(__name__)
app.secret_key = 'jdslajfsl;afjslkfdjsal;fja'
app.config['SECTRET_KEY'] = 'sdajflksahgsdjfaf;isoajalk'

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

@app.route('/login', methods=["POST", "GET"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != "admin" or request.form['pass'] !="admin":
            error = "try again"
        else:
            return redirect(url_for('index'))
    return render_template('login.html', title='Авторизация', error=error)


if __name__=="__main__":
    app.run(debug=True)