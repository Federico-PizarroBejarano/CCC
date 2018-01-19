friends = []
distance = []
sums = []
time = 0
end = []
for i in xrange(int(raw_input())):
    line = raw_input()
    if line[0] == "R":
        if line[2:] not in friends:
            friends.append(line[2:])
            distance.append(time)
            sums.append(0)
        else:
            distance[friends.index(line[2:])] = time
        time += 1
    elif line[0] == "S":
        sums[friends.index(line[2:])] += time - distance[friends.index(line[2:])]
        distance[friends.index(line[2:])] = -1
        time += 1
    else:
        time += int(line[2:]) - 1

for i in xrange(len(distance)):
    if distance[i] != -1:
        sums[i] = -1

for j in xrange(len(friends)):
    i = friends.index(min(friends))
    end.append("{} {}".format(friends[i], sums[i]))
    del friends[i]
    del sums[i]

for i in end:
    print i
               
                   
