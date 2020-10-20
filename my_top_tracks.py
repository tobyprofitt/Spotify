# Shows the top tracks for a user

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                               redirect_uri='http://localhost:7777/callback'))

ranges = ['long_term']
tracks = []

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=51, offset=50)
    for i, item in enumerate(results['items']):
        tracks.append(item['uri'])
        print((i+50), item['name'], '//', item['artists'][0]['name'])
    print()

playlists = sp.current_user_playlists()

playlist_id = sp.current_user_playlists()['items'][0]['id']
