from flask import Flask

server = Flask(__name__)


@server.route("/")
def hello():
    return "Hello Digicactus! V0.0.2"


@server.route("/api/dieu")
def redempteur():
    return "Dieu est mon rédempteur!"


@server.route("/api/jesus")
def sauveur():
    return "Jesus est mon sauveur!"


@server.route("/api/lola")
def lola():
    return "Lola c'est ma vie!"


@server.route("/api/birth")
def anniversaire():
    return "<h1> LOLA est née le 19/11/2022. </h1>\n <h2>Dans un mois, c'est son anniversaire."


if __name__ == "__main__":
    server.run(host='0.0.0.0')
