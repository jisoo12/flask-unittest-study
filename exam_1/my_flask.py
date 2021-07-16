from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
  return "Hello!"

@app.route("/world")
def world():
  return "World!"


if __name__ == '__main__':
  app.run(debug=True)