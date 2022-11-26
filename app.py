import yaml
from flask import Flask, render_template
from spotify import Client

app = Flask(__name__)

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

spotify_credentials = cfg['spotify_credentials']
spotify_client = Client('user-read-currently-playing',
                        spotify_credentials['client_id'],
                        spotify_credentials['client_secret'],
                        spotify_credentials['redirect_uri'])


@app.route("/")
def index():
    return render_template('index.html', content={})