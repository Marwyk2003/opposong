import yaml
from flask import Flask, render_template, request
from spotify import Client
from shazam import ShazamWrapper

app = Flask(__name__)

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

spotify_credentials = cfg['spotify_credentials']
spotify_client = Client('user-read-currently-playing',
                        spotify_credentials['client_id'],
                        spotify_credentials['client_secret'],
                        spotify_credentials['redirect_uri'])


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        s = ShazamWrapper(f)
        trackid = spotify_client.getMeatdata(*s.getData())
        trackStats = spotify_client.getTrackData(trackid)
        print(trackStats)
        return 'file uploaded successfully'
    else:
        return render_template('index.html', content={})
