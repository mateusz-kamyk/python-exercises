#!/usr/bin/env python3

from pydub import AudioSegment

test_audio = AudioSegment.from_mp3("mp3_test.mp3")

def get_properties():
    duration = len(test_audio)
    frame_rate = test_audio.frame_rate
    frame_width = test_audio.frame_width
    loudness = test_audio.rms

    print(f"Duration: {duration} ms\nFrequency: {frame_rate} Hz\nFrame width: {frame_width} (1 means 8 bit)\nLoudness: {loudness} Hz")

if __name__=="__main__":
    get_properties()




