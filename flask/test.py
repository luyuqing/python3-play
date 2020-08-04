from flask import Flask, request, current_app


app = Flask(__name__)
with app.test_request_context('http://127.0.0.1:10001/login/auth?client_id=boost&redirect_uri=http:127.0.0.1', data={'name': 'lal'}):
    print(request.scheme)  # http
    print(request.host)  # 127.0.0.1:10001
    print(request.path)  # /login/auth
    print(request.args)  # ImmutableMultiDict([('client_id', 'boost'), ('redirect_uri', 'http:127.0.0.1')])
    print(request.form)  # ImmutableMultiDict([('name', 'lal')])
    print(request.method)  # GET
