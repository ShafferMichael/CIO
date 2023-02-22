import whisper


class AudioTranscriber:
    def __init__(self, model_name="tiny.en"):
        self.model = whisper.load_model(model_name)
        self.text = None

    def transcribe(self, file_path):
        result = self.model.transcribe(file_path)
        self.text = result["text"]
        return self.text
