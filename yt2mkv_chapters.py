import json
import sys

# Command line parameters message.
if len(sys.argv) != 3:
    print("You must call like this:\n" +
          "python yt2mkv_chapters.py youtube.json matroska.txt\n" +
          "'youtube.json' can be '--' if you want to read from stdin.\n" +
          "'matroska.txt' can be '--' if you want to write to stdout.\n" +
          "You can download the json file from YouTube like this: (you must install youtube-dl previously)\n" +
          "youtube-dl --dump-json <YouTube_URL> > youtube.json\n" +
          "Also, you can pipe the whole thing like this:\n" +
          "youtube-dl --dump-json <YouTube_URL> | python yt2mkv_chapters.py -- matroska.txt\n")
    exit()

# Load and parse json
input_file = 0 if sys.argv[1] == '--' else sys.argv[1]
with open(input_file, encoding='utf-8') as f:
    chapters = json.load(f)

# Export Matroska chapters simple file format
output_file = 1 if sys.argv[2] == '--' else sys.argv[2]
chapters = chapters['chapters']
with open(output_file, "w", encoding='utf-8') as f:
    for i in range(len(chapters)):
        title = chapters[i]['title']
        time = chapters[i]['start_time']
        hours = time // 3600
        minutes = (time % 3600) // 60
        seconds = time % 60
        f.write("CHAPTER%02u=%02u:%02u:%02.3f\n" % (i, hours, minutes, seconds))
        f.write("CHAPTER%02uNAME=%s\n" % (i, title))