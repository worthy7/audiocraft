# loop and watch for the next snippet file

import torchaudio
import soundcard as sc
import time

default_speaker = sc.default_speaker()

sniptime = 1
fil = "1744725785"

with default_speaker.player(samplerate=32000) as player:
    while True:
        # try getting the next snippet file
        try:
            snip_waveform, snip_sr =torchaudio.load(f"{fil}/{sniptime}.wav")
            player.play(snip_waveform[0]) # will buffer
            sniptime += 1
        except Exception as e:
            print("No more snippets")
            time.sleep(0.1) # wait a bit before trying again
            pass