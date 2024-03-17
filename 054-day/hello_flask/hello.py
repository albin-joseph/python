from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def hello_bye():
    return "<p>Bye</p>"

@app.route("/username/<name>/<int:age>")
def greetings(name, age):
    return f"<p>Hello there {name}, you are {age} years older.</p>"

if __name__ == "__main__":
    app.run(debug=True)