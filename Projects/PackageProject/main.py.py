#
#
#
import random_name_generator
from pydub import AudioSegment
from pydub.playback import play

print("Hello user, I would like to make some friends, what is your name?")

name = input()

print("Hello " + name + " I may have lied to you, I *do* want to make friends, but I am actaully a psychic.")
print("I am going to read your mind and try to guess the names of your friends.")

song = AudioSegment.from_wav("magic.wav")
play(song)





