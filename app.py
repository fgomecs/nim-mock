from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/v1/mock", methods=["POST"])
def mock():
    prompt = request.json.get("prompt", "")
    return jsonify({"response": f"Mock NIM received: {prompt}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
