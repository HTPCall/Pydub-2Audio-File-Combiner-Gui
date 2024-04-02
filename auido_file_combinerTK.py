import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
from pydub.silence import split_on_silence

def select_audio_file(var):
    file_path = filedialog.askopenfilename(filetypes=[("WAV Files", "*.wav")])
    var.set(file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_var.set(folder_path)

def combine_audio():
    en_audio_path = en_audio_var.get()
    fr_audio_path = fr_audio_var.get()
    output_folder = output_folder_var.get()

    if not en_audio_path or not fr_audio_path or not output_folder:
        print("Please fill in all fields.")
        return

    en_audio = AudioSegment.from_file(en_audio_path, format="wav")
    fr_audio = AudioSegment.from_file(fr_audio_path, format="wav")

    silence_threshold = -50  # dB
    min_silence_duration = 500  # milliseconds
    wait_duration = 700  # milliseconds
    wait_duration1 = 500  # milliseconds

    en_segments = split_on_silence(en_audio, min_silence_len=min_silence_duration, silence_thresh=silence_threshold)
    fr_segments = split_on_silence(fr_audio, min_silence_len=min_silence_duration, silence_thresh=silence_threshold)
    fr1_segments = split_on_silence(fr_audio, min_silence_len=min_silence_duration, silence_thresh=silence_threshold)

    combined_audio = AudioSegment.empty()
    /*
    for segment in fr1_segments:
        combined_audio += segment
        combined_audio += AudioSegment.silent(duration=wait_duration1)
    */

    for i in range(min(len(en_segments), len(fr_segments))):
        combined_audio += fr_segments[i]
        combined_audio += AudioSegment.silent(duration=wait_duration1)
        combined_audio += en_segments[i]
        combined_audio += AudioSegment.silent(duration=wait_duration)

    output_file = "combined_audio.wav"
    output_path = os.path.join(output_folder, output_file)

    combined_audio.export(output_path, format="wav")
    print("Audio files successfully combined.")

# Create GUI
window = tk.Tk()
window.title("Audio File Combiner")

en_audio_var = tk.StringVar()
fr_audio_var = tk.StringVar()
output_folder_var = tk.StringVar()

tk.Label(window, text="English Audio File:").grid(row=0, column=0, sticky="e")
tk.Entry(window, textvariable=en_audio_var, width=50).grid(row=0, column=1)
tk.Button(window, text="Select", command=lambda: select_audio_file(en_audio_var)).grid(row=0, column=2)

tk.Label(window, text="French Audio File:").grid(row=1, column=0, sticky="e")
tk.Entry(window, textvariable=fr_audio_var, width=50).grid(row=1, column=1)
tk.Button(window, text="Select", command=lambda: select_audio_file(fr_audio_var)).grid(row=1, column=2)

tk.Label(window, text="Output Folder:").grid(row=2, column=0, sticky="e")
tk.Entry(window, textvariable=output_folder_var, width=50).grid(row=2, column=1)
tk.Button(window, text="Select", command=select_output_folder).grid(row=2, column=2)

tk.Button(window, text="Combine", command=combine_audio).grid(row=3, column=1, pady=10)

window.mainloop() 
