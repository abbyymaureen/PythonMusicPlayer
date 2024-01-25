"""
@author abbybrown
@filename Songs.py
@date 01/23/24

    This class allows for the creation of song objects containing the name of the song, the author of the song, the
    genre of the song, and the filename of the song.
"""


class Songs:
    song_name = ""
    artist = ""
    genre = ""
    mp3_file = ""

    # constructor
    def __init__(self, song, artist, genre, mp3):
        self.set_song_name(song)
        self.set_artist(artist)
        self.set_genre(genre)
        self.set_mp3_file(mp3)

    # sets the song name (parameter: song - string)
    def set_song_name(self, song):
        self.song_name = song

    # returns the song name (returns string)
    def get_song_name(self):
        return self.song_name

    # sets the artist name (parameter: artist - string)
    def set_artist(self, artist):
        self.artist = artist

    # gets the artist name (returns string)
    def get_artist(self):
        return self.artist

    # sets the genre (parameter: genre - string)
    def set_genre(self, genre):
        self.genre = genre

    # gets the genre (returns string)
    def get_genre(self):
        return self.genre

    # sets the name of the mp3 file (parameter: mp3 - string)
    def set_mp3_file(self, mp3):
        self.mp3_file = mp3

    # gets the mp3 file (returns string)
    def get_mp3_file(self):
        return self.mp3_file
