import os
from utils import tools

from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    with open(os.path.join(DATA_DIR, data["file_name"]), "r", encoding="utf-8") as file:
        info_logs = file.readlines()
    result1 = tools(file=info_logs, cmd=data["cmd1"], value=data["value1"])
    result2 = tools(file=result1, cmd=data["cmd2"], value=data["value2"])
    return jsonify(result2)


if __name__ == "__main__":
    app.run()
