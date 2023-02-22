import os

print("Hello World!")
# print(os.listdir())
# print(os.getcwd())
# print(os.chdir("audio"))

# ensure that the audio files are deleted after use of running gtts_test.py
os.remove("audio/out.mp3")
