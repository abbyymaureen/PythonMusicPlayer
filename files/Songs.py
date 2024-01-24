"""

"""


class Songs:
    song_name = ""
    artist = ""
    genre = ""
    mp3_file = ""

    def __init__(self, song, artist, genre, mp3):
        self.set_song_name(song)
        self.set_artist(artist)
        self.set_genre(genre)
        self.set_mp3_file(mp3)

    def set_song_name(self, song):
        self.song_name = song

    def get_song_name(self):
        return self.song_name

    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self):
        return self.genre

    def set_mp3_file(self, mp3):
        self.mp3_file = mp3

    def get_mp3_file(self):
        return self.mp3_file
