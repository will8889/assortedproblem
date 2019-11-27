def makeForms(verb):
    suffixes = ['o','ch','s','sh','x','z']
    if verb[-1] == 'y':
        return verb[:-1] + 'ies'
    elif verb[-1] in  suffixes or verb[-2:] in suffixes:
        return verb + 'es'
    else:
        return verb + 's'
        
print(makeForms("try"))