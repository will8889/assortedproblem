def find_longest_word(words:list):
    longest_word:str = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            return longest_word
print(find_longest_word(["terbang", "tenggelam", "jatuh", "melayang"]))