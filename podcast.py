import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
load_dotenv()

# Rest of the code
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("user"),
                                               client_secret=os.getenv("pword"),
                                               redirect_uri=os.getenv("redirect"),
                                               scope='user-read-playback-state'))

