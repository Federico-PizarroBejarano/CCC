n = input()
rice1 = map(int, raw_input().split())
b = True

while b:
    counter = 0
    for index in range(len(rice)-1):
        if index < len(rice)-2:
            if rice[index] == rice[index+2]:
                rice[index] = rice[index]*2 + rice[index+1]
                del rice[index+1]
                del rice[index+1]
                break
            elif rice[index] == rice[index+1]:
                rice[index] = rice[index]*2
                del rice[index+1]
                break
        elif rice[index] == rice[index+1]:
            rice[index] = rice[index]*2
            del rice[index+1]
            break
        else:
            counter += 1

        if counter == len(rice)-1:
            b = False
rice2 = rice
rice = rice1
while b:
    counter = 0
    for index in range(len(rice)-1):
        if rice[index] == rice[index+1]:
            rice[index] = rice[index]*2
            del rice[index+1]
            break
        elif index < len(rice)-2:
            if rice[index] == rice[index+2]:
                rice[index] = rice[index]*2 + rice[index+1]
                del rice[index+1]
                del rice[index+1]
                break
        else:
            counter += 1

        if counter == len(rice)-1:
            b = False

print max(max(rice), max(rice2))
