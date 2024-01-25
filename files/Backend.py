"""
@author abbybrown
@filename Backend.py
@date 01/24/24

    This backend allows for the creation of all of our songs and returning these song objects in a list. We also have a
    method that allows the user to search and retrieve a specific song from the list.
"""
import Songs


# creates all the songs in our library and returns a list containing these song objects
def create_songs():
    songs = []

    # create all the song objects
    classical1 = Songs.Songs("Winter", "Alex-Productions", "Classical", "songs/classical1.mp3")
    classical2 = Songs.Songs("Family", "Alex-Productions", "Classical", "songs/classical2.mp3")
    classical3 = Songs.Songs("The Silent Witness", "Justin Allan Arnold", "Classical", "songs/classical3.mp3")
    country1 = Songs.Songs("Acoustic Folk Background Guitar", "Alex-Productions", "Country", "songs/country1.mp3")
    country2 = Songs.Songs("Friends Forever", "FSM Team", "Country", "songs/country2.mp3")
    country3 = Songs.Songs("New Lands", "Alex-Productions", "Country", "songs/country3.mp3")
    country4 = Songs.Songs("Banjo Fever", "Alexander Nakarada", "Country", "songs/country4.mp3")
    country5 = Songs.Songs("Happy", "Alexander Nakarada", "Country", "songs/country5.mp3")
    indie1 = Songs.Songs("Tokyo", "e s c p", "Indie Pop", "songs/indie1.mp3")
    indie2 = Songs.Songs("Steps On Clouds", "e s c p", "Indie Pop", "songs/indie2.mp3")
    pop1 = Songs.Songs("Popsicle", "Johny Grimes", "Pop", "songs/pop1.mp3")
    rock1 = Songs.Songs("Let's Rock", "Alex=Productions", "Rock", "songs/rock1.mp3")
    rock2 = Songs.Songs("Banger", "Alexander Nakarada", "Rock", "songs/rock2.mp3")
    lofi1 = Songs.Songs("Downtown Walk", "e s c p", "LoFi", "songs/lofi1.mp3")
    lofi2 = Songs.Songs("Lunar New Year", "Alex-Productions", "LoFi", "songs/lofi2.mp3")
    lofi3 = Songs.Songs("Rain, Book And Cup Of Tea", "e s c p", "LoFi", "songs/lofi3.mp3")
    lofi4 = Songs.Songs("Small Town Boy", "e s c p", "LoFi", "songs/lofi4.mp3")


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

    # add all the rock songs to the song list
    songs.append(rock1)
    songs.append(rock2)

    # add all the LoFi songs to the song list
    songs.append(lofi1)
    songs.append(lofi2)
    songs.append(lofi3)
    songs.append(lofi4)

    return songs


# finds the song we want (parameter) in our list of songs (parameter)
def find_song(my_song, songs):
    for i in range(len(songs)):
        if songs[i].get_song_name() == my_song:
            return songs[i]
    return False

