import yaml
from flask import Flask, render_template, request, redirect
from spotify import Client
from shazam import ShazamWrapper
import webbrowser

PRESENTATION = True

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
    track='<TRACK>'
    artist='<ARTIST>'
    track2='<TRACK>'
    artist2='<ARTIST>'
    image1 = 'https://bulma.io/images/placeholders/128x128.png'
    image2 = 'https://bulma.io/images/placeholders/128x128.png'
    if request.method == 'POST':
        print("~")
        f = request.files['file']
        s = ShazamWrapper(f)
        shazamData = s.getData()
        track = shazamData['track']
        artist = shazamData['artist']
        trackid = spotify_client.getMeatdata(track, artist)
        trackStats = spotify_client.getTrackData(trackid)
        params = [trackStats[0]['danceability'], trackStats[0]['energy'],
                  trackStats[0]['acousticness'], trackStats[0]['valence']]
        opposites = spotify_client.getOpposite(params)
        songs = spotify_client.songRequest(opposites)
        url = songs[0]['external_urls']['spotify']
        # Open URL in new window, raising the window if possible.
        if PRESENTATION:
            url = 'https://open.spotify.com/track/4BjSoI8v5uBB1FblH1KYIr?si=2f660798414c4487'
            image1 = 'https://i.scdn.co/image/ab67616d00001e025755e164993798e0c9ef7d7a'
            image2 = 'https://i.scdn.co/image/ab67616d00001e02edaef00259da04154d9d26cf'
            track2='Barka'
            artist2='Jan Paweł II'
        else:
            image1 = 'https://bulma.io/images/placeholders/128x128.png'
            image2 = 'https://bulma.io/images/placeholders/128x128.png'
        webbrowser.open_new(url)
        return render_template('index.html', track=track, artist=artist, track2=track2, artist2=artist2, image1=image1, image2=image2)
    else:
        # return flask.send_file('/maps/map.html')

        return render_template('index.html', track=track, artist=artist, track2=track2, artist2=artist2, image1=image1, image2=image2)
