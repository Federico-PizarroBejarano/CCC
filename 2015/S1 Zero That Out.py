numbers = []

for i in range(int(raw_input())):
    num = int(raw_input())
    if num != 0:
        numbers.append(num)
    else:
        del numbers[-1]
print sum(numbers)
