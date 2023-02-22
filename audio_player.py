import os
from gtts import gTTS

'''
This is a Python code that demonstrates the usage of the Google Text-to-Speech (gTTS) library.
The gTTS library is used to generate an audio file from the provided text using Google's
text-to-speech API. This code defines a class named AudioPlayer that has two methods,
generate_audio() and play_audio(). The generate_audio() method takes in the text to be
converted to speech, language code, output file name, and directory where the output file
should be saved. It generates an audio file in mp3 format and saves it to the specified
directory with the provided filename. The play_audio() method plays the generated audio
file using the mpg321 command-line utility.
'''


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
