import re
import os
import numpy as np
from mingus.containers import Note, NoteContainer,Track,Bar
from mingus.midi import fluidsynth as fs
fs.init("sound_fonts/FluidR3_GM.SF2")
m_space = os.listdir("songs")

# Start of utility functions

def file_to_plaintext(txt_filename):
    # converts a txt file(the plaintext) to a list of numbers 0 to 88 
    # txt file should be 32 lines of notes(example: "C-3") or rests ("r")
    # the "-8" makes it so A0 (the first note on the piano is coded as 1 and not 9)
    # this makes room for a rest to be coded as a 0
    # in the conversion to a Track object we add this 8 back in
    txt = open(txt_filename, 'r')
    m = []
    for i,v in enumerate(txt.readlines()):
        cleaned = re.sub("\n","",v)
        cleaned = 0 if cleaned == "r" else (int(Note(cleaned))-8)
        m.append(cleaned)
    return m

def message_to_Track(message,this_meter = (4,4)):
    # Takes a list of integers 0 to 88 (rest, A0,A#0,....C8)
    # and converts it to a mingus Track object to be played
    track = Track()
    bar = Bar(meter = this_meter)
    for i,v in enumerate(message):
        if bar.is_full():
            track + bar
            bar = Bar(meter = this_meter)
            if v > 0:
                bar + Note().from_int(v + 8)
            else:
                bar + None
        else:
            if v > 0:
                bar + Note().from_int(v + 8)
            else:
                bar + None
    track + bar # Add the final bar since it doesn't loop after filling the last bar
    return track

# Shift Cipher
def shift_key_gen():
    # Generates a key for a shift cipher
    # Random integer from 0 to 88
    return np.random.randint(89)

def shift_encrypt(message,key):
    # 'message': list of integers. 'key': single integer
    # Generates a key taking on values from 0 to 88
    # Outputs a tuple of list of encrypted integers and the key (for convenience)
    return (list(map(lambda x: (x + key) % 89, message)),key)

def shift_decrypt(message, key):
    # Takes a list of integers as input
    # Decrypts ciphertext back to plaintext
    return list(map(lambda x: (x - key) % 89, message))

# Vigenere Cipher
def vigenere_key_gen(key_length):
    # 'key_length': length of array generated
    # Generates a key for a vigenere cipher
    # Array of random integers from 0 to 88
    return np.random.randint(0,89,key_length)

def vigenere_encrypt(message,key):
    # 'message': list of intgers 0 to 88. 'key': list of integers 0 to 88.
    # Takes a list of integers as input
    # Generates a key taking on values from 0 to 88
    # Outputs a tuple of list of encrypted integers and the key (for convenience)
    return (list([int((message[i] + key[i%len(key)]) % 89) for i,v in enumerate(message)]),key)

def vigenere_decrypt(message,key):
    # 'message': list of intgers 0 to 88. 'key': list of integers 0 to 88.
    # Takes a list of integers as input
    # Generates a key taking on values from 0 to 88
    # Outputs a list of integers which is the decryption.
    return list([int((message[i] - key[i%len(key)]) % 89) for i,v in enumerate(message)])


def encrypt(message, algo):
    pass
