line = raw_input()

pal = ""

for i in range(len(line)):
    for j in range(i+1):
        #print line[j:len(line) - i+j], line[j:len(line) - i+j][::-1], i, j
        if line[j:len(line) - i+j] == line[j:len(line) - i+j][::-1] and len(pal) == 0:
            pal = line[j:len(line) - i+j]
        

print len(pal)
