from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "nf": "AMF",
        "status": "UP",
        "version": "5G-CNF-MOCK"
    }), 200

@app.route("/ue/<supi>", methods=["GET"])
def ue_status(supi):
    return jsonify({
        "supi": supi,
        "state": "REGISTERED"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

