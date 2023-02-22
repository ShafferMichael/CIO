import pyaudio
import wave
from pydub import AudioSegment

# Define recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 500  # Adjust this value as needed
MIN_RECORD_SECONDS = 5
MAX_RECORD_SECONDS = 30

try:
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open microphone stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    # Record audio while sound is present
    frames = []
    silence_duration = 0
    while True:
        try:
            data = stream.read(CHUNK)
        except KeyboardInterrupt:
            # User has interrupted the program, stop recording
            break
        volume = max(abs(int(d))
                     for d in wave.struct.unpack("%dh" % (len(data) / 2), data))

        if volume > THRESHOLD:
            # Sound detected, start recording
            if silence_duration == 0:
                print("Sound detected, recording started")
            silence_duration = 0
            frames.append(data)
        else:
            # No sound detected, stop recording if started
            silence_duration += 1 / (RATE / CHUNK)
            if silence_duration >= MIN_RECORD_SECONDS and len(frames) > 0:
                # Stop recording after a few seconds of silence
                print("Recording stopped due to inactivity")
                break

        # Stop recording after a fixed duration
        if len(frames) > MAX_RECORD_SECONDS * (RATE // CHUNK):
            print("Recording stopped due to maximum duration")
            break

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Convert recorded audio to AudioSegment object
    audio_segment = AudioSegment(data=b''.join(
        frames), sample_width=2, frame_rate=RATE, channels=CHANNELS)

    # Save recorded audio as an MP3 file
    audio_segment.export("audio/input.wav", format="wav")

except Exception as e:
    print("An error occurred:", e)
