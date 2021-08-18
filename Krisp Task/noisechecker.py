import json
from pygame import mixer    # for play audio
from pathlib import Path    # for directory listing
import ntpath   # for get filename from path

labeled_file = {}
DIRECTORY = Path(r"MP3_resources")    # path of folder with audios
mixer.init()

for audio in DIRECTORY.glob('*.mp3'):
    print (str(audio))
    print("Playing The", ntpath.basename(str(audio)))
    mixer.music.load(str(audio))    # add each file to the queue
    mixer.music.play()

    while True:
        print("Press 'n' for a noisy label and 'c' for a clean label.")
        query = input("  ")
        if query == 'n' or query == 'c':    # Stop and label the audio
            if query == 'n':
                labeled_file.update({ntpath.basename(str(audio)): "noisy"})
            else:
                labeled_file.update({ntpath.basename(str(audio)): "clean"})
            break

with open("audio_labeled_detail.json", "w") as filename_with_label:
    json.dump(labeled_file, filename_with_label, indent=4)


