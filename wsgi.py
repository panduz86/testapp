from flask import Flask
from flask import request
application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


@application.route('/hello', methods=['GET', 'POST'])
def better_hello():
    nome = request.args.get('nome')
    return "Hello " + nome + "!"


if __name__ == "__main__":
    application.run()