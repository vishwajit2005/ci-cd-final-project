from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    app.logger.info("SERVICERUNNING")
    return "Service is running successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
