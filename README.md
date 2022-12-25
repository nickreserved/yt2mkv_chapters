# yt2mkv_chapters.py


## Why you are here

You just download a full music album from YouTube. Or you just download a video from Youtube, but in YouTube it has chapters.

You need to download the YouTube chapters (start time and title) to merge them with your just downloaded video.

You need to merge YouTube chapters with your just downloaded video in a Matroska MKV video file (or a Matroska MKA audio file if we talk about a full music album).


## How to download video from YouTube

This is possible with another  great program, the `youtube-dl`. You can find it here: https://youtube-dl.org/

Just run `youtube-dl <YouTubeURL>` and the video will be downloaded locally.


## How to download video chapters from YouTube

You cannot download just chapters from YouTube. But you can download a JSON file which contains the chapters.

Just run `youtube-dl --dump-json <YouTubeURL>` and the JSON file for that video, containing the chapters, will be downloaded locally.


## How to merge both video and video chapters

With another great program, the MKVToolnix. You can find it here: https://mkvtoolnix.download/

Basically this is a group of programs. We use either `mkvmerge` which is command line and hard, or the program with graphical user interface which is easy.

But there is a problem: The JSON file from YouTube is not compatible with MKVToolnix chapters file format.


## How to make the YouTube JSON file compatible with MKVToolnix chapters file format

Here we are! With the `yt2mkv_chapters.py` python script.

Just run `python yt2mkv_chapters.py YouTubeJSON.json matroska.txt` and the YouTube JSON file will be converted to matroska chapters file format.

Basically, the Matroska specification supports 2 chapters file formats: The easy and the XML. The script exports to easy file format because does not lack functionality.

Both file formats can be found here: https://mkvtoolnix.download/doc/mkvmerge.html#mkvmerge.chapters


## Command line options of `yt2mkv_chapters.py`
```
python yt2mkv_chapters.py <JSON> <TXT>
```
`JSON` can be the JSON file downloaded from YouTube, or can be `--` to read from `stdin`.

`TXT` can be the simple matroska chapters file to export, or can be `--` to write to `stdout`.

Without parameters, a help message printed in `stdout`.


## Direct convert to simple matroska chapters file
Ok, lets do an example with piping:
```
youtube-dl --dump-json https://www.youtube.com/watch?v=L928CmhAPQY | python yt2mkv_chapters.py -- "Blood (1997) [Midi OST].txt"
```
