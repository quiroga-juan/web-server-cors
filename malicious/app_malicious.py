# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from flask import Flask, session, redirect, escape, request
from flask_cors import CORS, cross_origin

# Configure the application name with the FLASK_APP environment variable.
app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/', methods=['GET', 'POST'])
def execute():
    if request.method == 'POST':
        
        return 'hola'
    return '''
        <form method="post">
        <p><input type=submit value=Execute>
        </form>
    '''


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)