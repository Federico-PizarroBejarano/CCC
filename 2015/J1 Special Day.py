month = int(raw_input())
day = int(raw_input())
if month == 1:
    print "Before"
elif month > 2:
    print "After"
else:
    if day < 18:
        print "Before"
    elif day > 18:
        print "After"
    else:
        print "Special"
