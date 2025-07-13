from scrapper import BillboardScrapper
from spotify_client import SpotifyClient


# get the Top 100
bs = BillboardScrapper()
song_titles = bs.get_song_titles()
band_names = bs.get_band_names()

# connect to Spotify and creates the playlist
sp = SpotifyClient()
song_uris = sp.create_uri_list(songs=song_titles, bands=band_names)
user_id = sp.get_user_id()

# create the playlist and populate it
new_playlist = sp.client.user_playlist_create(user=user_id, name=f"{bs.date} Billboard Top 100", public=False,
                                              collaborative=False, description=f"Billboard Top 100 on {bs.date}")
add_songs = sp.client.playlist_add_items(playlist_id=new_playlist['id'], items=song_uris)

if add_songs['snapshot_id']:
    print('Playlist created!')
