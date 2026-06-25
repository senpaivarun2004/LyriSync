import time
import pygame

def calibrate():
    lyrics = [
        "Baato-baato me hi, Khwabo-khwabo me hi mere qareeb hai tu",
        "Teri talab mujhko, teri talab, jaana, ho tu kabhi ru-ba-ru",
        "Shor-sharaba jo seene me hai mere, kaise bayaan mai karuu",
        "Haal jo mera hai, mai kis ko batau?",
        "Mere sahiba, dil na kiraaye ka, thoda to sambhalo na",
        "Nazuk hai yeh, toot jaata hai",
        "Sahiba, neende-veende aaye na,",
        "Raate kaati jaaye na",
        "Tera hi khayal din-rain aata hai",
    ]

    pygame.mixer.init()
    pygame.mixer.music.load("sahiba_audio.mp3.mp3")

    print("=" * 60)
    print("  SAHIBA - Lyric Timestamp Calibration Tool")
    print("=" * 60)
    print()
    print("The music will start playing.")
    print("Press ENTER exactly when you hear each line being sung.")
    print()
    input("Press ENTER to start the music...")

    pygame.mixer.music.play()
    start_time = time.time()
    timestamps = []

    for i, line in enumerate(lyrics):
        print(f"\n  Line {i+1}/{len(lyrics)}:")
        print(f"  \"{line}\"")
        input(f"  >> Press ENTER when this line starts... ")
        ts = round(time.time() - start_time, 1)
        timestamps.append(ts)
        print(f"     Recorded: {ts}s")

    pygame.mixer.music.stop()

    print("\n" + "=" * 60)
    print("  DONE! Copy this into sahiba.py (replace the timed_lyrics list):")
    print("=" * 60)
    print()
    print("    timed_lyrics = [")
    for ts, line in zip(timestamps, lyrics):
        print(f'        ({ts}, "{line}"),')
    print("    ]")
    print()

if __name__ == "__main__":
    calibrate()
