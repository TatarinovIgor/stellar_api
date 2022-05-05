import flask
from stellar_sdk import Keypair

app = flask.Flask(__name__)
app.config["DEBUG"] = True

keys = {"public": "",
        "secret": ""}


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/create_stellar_keypair', methods=['GET'])
def keypair():
    pair = Keypair.random()
    print(f"Secret: {pair.secret}")
    print(f"Public Key: {pair.public_key}")
    keys.update({"public": pair.public_key})
    keys.update({"secret": pair.secret})
    return keys

app.run()
