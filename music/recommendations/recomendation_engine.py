from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify credentials
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"

spotify = Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
)

EMOTION_TO_GENRE = {
    "Happy": "pop",
    "Sad": "acoustic",
    "Neutral": "classical",
    "Angry": "rock",
    "Surprised": "electronic",
}

def get_recommendations(emotion, language):
    genre = EMOTION_TO_GENRE.get(emotion, "pop")
    results = spotify.search(q=f"genre:{genre} language:{language}", type="track", limit=10)
    tracks = [{"name": track["name"], "artist": track["artists"][0]["name"]} for track in results["tracks"]["items"]]
    return tracks
