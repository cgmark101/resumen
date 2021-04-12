from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ok/')
def ok():
    return render_template("ok.html")

if __name__ == '__main__':
    app.run()
