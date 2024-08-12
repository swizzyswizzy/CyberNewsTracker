import mysql.connector
import requests
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/test', methods=['GET'])
def testMethod():
    return 'test'


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=2137)
