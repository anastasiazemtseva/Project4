# The program encrypts words in two ways: Caesar’s cipher and random
# predefined signs.
import string

language = str(input('Выберите язык: / Choose language: '))
if language.lower() == 'русский':
    import local_rus as lc
elif language.lower() == 'english':
    import local_eng as lc


type = input(lc.TXT_ENCRYPT_A_WORD)
print()

# The first method of encryption is to banally replace the letter
# of the entered word with a random, pre-registered character.
if type == '+':
    word = input(lc.TXT_WORD)
    cipher = ''

    # Cycle to replace letters in a new line chipher.
    for i in range(len(word)):
        if word[i] == 'a':
            cipher += str('✈')
        elif word[i] == 'b':
            cipher += str('🚌')
        elif word[i] == 'c':
            cipher += str('🚴')
        elif word[i] == 'd':
            cipher += str('👱')
        elif word[i] == 'e':
            cipher += str('🎇')
        elif word[i] == 'f':
            cipher += str('🌎')
        elif word[i] == 'g':
            cipher += str('🎠')
        elif word[i] == 'h':
            cipher += str('🎀')
        elif word[i] == 'i':
            cipher += str('❤')
        elif word[i] == 'j':
            cipher += str('💌')
        elif word[i] == 'k':
            cipher += str('🚝')
        elif word[i] == 'l':
            cipher += str('🌋')
        elif word[i] == 'm':
            cipher += str('🏯')
        elif word[i] == 'n':
            cipher += str('🏨')
        elif word[i] == 'o':
            cipher += str('💳')
        elif word[i] == 'p':
            cipher += str('⚓')
        elif word[i] == 'q':
            cipher += str('💰')
        elif word[i] == 'r':
            cipher += str('📊')
        elif word[i] == 's':
            cipher += str('🎅')
        elif word[i] == 't':
            cipher += str('💍')
        elif word[i] == 'u':
            cipher += str('Ⓜ')
        elif word[i] == 'v':
            cipher += str('⚠')
        elif word[i] == 'w':
            cipher += str('💯')
        elif word[i] == 'x':
            cipher += str('🌙')
        elif word[i] == 'y':
            cipher += str('✔')
        elif word[i] == 'z':
            cipher += str('🔅')

    print(lc.TXT_ENCRYPT_WORD, cipher)

# Caesar Cipher with a shift of 3.
# Caesar’s cipher is a type of substitution cipher in which each character
# in plaintext is replaced by a character located at a certain constant
# number of positions to the left or right of it in the alphabet.
elif type == '-':
    answer = input(lc.TXT_ENCRYPT_OR_DECRYPT)
    print()

    if answer == '+':
        word = str(input(lc.TXT_WORD))
        encrypted_word = ''
        # Create a line of letters and numbers.
        alphabet_numbers = string.ascii_lowercase + string.digits
        # Create a list of all letters
        # of the English alphabet and numbers from 1 to 9.
        alphabet_numbers = list(alphabet_numbers)

        for i in range(len(word)):
            for j in range(len(alphabet_numbers)):
                if word[i] == alphabet_numbers[j]:
                    encrypted_word += str(alphabet_numbers[j + 3])

        print(lc.TXT_ENCRYPT_WORD, encrypted_word)

    elif answer == '-':
        word = str(input(lc.TXT_WORD))
        encrypted_word = ''
        # Create a line of letters and numbers.
        alphabet_numbers = string.ascii_lowercase + string.digits
        # Create a list of all letters
        # of the English alphabet and numbers from 1 to 9.
        alphabet_numbers = list(alphabet_numbers)

        for i in range(len(word)):
            for j in range(len(alphabet_numbers)):
                if word[i] == alphabet_numbers[j]:
                    encrypted_word += str(alphabet_numbers[j - 3])

        print(lc.TXT_DECRYPT_WORD, encrypted_word)


