import audio_player as out
import transcriber as trans
import audio_recorder as rec
import time
import os

'''
This code allows users to test a CIO system, that transcribes their spoken input, 
generates an audio response, and plays it back. Upon running, the user will be prompted 
to start a test session. When the user speaks, their audio is recorded by the AudioRecorder 
class and transcribed using the Transcriber class. The text is then passed to the AudioPlayer 
class, which generates an audio response that is played back to the user. If the user is 
silent for more than 5 seconds, the program will automatically submit the recording 
for transcription and playback. The elapsed time of each test session is printed upon completion.
'''

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
        os.remove("audio/input.wav")
        os.remove("audio/out.mp3")
    else:
        print("Please enter a valid input")
