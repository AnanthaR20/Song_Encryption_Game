from helper_fns_encryption_and_music import *

play_again = True

while(play_again):
    print("\n\n\n+++++ Song List +++++")
    # ----- Step 1: Attacker selects 2 plaintexts from the message space ("songs")
    [print(str(i+1)+") "+v[:-4]) for i,v in enumerate(m_space)] # m_space = os.listdir("songs")

    in_1 = int(input("Choose a song to play from the list above. Type a number: ")) -1
    while(True):
        if type(in_1) != int :
            print("Must be number!\n")
        elif in_1 > len(m_space) or in_1 <= 0:
            print("Input a valid range!\n")
        else:
            break
        in_1 = int(input("Choose a song to play from the list above. Type a number: ")) -1

    # Convert to message and play
    tempo = int(input("Choose a bpm/tempo!"))
    m = file_to_plaintext("songs/"+m_space[in_1])
    print("\n--> Playing... " + m_space[in_1][:-4])
    fs.play_Track(message_to_Track(m),1,tempo)

    again = input("Would you like to play another song? 'y' or 'n' ")
    play_again = True if again == 'y' else False



