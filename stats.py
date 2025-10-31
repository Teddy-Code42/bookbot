def word_count(text):
    words = text.split()
    wordcounting = len(words)
    return wordcounting

def char_count(text):
    charactercount = {}
    chlower = text.lower()
    for ch in chlower:
        if ch in charactercount:
            charactercount[ch] += 1
        else:
            charactercount[ch] = 1
    return charactercount

def sort_on_list(charactercount):
    prettylist = []
    for ch in charactercount:
        prettycount = {}
        num = charactercount[ch]
        prettycount["char"] = ch
        prettycount["num"] = num
        prettylist.append(prettycount)
    return prettylist

def sort_on(prettylist):
    return prettylist["num"]
    
def prettiestlist(prettylist):
    return prettylist.sort(reverse=True, key=sort_on)