def char_freq(string):
    list = {}
    for c in string:
        if c in list:
            list[c] = list[c] + 1
        else:
            list[c] = 1
    for char_item, freq in list.items():
        print(char_item + ": " + str(freq))

char_freq("hello")