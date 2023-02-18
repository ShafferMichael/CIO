import os
from pocketsphinx import get_model_path, Decoder
from subprocess import call

# Set up the paths to the required Festival files
festival_bin = "/usr/bin/festival"
festival_lib = "/usr/lib/festival"

# Set up the paths to the required Sphinx files
model_path = get_model_path()
hmm = os.path.join(model_path, 'en-us')
dict_path = os.path.join(model_path, 'cmudict-en-us.dict')
lm_path = os.path.join(model_path, 'en-us.lm.bin')

# Set up the pocketsphinx decoder
config = Decoder.default_config()
config.set_string('-hmm', hmm)
config.set_string('-dict', dict_path)
config.set_string('-lm', lm_path)
decoder = Decoder(config)

# Get user input
input_text = input("Enter a phrase to say: ")

# Decode the user input
decoder.start_utt()
decoder.process_raw(input_text.encode(), False, True)
decoder.end_utt()

# Get the recognized text
recognized_text = decoder.hyp().hypstr

# Print the recognized text
print("You said: {}".format(recognized_text))

# Use Festival to convert the recognized text to speech and play it back
call(["echo", recognized_text, "|", festival_bin, "--libdir", festival_lib, "--tts"])
