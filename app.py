from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"Hello DevOps! Host: {socket.gethostname()}"

@app.route('/health')
def health():
    return {"status": "running"}

app.run(host='0.0.0.0', port=5000)
