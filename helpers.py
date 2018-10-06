def alphabet_position(someChar):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position=0
    newChar=someChar.lower()
    position=alphabet.find(newChar)
    
    return(position)

def giveNewChar(someChar, x):  #The only real purpose of this function is to maintain Uppers vs. Lowers.
    alphabetLOWER = 'abcdefghijklmnopqrstuvwxyz'
    alphabetUPPER = alphabetLOWER.upper()

    if (alphabetLOWER.find(someChar)!=-1):
        newChar=alphabetLOWER[x]
    else:
        if (alphabetUPPER.find(someChar)!=-1):
            newChar=alphabetUPPER[x]
        else:
            newChar=someChar
    
    return(newChar)


def rotate_character(rotChar, x):

    rotatedChar = ''
    charAlphaIndex = alphabet_position(rotChar)
    
    if (charAlphaIndex<0):
        rotatedChar= rotChar
    else:
        charAlphaIndex = charAlphaIndex + x
        rotatedChar = giveNewChar(rotChar,charAlphaIndex % 26)
        
    return rotatedChar