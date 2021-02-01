from flask import Flask


server = Flask(__name__)

@server.route("/")
def hello():
 return "Hello World!"

@server.route("/test_1")
def test_1():
 return 'test_1'

if __name__ == "__main__":
 server.run(host='0.0.0.0')