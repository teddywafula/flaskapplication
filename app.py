from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "test"

@app.route("/testmethods", methods = ["POST","GET"])
def api_post_get_test_methods():
    if request.method == "POST":
        return "post request"
    if request.method == "GET":
        return "get request"
if __name__ == "__main__":
    app.run()
