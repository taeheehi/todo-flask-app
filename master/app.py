from flask import Flask, jsonify

app = Flask(__name__)

# /todo 라우터 정의
@app.route("/todo")
def todo():
    return jsonify({
        "message": "This is your TODO list.",
        "items": [
            {"id": 1, "task": "Finish Kubernetes ingress setup"},
            {"id": 2, "task": "Review Flask routing"},
            {"id": 3, "task": "Take a break, you earned it 🧃"}
        ]
    })

# 서버 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
