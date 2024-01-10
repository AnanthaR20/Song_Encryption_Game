from helper_fns_encryption_and_music import *

# ----- Step 0: Explanation
print("""\nWelcome to the Song-ified version of the cryptographic indistinguishability experiment!
In a standard challenge-response distinguishability game, the adversary chooses two messages from the message space. 
One of them is encrypted at random and presented to the adversary. 
If the *best* ANY adversary can do is guess as to which message was encrypted, then the encryption scheme fits the definition of perfect security. 
However, encrypting a song need not be perfectly secure to leave a human with only guessing-odds. 
\nInstructions:
1. You will be presented with a list of songs.
2. Choose 2 songs from the list.
3. We will play both songs normally at first.
4. Afterwards, you will HEAR an encryption of ONE of your songs at random.
\n  ***Your goal is to guess which of your 2 songs was encrypted! Can you crack this musical cipher?***
""")
difficulty = int(input("First, choose a difficulty level from 1 (easy) to 4 (hard): "))

# ----- Step 1: Attacker selects 2 plaintexts from the message space ("8_bar_melodies")
print("\n+++++ Song List +++++")
[print(str(i+1)+") "+v[:-4]) for i,v in enumerate(m_space)] # m_space = os.listdir("8_bar_melodies")
in_1 = int(input("\nChoose your first song from the list above. Type a number: ")) -1
print("--> Song 1: " + m_space[in_1][:-4])
while(True):
    in_2 = int(input("Choose a second song. Type a number: ")) -1
    if in_2 == in_1:
        print("Cannot choose the same song!\n")
        continue
    else:
        print("--> Song 2: " + m_space[in_2][:-4])
        break
files = ["songs/"+m_space[in_1], "songs/"+m_space[in_2]]
m = [file_to_plaintext(files[0]), file_to_plaintext(files[1])]
# Play each plaintext out loud to initialize the listener.
while(True):
    print("-----------------------------------------------------")
    input("-Press Enter to hear '" + files[0][6:-4] + "' NORMALLY")
    print("--> Playing song #1... " + files[0][6:-4])
    fs.play_Track(message_to_Track(m[0]),1,300)
    input("\n-Press Enter to hear '" + files[1][6:-4] + "' NORMALLY")
    print("--> Playing song #2... " + files[1][6:-4])
    fs.play_Track(message_to_Track(m[1]),1,300)
    y_n = input("\nWould you like to hear your songs again? 'y' or 'n': ")
    if y_n == 'y':
        continue
    else:
        break

# ----- Step 2: Encrypt one plaintext randomly and play for the listener
key = vigenere_key_gen(difficulty)
c = [vigenere_encrypt(m[0],key)[0], vigenere_encrypt(m[1],key)[0]]
b = np.random.randint(2)
# Present the encryption to the Attacker
while(True):
    print("-----------------------------------------------------")
    input("-Press Enter to hear the encrypted song.")
    print("--> Playing the encrypted song... ???")
    fs.play_Track(message_to_Track(c[b]),1,300)
    y_n = input("\nWould you like to hear the encrypted song again? 'y' or 'n': ")
    if y_n == 'y':
        continue
    else:
        break

# ----- Step 3: Attacker Play selected encrypted message
# See if Attacker/Adversary has better than chance odds of guessing original plaintext
# If attacker guesses plaintext
print("-----------------------------------------------------")
guess = input("\nWhich of your songs was encrypted?\n1." + files[0][6:-4] + "  -or-  2." + files[1][6:-4] + "\n")
print("\nResults:")
print("Correct" if int(guess)-1 == b else "Incorrect")
print("\n--> Playing DECRYPTED song... " + files[b][6:-4])
fs.play_Track(message_to_Track(vigenere_decrypt(c[b],key)),1,300)
