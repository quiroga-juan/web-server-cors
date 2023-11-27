# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import redis
from config import Config
from flask import Flask, session, redirect, escape, request, make_response, jsonify
from flask_cors import CORS
import codecs


# Configure the application name with the FLASK_APP environment variable.
app = Flask(__name__)

cors = CORS(app, supports_credentials=True)

# Configure the secret_key with the SECRET_KEY environment variable.
app.secret_key = os.environ.get('SECRET_KEY', default=None)

# Configure the REDIS_URL constant with the REDIS_URL environment variable.
REDIS_URL = os.environ.get('REDIS_URL')


class SessionStore:
    """Store session data in Redis."""

    def __init__(self, token, url='redis://localhost:6379', ttl=120):
        self.token = token
        self.redis = redis.Redis.from_url(url)
        self.ttl = ttl

    def set(self, key, value):
        self.refresh()
        return self.redis.hset(self.token, key, value, exp=self.ttl)

    def get(self, key, value):
        self.refresh()
        return self.redis.hget(self.token, key)

    def incr(self, key):
        self.refresh()
        return self.redis.hincrby(self.token, key, 1)

    def refresh(self):
        self.redis.expire(self.token, self.ttl)


@app.route('/sensitive-victim-data')
def index():
    if 'username' in session:
        username = escape(session['username'])

        store = SessionStore(username, REDIS_URL)

        visits = store.incr('visits')
        response = {
            'user': username,
            'visits': visits
        }
        response = make_response(jsonify(response))
        if 'Origin' in request.headers:
            header_request = request.headers['Origin']
            response.headers.add("Access-Control-Allow-Origin", header_request)
            response.headers.add('Access-Control-Allow-Headers', "*")
            response.headers.add('Access-Control-Allow-Methods', "*")
            response.headers.add('Access-Control-Allow-Credentials', "true")
        return response

    return 'You are not logged in'

@app.route('/sensitive-victim-data-with-cors')
def index_with_cors():
    username = 'pepe'
    response = '''
        Logged in as {0}.<br>
        Visits: {1}
    '''.format(username, 1)
    response = make_response(response)
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:8000")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    return response

@app.route('/subdomain', methods=['GET'])
def execute():
    f=codecs.open("test_subdomain.html", 'r')
    return f.read()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        if session['password'] != Config.password:
            raise Exception('Invalid login')
        return redirect('/sensitive-victim-data')
    return '''
        <form method="post">
        <label>Enter your username: </label>
        <p><input type=text name=username>
        <label>Enter your password: </label>
        <p><input type=text name=password>
        <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)