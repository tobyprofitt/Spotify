import spotipy
import logging
import json
import pandas

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

gizz_uri = 'spotify:artist:6XYvaoDGE0VmRt83Jss9Sn'
lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
honey_uri = 'spotify:track:01IuTsgAlgKlgrvPhZ2c95'

bad = 'spotify:artist:7hqZBHSgDs1odG9aupMzEI'
js = 'spotify:artist:2A09V0kHlETOFfT8Hz8oba'

print(sp.recommendation_genre_seeds())
results = sp.recommendations(seed_artists=[bad, js, gizz_uri])
for track in results['tracks']:
    if 'AU' in track['available_markets']:
        print(track)

playlists = sp.featured_playlists(country='AU', locale='ang')
print(playlists)

"""
with open('data.json', 'w') as outfile:
    json.dump(playlists, outfile)
"""

'''
results = sp.artist_top_tracks(gizz_uri, country='NZ')
for track in results['tracks']:
    if not track['preview_url']:
        continue
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
'''
logger = logging.getLogger('examples.artist_recommendations')
logging.basicConfig(level='INFO')
