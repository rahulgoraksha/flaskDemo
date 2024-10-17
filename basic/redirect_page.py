from flask import Flask, redirect

app = Flask(__name__)

@app.route("/old-page")
def old_page():
    # Redirect the user to the new page
    return redirect("/new-page")

@app.route("/new-page")
def new_page():
    return "Welcome to the new page!"

if __name__ == "__main__":
    app.run(debug = True)
