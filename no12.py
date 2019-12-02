import string
def caeser_cipher(text:str,n):
    alphabet = string.ascii_lowercase
    new_word = ""
    for x in text:
        next = alphabet.find(x) + n
        if next >= 25:
            next = next-25
        new_letter = alphabet[next]
        new_word = new_word +new_letter
    return new_word

print(caeser_cipher('hello',13))
