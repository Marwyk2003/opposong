import yaml
from flask import Flask, render_template, request, redirect
from spotify import Client
from shazam import ShazamWrapper

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

spotify_credentials = cfg['spotify_credentials']
spotify_client = Client('user-read-currently-playing',
                        spotify_credentials['client_id'],
                        spotify_credentials['client_secret'],
                        spotify_credentials['redirect_uri'])


@app.route("/", methods=['POST', 'GET'])
def index():
    track=''
    artist=''
    if request.method == 'POST':
        print("~")
        f = request.files['file']
        s = ShazamWrapper(f)
        shazamData = s.getData()
        track = shazamData['track']
        artist = shazamData['artist']
        trackid = spotify_client.getMeatdata(track, artist)
        trackStats = spotify_client.getTrackData(trackid)
        print(track, artist)
        return render_template('index.html', track=track, artist=artist)
    else:
        # return flask.send_file('/maps/map.html')

        return render_template('index.html', track=track, artist=artist)
