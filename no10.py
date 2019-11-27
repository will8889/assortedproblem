import string
def check_pangram(str):
    alphabet = set(string.ascii_lowercase)
    valid = set(str.lower().replace(" ",""))
    if sorted(valid) == sorted(alphabet):
        return True
    return False
    
print(check_pangram("The quick brown fox jumps over the lazy dog"))