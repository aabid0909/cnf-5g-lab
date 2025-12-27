from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pdu-session", methods=["POST"])
def create_pdu_session():
    data = request.get_json(force=True)

    response = {
        "supi": data.get("supi", "imsi-00101"),
        "dnn": data.get("dnn", "internet"),
        "status": "ACTIVE"
    }

    return jsonify(response), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)

