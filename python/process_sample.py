#import mido
from mido import MidiFile
mid = MidiFile('../Melancholy_-_Piano_Solo_Arrangement.mscz.mid')

print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
