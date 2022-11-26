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
        return results['tracks']['items'][0]["id"]

    def getTrackData(self, trackid):
        response = self.sp.audio_features([trackid])
        return response

    def getOpposite(self, params):
        opposites = [(round((feature+0.5) % 1+0.2, 3) if round((feature+0.5) %
                      1, 3) < 0.2 else round((feature+0.5) % 1, 3)) for feature in params]
        return opposites

    def songRequest(self, opposite):
        results= self.sp.recommendations(seed_genres= ['pop','rock','soul','metal','shanty'],limit=5,target_danceability=opposite[0],target_valence=opposite[3], target_energy=0.85, target_acousticness=opposite[2])
        return results['tracks']