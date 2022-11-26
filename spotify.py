import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Client():
    def __init__(self, scope, id, secret, uri):
        self.scope = scope
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=self.scope, client_id=id, client_secret=secret, redirect_uri=uri))
