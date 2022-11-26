import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials


class Client():
    def __init__(self, scope, id, secret, uri):
        self.scope = scope
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=id, client_secret=secret))
        # self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        #     scope=self.scope, client_id=id, client_secret=secret, redirect_uri=uri))

    def getMeatdata(self, track, artist):
        results = self.sp.search(
            q=f'artist:{artist} track:{track}', type='track', limit=1)
        # print(results)
        return results['tracks']['items'][0]["id"]

    def getTrackData(self, trackid):
        response = self.sp.audio_features([trackid])
        return response
