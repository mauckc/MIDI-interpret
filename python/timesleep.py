
from mido import MidiFile
# '../Melancholy_-_Piano_Solo_Arrangement.mscz.mid'
for msg in MidiFile('song.mid'):
    time.sleep(msg.time)
    if not msg.is_meta:
        port.send(msg)
