import whisper

'''
The whisper library is a toolkit for working with Automatic Speech Recognition (ASR) models
and datasets. The Transcriber class in this code uses the whisper library to transcribe an
audio file at a specified file path using a pre-trained model. The constructor of the
Transcriber class initializes the transcriber with a specified model (default is "medium.en").
The transcribe method of the Transcriber class takes a file path as input and returns the
transcribed text of the audio file at the given path using the specified model. This code
demonstrates how the Transcriber class can be used to transcribe audio files using
the whisper library.
'''


class Transcriber:
    def __init__(self, model_name="medium.en"):
        # Initializes the transcriber with the specified model
        self.model = whisper.load_model(model_name)
        # The text that will be transcribed
        self.text = None

    def transcribe(self, file_path):
        # Transcribes the audio file at the specified file path using the transcriber's model
        result = self.model.transcribe(file_path)
        # Sets the transcribed text to the result's "text" field
        self.text = result["text"]
        # Returns the transcribed text
        return self.text


if __name__ == "__main__":
    # Creates a new transcriber object
    transcriber = Transcriber()
    # Transcribes the audio file at the specified path
    transcribed_text = transcriber.transcribe("audio/input.wav")
