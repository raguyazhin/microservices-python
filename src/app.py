from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return str(hostname), str(hostip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, hostip = fetchDetails()
    return render_template('index.html' , HOSTNAME=hostname, HOSTIP=hostip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)