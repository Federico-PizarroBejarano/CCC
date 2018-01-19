n = int(input());
k = int(input());

count = 1

maths = [n//k]*(k-1) + [n - (n//k)*(k-1)]

def pi(min_slice, maths):
    if len(maths) == 1:
        return maths
    elif maths[0] == min_slice:
        pi(min_slice, maths[:-1])
    
    