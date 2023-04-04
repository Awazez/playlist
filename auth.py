import spotipy
from spotipy.oauth2 import SpotifyOAuth

def auth():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="http://www.google.com",
                                               scope="playlist-modify user-read-private"))
    return sp
