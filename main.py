import tkinter as tk
from tkinter import filedialog, messagebox
import os
from audio_utils import *
from playback import *

class AudioApp:
    def __init__(self, root):
        self.root = root
        root.title("Vocal & Instrumental Extractor")

        self.current_song = None
        self.songs_dir = "songs/"
        os.makedirs(self.songs_dir, exist_ok=True)
        os.makedirs("output", exist_ok=True)

        # Add Song Button
        tk.Button(root, text="Add Song", width=20, command=self.add_song).pack(pady=(10, 0))

        # Song list
        self.listbox = tk.Listbox(root, bg="white", fg="black", width=60, selectbackground="lightblue", selectforeground="black")
        self.listbox.pack(pady=10)

        # Controls frame (Play/Pause/Stop/Extract)
        controls = tk.Frame(root)
        controls.pack(pady=10)

        tk.Button(controls, text="Play", width=12, command=self.play).grid(row=0, column=0, padx=5)
        tk.Button(controls, text="Pause/Resume", width=12, command=self.pause).grid(row=0, column=1, padx=5)
        tk.Button(controls, text="Stop", width=12, command=self.stop).grid(row=0, column=2, padx=5)
        tk.Button(controls, text="Extract", width=12, command=self.extract).grid(row=0, column=3, padx=5)
        tk.Button(controls, text="Extract (Librosa)", width=15, command=self.extract_librosa).grid(row=0, column=4, padx=5)

        # On close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def add_song(self):
        file = filedialog.askopenfilename(initialdir=self.songs_dir, filetypes=[("WAV Files", "*.wav")])
        if file:
            filename = os.path.basename(file)
            dest = os.path.join(self.songs_dir, filename)
            if not os.path.exists(dest):
                os.rename(file, dest)
            if filename not in self.listbox.get(0, "end"):
                self.listbox.insert(tk.END, filename)

    def extract_librosa(self):
        path = self.get_selected_song_path()
        if not path: return
        from audio_utils import extract_vocals_instrumentals_librosa
        vocal, instr = extract_vocals_instrumentals_librosa(path)
        for f in [vocal, instr]:
            fname = os.path.basename(f)
            if fname not in self.listbox.get(0, "end"):
                self.listbox.insert(tk.END, fname)
        messagebox.showinfo("Done", "Librosa-based extraction complete.")


    def get_selected_song_path(self):
        selection = self.listbox.get(tk.ACTIVE)
        song_path = os.path.join(self.songs_dir, selection)
        if not os.path.exists(song_path):
            # Check in output folder (for extracted files)
            song_path = os.path.join("output", selection)
        return song_path


    def play(self):
        song_path = self.get_selected_song_path()
        self.current_song = song_path
        play_audio(song_path)

    def stop(self):
        stop_audio()

    def pause(self):
        pause_audio()

    def extract(self):
        path = self.get_selected_song_path()
        if not path: return
        vocal, instr = extract_vocals_instrumentals(path)
        for f in [vocal, instr]:
            fname = os.path.basename(f)
            if fname not in self.listbox.get(0, "end"):
                self.listbox.insert(tk.END, fname)
        messagebox.showinfo("Done", "Vocal/Instrumental extraction complete.")

    def on_close(self):
        stop_audio()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioApp(root)
    root.mainloop()
