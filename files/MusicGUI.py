"""

"""


import tkinter as tk
import Backend


if __name__ == '__main__':
    wn = tk.Tk()
    wn.title("Fapple FiPod")

    songs = Backend.create_songs()

    library = tk.LabelFrame(wn, text="Library", padx=5, pady=5)
    library.pack(fill="both", expand="yes", padx=5, pady=5)

    scrollbar = tk.Scrollbar(library)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    music_listbox = tk.Listbox(library, width=25, yscrollcommand=scrollbar.set)
    for i in range(len(songs)):
        music_listbox.insert(i, songs[i].get_song_name())
    music_listbox.pack()

    btn_start = tk.Button(library, text='Start', width=25, command=wn.destroy)
    btn_start.pack()

    btn_stop = tk.Button(library, text='Stop', width=25, command=wn.destroy)
    btn_stop.pack()

    btn_quit = tk.Button(library, text='Quit', width=25, command=wn.destroy)
    btn_quit.pack()

    song = tk.LabelFrame(wn, text="Song Details", padx=5, pady=5)
    song.pack(fill="both", expand="yes", padx=5, pady=5)

    song_name = tk.Label(song, text='Song Name').grid(row=0, sticky='e', padx=5)
    artist = tk.Label(song, text='Artist').grid(row=1, sticky='e', padx=5)
    genre = tk.Label(song, text='Genre').grid(row=2, sticky='e', padx=5)

    name_entry = tk.Entry(song, width=30)
    artist_entry = tk.Entry(song, width=30)
    genre_entry = tk.Entry(song, width=30)

    name_entry.grid(row=0, column=1, padx=5, pady=5)
    artist_entry.grid(row=1, column=1, padx=5, pady=5)
    genre_entry.grid(row=2, column=1, padx=5, pady=5)

    wn.mainloop()
