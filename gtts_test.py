import os  # uses mpg321 (audio player) to play the audio file
from gtts import gTTS  # Google Text-to-Speech

# the text that you want to convert to audio
toSpeak = "Welcome to the andromeda galaxy"

# create a gTTS object
tts = gTTS(text=toSpeak, lang="en")

# save the audio file
tts.save("audio/out.mp3")

# play the audio
os.system("mpg321 audio/out.mp3")
