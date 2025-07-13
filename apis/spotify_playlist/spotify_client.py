import urllib.parse
import pprint
import spotipy
from spotipy import SpotifyOAuth
from data.env_vars import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI


class SpotifyClient:

    def __init__(self):
        spotify_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                       redirect_uri=SPOTIFY_REDIRECT_URI,
                                       scope='playlist-modify-private')
        self.client = spotipy.Spotify(auth_manager=spotify_manager)

    def get_playlists(self):
        playlists = self.client.current_user_playlists()
        print(playlists)

    def get_user_id(self) -> str:
        data = self.client.current_user()
        return data['id']

    def create_uri_list(self, songs: list, bands: list) -> list:
        """Builds a list of Spotify URI from the list of songs and bands"""
        song_uris = []
        for _ in range(0, len(songs)):
            # print(f"Searching for {songs[_]} by {bands[_]}...")
            song_result = self.search_song(song=songs[_], artist=bands[_])
            song_uri = self.get_song_uri(song_result, songs[_], artist=bands[_])
            if song_uri:
                song_uris.append(song_uri)
        print(f"Found {len(song_uris)} songs")
        return song_uris

    def search_song(self, song: str, artist: str) -> list:
        """Execute the track search in the US market. Limited to 3 results"""
        query = f"q=track:{song} artist:{artist}"
        query = urllib.parse.quote_plus(query)

        song_result = self.client.search(q=query, limit=3, offset=0, market="US", type="track")
        # print(song_result)
        return song_result

    def get_song_uri(self, song_details: list, song: str, artist: str) -> str | None:
        """Given a search result, finds the song interpreted by the Artist and returns the URI (None if not found)"""
        items = song_details['tracks']['items']
        for item in items:
            # startswith() considers remastered versions
            if item['name'].startswith(song):
                list_of_artists = [artist_name['name'] for artist_name in item['artists']]
                if len(list_of_artists) > 1:
                    if artist in list_of_artists:
                        return item['uri']
                    else:
                        print(f"{song} by {artist} --> {item['name']} by {list_of_artists}")
                        with open(f"./search_debug/{song}.json", "w") as file:
                            file.write(pprint.pformat(song_details, compact=True).replace("'", '"'))
                else:
                    if artist in list_of_artists[0] or list_of_artists[0] in artist:
                        return item['uri']
                    else:
                        print(f"{song} by {artist} --> {item['name']} by {list_of_artists}")
                        with open(f"./search_debug/{song}.json", "w") as file:
                            file.write(pprint.pformat(song_details, compact=True).replace("'", '"'))
