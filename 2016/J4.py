hr, mi = map(int, raw_input().split(":"))
if 7<=(hr + mi/60.0) <10 or  7<(hr +2 + mi/60.0) <=10:
    ft = 0
    if (hr + mi/60.0) < 7:
        ft = 7*60 - hr*60 - mi
        hr = 7
        mi = 0
    if ft + 90 > 120:
        hr = 7 + ((120-ft)*2)/60
        mi = ((120-ft)*2)%60
        print "0"*(2-len(str(hr))) + str(hr) + ":" + "0"*(2-len(str(mi))) + str(mi)
    elif ft + 90 < 120:
        hrn = 10 + (120-ft-(10*30 - hr*30 - mi/2))/60
        mi = (120-ft-(10*30 - hr*30 - mi/2))%60
        hr = hrn
        print "0"*(2-len(str(hr))) + str(hr) + ":" + "0"*(2-len(str(mi))) + str(mi)
    else:
        print "10:00"
elif 15<=(hr + mi/60.0) <19 or 15<(hr + mi/60.0 +2) <=19:
    ft = 0
    if (hr + mi/60.0) < 15:
        ft = 15*60 - hr*60 - mi
        hr = 15
        mi = 0
    if ft + 90 > 120:
        hr = 15 + ((120-ft)*2)/60
        mi = ((120-ft)*2)%60
        print "0"*(2-len(str(hr))) + str(hr) + ":" + "0"*(2-len(str(mi))) + str(mi)
    elif ft + 90 < 120:
        hrn = 19 + (120-ft-(19*30 - hr*30 - mi/2))/60
        mi = (120-ft-(19*30 - hr*30 - mi/2))%60
        hr = hrn
        print "0"*(2-len(str(hr))) + str(hr) + ":" + "0"*(2-len(str(mi))) + str(mi)
    else:
        print "19:00"
else:
    hr = (hr+2)%24
    print "0"*(2-len(str(hr))) + str(hr) + ":" + "0"*(2-len(str(mi))) + str(mi)
