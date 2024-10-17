from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/profile/<username>")
def profile(username):
    return f"Hello, {username}!"

@app.route("/login")
def login():
    # Simulating a user login and redirecting to their profile page
    username = "Rahul"
    return redirect(url_for("profile", username=username))

if __name__ == "__main__":
    app.run(debug = True)