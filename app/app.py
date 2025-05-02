from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    xff = request.headers.get("X-Forwarded-For", "Not found")
    return f"X-Forwarded-For: {xff}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)