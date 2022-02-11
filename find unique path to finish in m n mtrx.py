mtrx = [3,7]

# start = [m[0],n[0]]
# finish = [m[i],n[j]] = [m[2],n[6]]

# [mtrx[0][0],mtrx[0][1],mtrx[0][2],mtrx[0][3],mtrx[0][4],mtrx[0][5],mtrx[0][6],mtrx[1][6],mtrx[2][6]]
# [mtrx[0][0],mtrx[0][1],mtrx[0][2],mtrx[0][3],mtrx[0][4],mtrx[0][5],mtrx[1][5],mtrx[2][5],mtrx[2][6]]

def path(matrixx):
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
