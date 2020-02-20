'''
Remove the garbage word from the string.
Replace one word and its sequence with a space, if the word occurs at the beginning or end of the line - just delete it.
'''

def song_decoder(song, garbage_word):
    return (" ".join((song.replace(garbage_word," ")).split())).strip()
