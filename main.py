import os
import audio_player as out
import transcriber as feed


transcriber = feed.Transcriber()
text = transcriber.transcribe("audio/input.wav")

'''
Initialize the audio player and generate the audio file with the text
'''
player = out.AudioPlayer(text)
player.generate_audio()
player.play_audio()


print("Hello World!")


# print(os.listdir())
# print(os.getcwd())
# print(os.chdir("audio"))

# ensure that the audio files are deleted after use of running gtts_test.py
# os.remove("audio/out.mp3")
