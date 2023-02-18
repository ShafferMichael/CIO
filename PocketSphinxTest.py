from pocketsphinx import LiveSpeech

speech = LiveSpeech()

while True:
    for phrase in speech:
        print(phrase)
        if 'finish' in phrase:
            break
    break
