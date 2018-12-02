import spotipy

spotify = spotipy.spotify()
results = spotify.search(q='artist:' + name, type='artist')
print(results)
