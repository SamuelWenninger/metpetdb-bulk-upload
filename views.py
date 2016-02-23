from flask import Flask, render_template, request, jsonify
import os, json

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    UserInput = request.json
    print type(UserInput)
    print UserInput
    #Call the parse program
    #os.system("command line thing goes here")
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)
