from flask import Flask, jsonify, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Response(
        "Hello, World! \nThis is Huy's webapi",
        mimetype='text/plain'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
