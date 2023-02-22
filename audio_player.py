import os
from gtts import gTTS


class AudioPlayer:
    def __init__(self, text, lang="en", filename="output.mp3", directory="audio"):
        self.text = text
        self.lang = lang
        self.filename = filename
        self.directory = directory

    def generate_audio(self):
        # create a gTTS object
        tts = gTTS(text=self.text, lang=self.lang)

        # save the audio file
        filepath = os.path.join(self.directory, self.filename)
        tts.save(filepath)

        print(f"Audio file generated at {filepath}")

    def play_audio(self):
        # play the audio
        filepath = os.path.join(self.directory, self.filename)
        os.system(f"mpg321 {filepath}")


if __name__ == "__main__":
    # example usage
    player = AudioPlayer("Welcome to the andromeda galaxy!")
    player.generate_audio()
    player.play_audio()
