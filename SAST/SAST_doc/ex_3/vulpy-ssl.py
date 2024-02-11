#!/usr/bin/env python3

from flask import Flask, g, redirect, request
from decouple import config  # Importez la fonction config
import libsession
from mod_hello import mod_hello
from mod_user import mod_user
from mod_posts import mod_posts
from mod_mfa import mod_mfa

app = Flask('vulpy')

# Utilisez la fonction config pour récupérer la clé secrète depuis une variable d'environnement
app.config['SECRET_KEY'] = config('SECRET_KEY', default='default_secret_key')

app.register_blueprint(mod_hello, url_prefix='/hello')
app.register_blueprint(mod_user, url_prefix='/user')
app.register_blueprint(mod_posts, url_prefix='/posts')
app.register_blueprint(mod_mfa, url_prefix='/mfa')

@app.route('/')
def do_home():
    return redirect('/posts')

@app.before_request
def before_request():
    g.session = libsession.load(request)

# Modifiez le passage du contexte SSL pour utiliser des variables d'environnement
ssl_cert_path = config('SSL_CERT_PATH', default='/tmp/acme.cert')
ssl_key_path = config('SSL_KEY_PATH', default='/tmp/acme.key')
app.run(debug=True, host='127.0.1.1', ssl_context=(ssl_cert_path, ssl_key_path))