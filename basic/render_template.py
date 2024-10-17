from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def print():
    return render_template("show.html")


@app.route("/cursession", methods = ["POST","GET"])
def cursession():
    if request.method == "POST":
        cs = request.form.get("cursession")
        return render_template("mysession.html", cs = cs)
    else:
        return "Not working"




if __name__ == "__main__":
    app.run(debug = True)