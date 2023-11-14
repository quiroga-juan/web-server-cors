# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from flask import Flask
import codecs

# Configure the application name with the FLASK_APP environment variable.
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def execute():
    f=codecs.open("test.html", 'r')
    return f.read()

@app.route('/with-cors', methods=['GET', 'POST'])
def execute_():
    f=codecs.open("test_with_cors.html", 'r')
    return f.read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)