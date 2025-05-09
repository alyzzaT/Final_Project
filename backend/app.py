from flask import Flask
app = Flask(__name__)

@app.route("/api/message")
def message():
    return {"message": "VR Backend is running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
