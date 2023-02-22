import pyaudio
import wave
from pydub import AudioSegment


class AudioRecorder:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024, threshold=500,
                 min_record_seconds=5, max_record_seconds=30):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.threshold = threshold
        self.min_record_seconds = min_record_seconds
        self.max_record_seconds = max_record_seconds
        self.frames = []

    def record(self):
        try:
            # Initialize PyAudio
            audio = pyaudio.PyAudio()

            # Open microphone stream
            stream = audio.open(format=self.format, channels=self.channels,
                                rate=self.rate, input=True, frames_per_buffer=self.chunk)

            # Record audio while sound is present
            silence_duration = 0
            loading_counter = 0
            while True:
                try:
                    data = stream.read(self.chunk)
                except KeyboardInterrupt:
                    # User has interrupted the program, stop recording
                    break
                volume = max(abs(int(d))
                             for d in wave.struct.unpack("%dh" % (len(data) / 2), data))

                if volume > self.threshold:
                    # Sound detected, start recording
                    if silence_duration == 0:
                        loading_counter += 1
                        if loading_counter % 10 == 0:
                            print()
                        else:
                            print('* ', end='')

                    silence_duration = 0
                    self.frames.append(data)
                else:
                    # No sound detected, stop recording if started
                    silence_duration += 1 / (self.rate / self.chunk)
                    if silence_duration >= self.min_record_seconds and len(self.frames) > 0:
                        # Stop recording after a few seconds of silence
                        print(
                            "\n\nRECORDING STOP: Silence detected longer than minimum duration")
                        break

                # Stop recording after a fixed duration
                if len(self.frames) > self.max_record_seconds * (self.rate // self.chunk):
                    print("\n\nRECORDING STOP: maximum duration reached")
                    break

            # Stop recording
            stream.stop_stream()
            stream.close()
            audio.terminate()

            # Convert recorded audio to AudioSegment object
            audio_segment = AudioSegment(data=b''.join(
                self.frames), sample_width=2, frame_rate=self.rate, channels=self.channels)

            # Save recorded audio as an MP3 file
            audio_segment.export(
                "audio/input.wav", format="wav")

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    # example usage
    recorder = AudioRecorder()
    audio_segment = recorder.record()
