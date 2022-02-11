pattrn = "abba"
stringy = "cat dog dog cat" # true



pattrn = "vvvbssds"
stringy = "dog dog dog cat fish fish lion fish"



import collections
def find_word_pattern(patt, strr):
    g = strr.split(" ")
    char_to_word = {}
    word_to_char = {}
    ss = zip(patt, g)
    print(list(ss))
    for c, w in zip(patt, g):
        
        if c in char_to_word and char_to_word[c] != w:
            return False
        if w in word_to_char and word_to_char[w] != c:
            return False
        char_to_word[c] = w
        word_to_char[w] = c
    print(char_to_word)
    print(word_to_char)


for i in range(10):
    print(i)
    
find_word_pattern(pattrn, stringy)
