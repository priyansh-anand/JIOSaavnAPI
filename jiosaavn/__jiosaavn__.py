import requests
from jiosaavn import __endpoints__
from jiosaavn import __helper__
import json
from traceback import print_exc as __print_exc__

def search_for_song(query: str,lyrics: bool) -> list:
    search_base_url = __endpoints__.search_base_url+query
    response = requests.get(search_base_url).text.encode().decode('unicode-escape')
    response = json.loads(response)
    song_response = response['songs']['data']
    songs = []
    for song in song_response:
        id = song['id']
        song_details_base_url = __endpoints__.song_details_base_url+id
        song_response = requests.get(song_details_base_url).text.encode().decode('unicode-escape')
        song_response = json.loads(song_response)
        song_data = __helper__.format_song(song_response[id],lyrics)
        songs.append(song_data)
    return songs

def get_song(id: str,lyrics: bool) -> dict:
    song_details_base_url = __endpoints__.song_details_base_url+id
    song_response = requests.get(song_details_base_url).text.encode().decode('unicode-escape')
    song_response = json.loads(song_response)
    song_data = __helper__.format_song(song_response[id],lyrics)
    return song_data

def get_song_id(url: str) -> str:
    res = requests.get(url, data=[('bitrate', '320')])
    try:
        return res.text.split('"song":{"type":"')[1].split('","image":')[0].split('"id":"')[-1]
    except IndexError:
        return(res.text.split('"pid":"'))[1].split('","')[0]

def get_album(album_id: str,lyrics: bool) -> dict:
    songs_json = []
    try:
        response = requests.get(__endpoints__.album_details_base_url+album_id)
        if response.status_code == 200:
            songs_json = response.text.encode().decode('unicode-escape')
            songs_json = json.loads(songs_json)
            return __helper__.format_album(songs_json,lyrics)
    except Exception as e:
        print(e)
        return None

def get_album_id(input_url: str) -> str:
    res = requests.get(input_url)
    try:
        return res.text.split('"album_id":"')[1].split('"')[0]
    except IndexError:
        return res.text.split('"page_id","')[1].split('","')[0]

def get_playlist(listId: str,lyrics: bool) -> dict:
    try:
        response = requests.get(__endpoints__.playlist_details_base_url+listId)
        if response.status_code == 200:
            songs_json = response.text.encode().decode('unicode-escape')
            songs_json = json.loads(songs_json)
            return __helper__.format_playlist(songs_json,lyrics)
        return None
    except Exception:
        __print_exc__()
        return None

def get_playlist_id(input_url: str) -> str:
    res = requests.get(input_url).text
    try:
        return res.split('"type":"playlist","id":"')[1].split('"')[0]
    except IndexError:
        return res.split('"page_id","')[1].split('","')[0]


def get_lyrics(id: str) -> str:
    url = __endpoints__.lyrics_base_url+id
    lyrics_json = requests.get(url).text.encode().decode('unicode-escape')
    lyrics_text = json.loads(lyrics_json)
    return lyrics_text['lyrics']
