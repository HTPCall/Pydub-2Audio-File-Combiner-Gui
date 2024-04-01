# Audio-File-Combiner-with-Pydub


This Python script allows you to combine two audio files (in WAV format) by splitting them into segments based on silence and then interleaving the segments with specified durations of silence between them. It provides a graphical user interface (GUI) built with Tkinter for easy selection of input files and output folder.

## Requirements

- Python 3.x
- pydub library
- tkinter library

## Installation

1. Clone the repository or download the script file.
2. Install the required libraries by running the following command:
   ```
   pip install pydub
   ```

## Usage

1. Run the script using the following command:
   ```
   python audio_combiner.py
   ```
2. The GUI window will open.
3. Click on the "Select" button next to "English Audio File" and choose the English audio file (in WAV format).
4. Click on the "Select" button next to "French Audio File" and choose the French audio file (in WAV format).
5. Click on the "Select" button next to "Output Folder" and choose the folder where you want to save the combined audio file.
6. Click on the "Combine" button to start the audio combination process.
7. The combined audio file will be saved in the selected output folder with the name "combined_audio.wav".

## Customization

You can customize the following parameters in the script:

- `silence_threshold`: The threshold (in dB) below which audio is considered silence. Default is -50 dB.
- `min_silence_duration`: The minimum duration (in milliseconds) of silence required to split the audio. Default is 500 ms.
- `wait_duration`: The duration (in milliseconds) of silence to be added between the French and English segments. Default is 700 ms.
- `wait_duration1`: The duration (in milliseconds) of silence to be added between the French segments. Default is 500 ms.

## Notes

- The script assumes that the input audio files are in WAV format. If your audio files are in a different format, you may need to modify the script accordingly.
- The script uses the pydub library for audio processing, which relies on the FFmpeg library. Make sure you have FFmpeg installed on your system.
- The GUI is built using the Tkinter library, which is included in the Python standard library.

## License

This script is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
