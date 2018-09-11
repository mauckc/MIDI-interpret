from roll import MidiFile

if __name__ == "__main__":
    mid = MidiFile("new_song.mid")

    # get the list of all events
    # events = mid.get_events()

    # get the np array of piano roll image
    roll = mid.get_roll()

    # draw piano roll by pyplot
    mid.draw_roll()
