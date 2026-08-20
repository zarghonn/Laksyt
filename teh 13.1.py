from flask import Flask, jsonify

app = Flask(__name__)


def on_alkuluku(luku):
    if luku < 2:
        return False
    jakaja = 2
    while jakaja * jakaja <= luku:
        if luku % jakaja == 0:
            return False
        jakaja += 1
    return True


@app.route("/alkuluku/<int(signed=True):luku>")
def alkuluku(luku):
    return jsonify({"Number": luku, "isPrime": on_alkuluku(luku)})


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)


