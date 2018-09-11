import argparse
import time
from mido import Message, MidiFile, MidiTrack
# '../Melancholy_-_Piano_Solo_Arrangement.mscz.mid'

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input",
                    help="Input Midi File")
parser.add_argument("-o", "--output",
                    help="Output Midi File")
args = parser.parse_args()

if args.input != None:
    print("input: {} output: equals {}".format(args.input, args.output))
else:
    pass
#import mido

mid = MidiFile(args.input)

print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

mid2 = MidiFile(type=1)

print(mid2)

for i, track in enumerate(mid2.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
'''
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('new_song.mid')
'''
