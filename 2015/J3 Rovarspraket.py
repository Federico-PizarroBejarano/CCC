vowels = ("a", "e", "i", "o", "u")
alph = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
word = list(raw_input())

for i in range(len(word)):
    if word[i] not in vowels:
        new = word[i]
        for j in xrange(26):
            if alph[alph.index(word[i])+j] == "z":
                rt = 26
                break
            elif alph[alph.index(word[i])+j] in vowels:
                rt = j
                break
        for j in xrange(26):
            if alph[alph.index(word[i])-j] in vowels:
                lt = j
                break
        if lt > rt:
            new += alph[alph.index(word[i]) + rt]
        else:
            new += alph[alph.index(word[i]) - lt]

        if word[i] == "z":
            new += "z"
        else:
            for j in xrange(26):
                if alph[alph.index(word[i])+j+1] not in vowels:
                    new += alph[alph.index(word[i])+j+1]
                    break
        word[i] = new
print "".join(word)
            
                         
            
        
