# Lyric Timestamp Calibration Tool

An interactive Python utility designed to calibrate and record real-time timestamps for synchronized song lyrics.

## Features

- **Interactive Calibration**: Plays the song `sahiba_audio.mp3.mp3` and prompts you to press `ENTER` when each line starts.
- **Real-Time Recording**: Tracks elapsed time from the start of the song and maps it to the respective line.
- **Copy-Paste Output**: Generates a formatted python list (`timed_lyrics`) that can be pasted directly into `sahiba.py`.

## Prerequisites

Make sure you have Python installed, along with the `pygame` library:

```bash
pip install pygame
```

## Setup & Running

1. Ensure the audio file `sahiba_audio.mp3.mp3` is in the same directory as the script.
2. Run the calibration script:

```bash
python calibrate.py
```

## How to Use

1. Run the script and press `ENTER` to start the music.
2. Listen to the track. Exactly when you hear the vocals start singing the displayed line, press `ENTER`.
3. Once all lines are calibrated, the program will output a Python list structure:
   ```python
   timed_lyrics = [
       (0.5, "Baato-baato me hi, Khwabo-khwabo me hi mere qareeb hai tu"),
       ...
   ]
   ```
4. Copy this list and replace the existing `timed_lyrics` block in `sahiba/sahiba.py`.
