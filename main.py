import os
from typing import Any, Optional, Union, Iterator, Generator

from utils import commands

from flask import Flask, request, jsonify, abort, Response

app: Flask = Flask(__name__)

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: str = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Response:
    data: Optional[Any] = request.json
    if not data:
        return jsonify('No data')
    cmd1: Optional[str] = data.get('cmd1')
    cmd2: Optional[str] = data.get('cmd2')
    value1: Optional[str] = data.get('value1')
    value2: Optional[str] = data.get('value2')
    filename: Optional[str] = data.get('filename')

    if not filename or not cmd1 or not value1:
        abort(400, 'Not enough arguments')
    filepath: str = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        abort(400, 'There is no such file')

    with open(filename, "r", encoding="utf-8") as file:
        result: Union[str, Iterator, Generator] = commands(it=file, cmd=data["cmd1"], value=data["value1"])
        if cmd2 and value2:
            result2: Union[str, Iterator, Generator] = commands(it=result, cmd=data["cmd2"], value=data["value2"])
            return jsonify(result2)
    return jsonify(result)


if __name__ == "__main__":
    app.run()
