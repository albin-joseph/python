from flask import Flask, render_template

#To run this we have to export this app . Please find for this app  export FLASK_APP=server.py and flask run   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
    