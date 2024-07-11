'''
The modules below do not require internet connection to function.
'''
import soundfile as sf
import pyrubberband as pyrb

from pydub import AudioSegment
from pydub.playback import play

import pyaudio
import wave
import simpleaudio as sa

from Utility import print_default_error_message

def record_audio(filename, duration=5, rate=44100, chunk=1024, channels=1, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for i in range(int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording done.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def change_pitch_and_tone(input_file, output_file, pitch_factor, tone_factor):
    # Load audio file
    data, sample_rate = sf.read(input_file)

    # Modify pitch and tone using pyrubberband
    data_stretch = pyrb.time_stretch(data, sample_rate, pitch_factor)
    data_pitch = pyrb.pitch_shift(data_stretch, sample_rate, tone_factor)

    # Save modified audio
    sf.write(output_file, data_pitch, sample_rate)

def play_audio(filename):
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Example usage:
def voice_changer():
    try:
        # record_audio("Assets/wav_files/output.wav", duration=5)
        # play_audio("Assets/wav_files/output.wav")
        filename = "Assets/wav_files/input.wav"
        voice_changer_inputfile(filename, 0.5, 1.5)
    except Exception as e:
        print_default_error_message(e)

def voice_changer_inputfile(filename, octaves, speed):
    # Load audio file
    audio = AudioSegment.from_file(filename)

    # Example: Increase pitch by semitones
    new_sample_rate = int(audio.frame_rate * (2 ** octaves))
    high_pitched = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})
    high_pitched = high_pitched.set_frame_rate(audio.frame_rate)

    # Example: Change tone by adjusting speed
    # Increase speed to raise pitch, decrease to lower
    tone_changed = audio.speedup(playback_speed=speed)

    # Play modified audio
    play(high_pitched)
    play(tone_changed)

    # Export modified audio
    high_pitched.export("Assets/wav_files/high_pitched_audio.wav", format="wav")
    tone_changed.export("Assets/wav_files/tone_changed_audio.wav", format="wav")

'''
getting FFmpeg errors - ignore this file for now
'''