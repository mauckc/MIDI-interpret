# MIDI-interpret
Dean's MIDI project


## Python
### Mido Package
reference:
https://mido.readthedocs.io/en/latest/midi_files.html#opening-a-file
 
#### Read a Midi file
print out all messages in the file
 ```python3
from mido import MidiFile
mid = MidiFile('../Melancholy_-_Piano_Solo_Arrangement.mscz.mid')

print(mid)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
 ```
 
#### Creating a new File

  ```python3
 from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
track.append(Message('note_on', note=64, velocity=64, time=32))
track.append(Message('note_off', note=64, velocity=127, time=32))

mid.save('new_song.mid')
 ```
 
#### File Types
There are three types of MIDI files:

*type 0 (single track): all messages are saved in one track
*type 1 (synchronous): all tracks start at the same time
*type 2 (asynchronous): each track is independent of the others
 
When creating a new file, you can select type by passing the type keyword argument, or by setting the type attribute:
```python3
mid = MidiFile(type=2)
mid.type = 1
```

## MIDIVIS
Possible library:
https://github.com/Gimpneek/midivis

## Roll Functionality
git submodule added https://github.com/exeex/midi-visualization python/midi-visualization

