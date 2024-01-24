"""

"""
import Songs


def create_songs():
    songs = []

    # create all the song objects
    classical1 = Songs.Song("Winter", "Alex-Productions", "Classical", "classical1.mp3")
    classical2 = Songs.Song("Family", "Alex-Productions", "Classical", "classical2.mp3")
    classical3 = Songs.Song("The Silent Witness", "Justin Allan Arnold", "Classical", "classical3.mp3")
    country1 = Songs.Song("Acoustic Folk Background Guitar", "Alex-Productions", "Country", "country1.mp3")
    country2 = Songs.Song("Friends Forever", "FSM Team", "Country", "country2.mp3")
    country3 = Songs.Song("New Lands", "Alex-Productions", "Country", "country3.mp3")
    country4 = Songs.Song("Banjo Fever", "Alexander Nakarada", "Country", "country4.mp3")
    country5 = Songs.Song("Happy", "Alexander Nakarada", "Country", "country5.mp3")
    indie1 = Songs.Song("Tokyo", "e s c p", "Indie Pop", "indie1.mp3")
    indie2 = Songs.Song("Steps On Clouds", "e s c p", "Indie Pop", "indie2.mp3")
    pop1 = Songs.Song("Popsicle", "Johny Grimes", "Pop", "pop1.mp3")

    # add all the classical songs to song list
    songs.append(classical1)
    songs.append(classical2)
    songs.append(classical3)

    # add all the country songs to song list
    songs.append(country1)
    songs.append(country2)
    songs.append(country3)
    songs.append(country4)
    songs.append(country5)

    # add all the indie pop songs to the song list
    songs.append(indie1)
    songs.append(indie2)

    # add all the pop songs to the song list
    songs.append(pop1)

    return songs

