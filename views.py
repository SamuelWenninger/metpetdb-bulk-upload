from flask import Flask, render_template, request, jsonify
import commands, json

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def test():
    #Capture bulk upload details inputted by user (url, filetype) formatted as
    #JSON that was sent from JavaScript
    UserInput = request.json
    print "Type received: ", type(UserInput)
    if (UserInput != None):
        print "Checked Value: ", UserInput['checked']
        #Call the parse program and get the response
        status, response = commands.getstatusoutput("python \
                ./ParseTest/bulk-upload.py " + str(UserInput['url']) \
                + " " + str(UserInput['checked']))
        print "Response: ", response
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
