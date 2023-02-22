import audio_player as out
import transcriber as trans
import audio_recorder as rec
import time

isTest = True
while isTest:
    start_time = time.time()
    user_input = input("\nWould you like to test CIO? (y/n) \n")
    if user_input.lower() == 'y':
        recorder = rec.AudioRecorder()  # initializes the recorder
        audio_segment = recorder.record()  # records the audio when the user speaks
        transcriber = trans.Transcriber()  # initializes the transcriber
        text = transcriber.transcribe(
            "audio/input.wav")  # transcribes the audio
        # initializes the audio player with text
        player = out.AudioPlayer(text)
        player.generate_audio()  # generates the audio file
        player.play_audio()  # plays the audio file
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: ", elapsed_time)
    elif user_input.lower() == 'n':
        isTest = False  # ends the loop
    else:
        print("Please enter a valid input")


# print(os.listdir())
# print(os.getcwd())
# print(os.chdir("audio"))

# ensure that the audio files are deleted after use of running gtts_test.py
# os.remove("audio/out.mp3")
