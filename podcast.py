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

urls = ["https://open.spotify.com/episode/64n5ZUa1BekxB8WCM958cy?si=de1a48edc4ec4e78", "https://open.spotify.com/episode/2cfCLhhGZBGM4hclq3QIym?si=70ca43da1fd8443b"]

def urlID(url):
    parts = url.split('/')
    episode_id_index = parts.index('episode') + 1
    episode_id_with_query = parts[episode_id_index]
    return episode_id_with_query.split('?')[0]

def urlIDS(urls):
    ids = []
    for url in urls:
        episode_id = urlID(url)
        if episode_id:
            ids.append(episode_id)
    return ids
      

episode_ids = urlIDS(urls)

def sumEpisodeDuration(episode_ids):
    total_duration = 0
    for episode_id in episode_ids:
        episode_details = sp.episode(episode_id)
        episode_duration_ms = episode_details['duration_ms']
        total_duration += episode_duration_ms    
    return total_duration

episode_duration_ms = sumEpisodeDuration(episode_ids)

minutes, seconds = divmod(episode_duration_ms // 1000, 60)
print(f"Total duration of episodes is {minutes} minutes and {seconds} seconds")

#retrieve episode
#get spotify episode id 1 to 50 max
# find time
# add time
# present time


   