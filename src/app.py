from flask import Flask, jsonify, Response
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Response(
        "Hello, World! "
        "\nThis is Huy's webapi "
        "\nConfigMap: NAME: {0}, EMAIL: {1}"
        "\nSecret: USER: {2}, PASS: {3}".format(os.getenv("NAME"), os.getenv("EMAIL"), os.getenv("USER"), os.getenv("PASS")),
        mimetype='text/plain'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
