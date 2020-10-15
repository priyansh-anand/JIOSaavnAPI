
## JioSaavn Python Module [Unofficial]

### Show some :heart: and :star: the repo to support the project


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


 ---
###### **NOTE:** You don't need to have JioSaavn link of the song in order to fetch the song details, you can directly search songs by their name. Fetching Songs/Albums/Playlists from URL is also supported in this module.  

 ---

### **Features**:
##### Currently the module can get the following details for a specific song:
- **Song Name**
- **Singer Name**
- **Album Name**
- **Album URL**
- **Duration of Song**
- **Song Thumbnail URL (Max Resolution)**
- **Song Language**
- **Download Link**
- **Release Year**
- **Album Art Link (Max Resolution)**
- **Lyrics**
- .... and much more!

```json
{
    "album": "BIBA",
    "album_url": "https://www.jiosaavn.com/album/biba/98G3uzIs2qQ_",
    "autoplay": "false",
    "duration": "175",
    "e_songid": "ICERW0MFfQs",
    "has_rbt": "false",
    "image_url": "https://c.saavncdn.com/987/BIBA-English-2019-20190201201359-500x500.jpg",
    "label": "Joytime Collective",
    "label_url": "/label/joytime-collective-albums/",
    "language": "hindi",
    "liked": "false",
    "map": "Marshmello^~^/artist/marshmello-songs/Eevs5FiVgus_^~^Pritam Chakraborty^~^/artist/pritam-chakraborty-songs/OaFg9HPZgq8_^~^Shirley Setia^~^/artist/shirley-setia-songs/9qGdjoPJ1vM_^~^Pardeep Singh Sran^~^/artist/pardeep-singh-sran-songs/NIfiZRCrYQA_^~^Dev Negi^~^/artist/dev-negi-songs/NpCqdI4dD5U_",
    "music": "",
    "origin": "search",
    "origin_val": "biba",
    "page": 1,
    "pass_album_ctx": "true",
    "perma_url": "https://www.jiosaavn.com/song/biba/ICERW0MFfQs",
    "publish_to_fb": true,
    "singers": "Marshmello, Pritam Chakraborty, Shirley Setia, Pardeep Singh Sran, Dev Negi",
    "songid": "PIzj75J8",
    "starred": "false",
    "starring": "",
    "streaming_source": null,
    "tiny_url": "https://www.jiosaavn.com/song/biba/ICERW0MFfQs",
    "title": "BIBA",
    "twitter_url": "http://twitter.com/share?url=https%3A%2F%2Fwww.jiosaavn.com%2Fsong%2Fbiba%2FICERW0MFfQs&text=%23NowPlaying+%22BIBA%22+%40jiosaavn+%23OurSoundtrack&related=jiosaavn",
    "url": "http://h.saavncdn.com/987/cd902d048c13e5ce6ca84cc409746a5d.mp3",
    "year": "2019"
}
```

### **Installation**:

Clone this repository using
```sh
$ git clone https://github.com/priyansh-anand/JioSaavnAPI
```
Enter the directory and change the branch to **python-module**
```sh
$ git checkout python-module
```
Install the module using
```sh
$ pip3 install .
```
Now you can import **jiosaavn** module in python3
```python
>> import jiosaavn
```


### **Usage**:
**If you enable lyrics search, it will take more time to fetch results**

---
##### **General search function**: (Supports Song Name, Song Link, Album Link, Playlist Link)
```python
>> res = jiosaavn.search(query="<insert-jiosaavn-link-or-query-here>", lyrics=True)
```
**Example:** 
```python
>> res = jiosaavn.search("perfect", lyrics=False)
>> print(type(res)) 
> list
>> print(res[0]) # get first song
>{'320kbps': 'true',
 'album': 'Ã·',
 'album_url': 'https://www.jiosaavn.com/album/÷/KelXOKU4pi4_',
 'albumid': '10436096',
 'artistMap': {'Ed Sheeran': '578407'},
 'cache_state': 'false',
 'copyright_text': '℗ 2017, Asylum Records UK, a division of Atlantic Records '
                   'UK, a Warner Music Group company.',
 'duration': '263',
 'encrypted_media_path': 'NMKyboFo/FjKriMVERRGRduWOIHiK1Zhg4mXFG8YE0b+SHoxlBqVMRyt6n4JwGMz',
 'encrypted_media_url': 'ID2ieOjCrwfgWvL5sXl4B1ImC5QfbsDyjLJatj30eCYo8W/T/nVreaZTbB+LPRvCYdcDxZKjYlxdk812I6LIsBw7tS9a8Gtq',
 'explicit_content': 0,
 'featured_artists': '',
 'featured_artists_id': '',
 'has_lyrics': 'false',
 'id': '6o8JoQ8b',
 'image': 'https://c.saavncdn.com/286/WMG_190295851286-English-2017-500x500.jpg',
 'label': 'Atlantic Records UK',
 'label_url': '/label/atlantic-records-uk-albums/Nq1WxI8CVrI_',
 'language': 'english',
 'lyrics_snippet': '',
 'media_preview_url': 'https://preview.saavncdn.com/286/71bb6cc3391ddf619a4a3f1a1134f1c4_96_p.mp4',
 'media_url': 'https://aac.saavncdn.com/286/71bb6cc3391ddf619a4a3f1a1134f1c4_320.mp4',
 'music': '',
 'music_id': '',
 'origin': 'none',
 'perma_url': 'https://www.jiosaavn.com/song/perfect/RgdTexthD1E',
 'play_count': 36465779,
 'primary_artists': 'Ed Sheeran',
 'primary_artists_id': '578407',
 'release_date': '2017-03-03',
 'rights': {'cacheable': True,
            'code': 0,
            'delete_cached_object': False,
            'reason': ''},
 'singers': 'Ed Sheeran',
 'song': 'Perfect',
 'starred': 'false',
 'starring': '',
 'type': '',
 'vcode': '010910140683676',
 'vlink': 'https://jiotunepreview.jio.com/content/Converted/010910140647552.mp3',
 'year': '2017'}

```

----


##### **Song search function**:
Returns a single song if a Jiosaavn URL is passed as query, else returns list of first 5 songs related to query
```python
>> res = jiosaavn.song(query="<insert-jiosaavn-link-or-query-here>", lyrics=True)
```
**Example:** 
```python
>> res = jiosaavn.song("perfect", lyrics=False)
>> print(type(res)) 
> list
>> print(res[0]) # get first song
>{'320kbps': 'true',
 'album': 'Ã·',
 'album_url': 'https://www.jiosaavn.com/album/÷/KelXOKU4pi4_',
 'albumid': '10436096',
 'artistMap': {'Ed Sheeran': '578407'},
 'cache_state': 'false',
 'copyright_text': '℗ 2017, Asylum Records UK, a division of Atlantic Records '
                   'UK, a Warner Music Group company.',
 'duration': '263',
 'encrypted_media_path': 'NMKyboFo/FjKriMVERRGRduWOIHiK1Zhg4mXFG8YE0b+SHoxlBqVMRyt6n4JwGMz',
 'encrypted_media_url': 'ID2ieOjCrwfgWvL5sXl4B1ImC5QfbsDyjLJatj30eCYo8W/T/nVreaZTbB+LPRvCYdcDxZKjYlxdk812I6LIsBw7tS9a8Gtq',
 'explicit_content': 0,
 'featured_artists': '',
 'featured_artists_id': '',
 'has_lyrics': 'false',
 'id': '6o8JoQ8b',
 'image': 'https://c.saavncdn.com/286/WMG_190295851286-English-2017-500x500.jpg',
 'label': 'Atlantic Records UK',
 'label_url': '/label/atlantic-records-uk-albums/Nq1WxI8CVrI_',
 'language': 'english',
 'lyrics_snippet': '',
 'media_preview_url': 'https://preview.saavncdn.com/286/71bb6cc3391ddf619a4a3f1a1134f1c4_96_p.mp4',
 'media_url': 'https://aac.saavncdn.com/286/71bb6cc3391ddf619a4a3f1a1134f1c4_320.mp4',
 'music': '',
 'music_id': '',
 'origin': 'none',
 'perma_url': 'https://www.jiosaavn.com/song/perfect/RgdTexthD1E',
 'play_count': 36465779,
 'primary_artists': 'Ed Sheeran',
 'primary_artists_id': '578407',
 'release_date': '2017-03-03',
 'rights': {'cacheable': True,
            'code': 0,
            'delete_cached_object': False,
            'reason': ''},
 'singers': 'Ed Sheeran',
 'song': 'Perfect',
 'starred': 'false',
 'starring': '',
 'type': '',
 'vcode': '010910140683676',
 'vlink': 'https://jiotunepreview.jio.com/content/Converted/010910140647552.mp3',
 'year': '2017'}

```
---

##### **Playlist URL Endpoint**:
```python
>> res = jiosaavn.playlist(query="<insert-jiosaavn-playlist-link>", lyrics=False)
```

---

##### **Album URL Endpoint**:
```python
>> res = jiosaavn.album(query="<insert-jiosaavn-album-link>", lyrics=False)
```

---

##### **Lyrics Endpoint**:
```python
>> res = jiosaavn.lyrics(query="<insert-jiosaavn-song-link-or-song-id>")
```


---

#### Star the Repo in case you liked it :)