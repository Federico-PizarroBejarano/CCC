line = raw_input()
hap = line.count(":-)")
sad = line.count(":-(")
if hap == 0 and sad == 0:
    print "none"
elif hap == sad:
    print "unsure"
elif hap > sad:
    print "happy"
elif sad > hap:
    print "sad"
