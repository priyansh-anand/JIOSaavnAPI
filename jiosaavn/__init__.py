from jiosaavn import __jiosaavn__
from traceback import print_exc as __print_exc__

def song(query: str, lyrics: bool = False) -> list or dict:
    if "saavn" in query and "/song" in query:
        song_id = __jiosaavn__.get_song_id(query)
        song = __jiosaavn__.get_song(song_id,lyrics)
        return song
    else:
        return __jiosaavn__.search_for_song(query,lyrics)

def playlist(query: str, lyrics: bool = False) -> dict:
    id = __jiosaavn__.get_playlist_id(query)
    songs = __jiosaavn__.get_playlist(id,lyrics)
    return songs

def album(query: str, lyrics: bool = False) -> dict:
    id = __jiosaavn__.get_album_id(query)
    songs = __jiosaavn__.get_album(id,lyrics)
    return songs

def lyrics(query: str) -> dict:
    try:
        if 'http' in query and 'saavn' in query:
            id = __jiosaavn__.get_song_id(query)
            lyrics = __jiosaavn__.get_lyrics(id)
        else:
            lyrics = __jiosaavn__.get_lyrics(query)
        response = {}
        response['status'] = True
        response['lyrics'] = lyrics
        return response
    except Exception as e:
        error = {
            "status": False,
            "error": str(e)
        }
        return error

def search(query: str, lyrics: bool = False) -> list or dict:
    if 'saavn' not in query:
        return __jiosaavn__.search_for_song(query,lyrics)
    try:
        if '/song/' in query:
            song_id = __jiosaavn__.get_song_id(query)
            song = __jiosaavn__.get_song(song_id,lyrics)
            return song

        elif '/album/' in query:
            id = __jiosaavn__.get_album_id(query)
            songs = __jiosaavn__.get_album(id,lyrics)
            return songs

        elif '/playlist/' or '/featured/' in query:
            id = __jiosaavn__.get_playlist_id(query)
            songs = __jiosaavn__.get_playlist(id,lyrics)
            return songs

    except Exception as e:
        __print_exc__()
        error = {
            "status": True,
            "error":str(e)
        }
        return error
    return None

if __name__ == '__main__':
    print("[*] You have to import this file into your python script")
