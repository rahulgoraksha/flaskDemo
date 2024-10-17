from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/guest/<gid>")
def guest(gid):
    return "Welcome to the Department of Computer Science Library. You have logged in as Guest with id: %s" %gid

@app.route("/student/<sid>")
def student(sid):
    return "Welcome to the Department of Computer Science Library. You have logged in as Student with id: %s" %sid

@app.route("/faculty/<fid>")
def faculty(fid):
    return "Welcome to the Department of Computer Science Library. You have logged in as faculty with id: %s" %fid

@app.route("/Library/<login>/<id>")
def library(login, id):
    if login == "guest":
        return redirect(url_for("guest",gid = id))
    elif login == "student":
        return redirect(url_for("student",sid = id))
    elif login == "faculty":
        return redirect(url_for("faculty",fid = id))
    else:
        return "invalid input"
    
if __name__ == "__main__":
    app.run(debug = True)