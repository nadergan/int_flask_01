from flask import Flask

app = Flask(__name__)

# This is a comment 

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello From Flask!"

app.run()




