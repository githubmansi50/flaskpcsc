from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/suciencrypt")
def suciencrypt():
    return render_template('suciencrypt.html')

@app.route("/sucidecrypt")
def sucidecrypt():
    return render_template('sucidecrypt.html')


if __name__ == '__main__':
    app.run(debug=True)
