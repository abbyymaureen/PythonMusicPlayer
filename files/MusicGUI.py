"""
@author abbybrown
@filename MusicGUI.py
@date 01/23/24

    This GUI lets the user pick songs from a listbox of options. Once selected, the song details (name, artist, genre)
    will populate at the bottom of the music player device. The user can play, stop, and quit the program. The user
    cannot edit any of the details of the song.

    GUI Design Help:
    https://www.tutorialspoint.com/python/tk_labelframe.htm
    https://www.geeksforgeeks.org/python-gui-tkinter/
    Clue Files provided by Dr. Theodore Wendt and Mr. Nathan Williams

    General Debugging:
    ChatGPT
"""


import tkinter as tk
import Backend
import subprocess


def update_fields(event):
    # get the index of the song in the listbox
    selected_song_index = music_listbox.curselection()

    if selected_song_index:
        # will return list, so get the first element of the list
        selected_song_index = selected_song_index[0]
        selected_song = songs[selected_song_index]

        # update the song information
        name_entry.delete(0, "end")
        name_entry.insert(0, selected_song.get_song_name())

        artist_entry.delete(0, "end")
        artist_entry.insert(0, selected_song.get_artist())

        genre_entry.delete(0, "end")
        genre_entry.insert(0, selected_song.get_genre())


def start_music():
    # needs to be global in order to use in other functions
    global player_process
    selected_song_index = music_listbox.curselection()

    if selected_song_index:
        # will return list, so get the first element of the list
        selected_song_index = selected_song_index[0]
        selected_song = songs[selected_song_index]

        # if there is an existing player_process, terminate it before starting a new one
        if player_process and player_process.poll() is None:
            end_music()

        player_process = subprocess.Popen(["mpg123", selected_song.get_mp3_file()])


def end_music():
    # again, use global variable so it can be used across functions
    global player_process
    if player_process and player_process.poll() is None:
        player_process.terminate()


def quit_app():
    # terminate music player if it is playing
    if player_process and player_process.poll() is None:
        player_process.terminate()

    # destroy the window
    wn.destroy()


if __name__ == '__main__':
    wn = tk.Tk()
    wn.title("Fapple FiPod")

    # get the list of songs
    songs = Backend.create_songs()

    # create the library label frame window
    library = tk.LabelFrame(wn, text="Library", padx=5, pady=5)
    library.pack(fill="both", expand="yes", padx=5, pady=5)

    # add a scrollbar in case there are too many songs
    scrollbar = tk.Scrollbar(library)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # add all the songs to the listbox via looping
    music_listbox = tk.Listbox(library, width=25, yscrollcommand=scrollbar.set)
    for i in range(len(songs)):
        music_listbox.insert(i, songs[i].get_song_name())
    music_listbox.pack()

    # bind the selection of a song to the update field function
    music_listbox.bind("<<ListboxSelect>>", update_fields)

    # create buttons
    btn_start = tk.Button(library, text='Start', width=25, command=start_music)
    btn_start.pack()

    btn_stop = tk.Button(library, text='Stop', width=25, command=end_music)
    btn_stop.pack()

    btn_quit = tk.Button(library, text='Quit', width=25, command=quit_app)
    btn_quit.pack()

    # create new label frame for the song details
    song = tk.LabelFrame(wn, text="Song Details", padx=5, pady=5)
    song.pack(fill="both", expand="yes", padx=5, pady=5)

    # add a label for the song name, artist, and genre, sticky to the east
    tk.Label(song, text='Song Name').grid(row=0, sticky='e', padx=5)
    tk.Label(song, text='Artist').grid(row=1, sticky='e', padx=5)
    tk.Label(song, text='Genre').grid(row=2, sticky='e', padx=5)

    # create an entry label for each song
    name_entry = tk.Entry(song, width=30)
    artist_entry = tk.Entry(song, width=30)
    genre_entry = tk.Entry(song, width=30)

    # make these entry labels read only
    # https://www.delftstack.com/howto/python-tkinter/how-to-make-tkinter-text-widget-read-only/
    name_entry.bind("<Key>", lambda a: "break")
    artist_entry.bind("<Key>", lambda a: "break")
    genre_entry.bind("<Key>", lambda a: "break")

    # grid these to the correct spot
    name_entry.grid(row=0, column=1, padx=5, pady=5)
    artist_entry.grid(row=1, column=1, padx=5, pady=5)
    genre_entry.grid(row=2, column=1, padx=5, pady=5)

    player_process = None

    wn.mainloop()
