from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("books.html")

@app.route("/book_cat" ,methods = ["POST","GET"])
def cat():
    if request.method == "POST":
        return render_template("book_cat.html")
    
   
@app.route("/book_back")
def back():
    return render_template("book_cat.html")

@app.route("/book_thriller")
def thriller():
    return render_template("book_thriller.html")


@app.route("/book_fiction")
def fiction():
    return render_template("book_fiction.html")


@app.route("/book_adult")
def adult():
    return render_template("book_adult.html")



if __name__ == "__main__":
    app.run(debug = True)