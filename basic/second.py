from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello Welcome to the Homepage"

@app.route("/demo")
def webapage():
    return "These is the page where you get more information about Jinja2 Template"

if __name__ == "__main__":
    app.run(debug = True)


