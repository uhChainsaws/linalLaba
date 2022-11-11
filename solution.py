from math import factorial, pi, sin, sqrt, acos

VH = 20
VW = 119
DX = 1
OFFSET = 6000
DM = 0.004
HUGENUM = 133337
labaTZ_MODE = True
def f(x):
    try:
        return (1+sin(x*pi/2))*((x-3)/(x+5))
        # return ((x/(x+1))*(2+((-1)**x)))
        # return ((5*x-7)/(3*x-2))*acos((1+(-1)**x)*pi/6)
        # return (2**(4*x-3)+2*(x**2)*(factorial(x-2)))/(factorial(x)-16**(2*x))
        # return ((1-x**3)/(x-x**3))**(-x**3)
        # return (x)
        # return sqrt(x)
    except:
        return 0
X = range(OFFSET, VW-1+OFFSET)
Y = [f(x*DX) for x in X]
# print(Y) # DEBUG
DY = max(abs(max(Y)), abs(min(Y)))*1.01
farSample = [f(x) for x in range(HUGENUM, HUGENUM+12)]
susLims = set()
for y in Y:
    susLims.add(round(y, 2))
realLims = susLims.copy()
for lim in susLims:
    areFar = [abs(y-lim)>DM for y in farSample]
    if all(areFar):
        realLims.remove(lim)
if DY == 0:
    DY = 1.0
screen = [[' ' for i in range(VW)] for j in range(VH)]
for i in range(VH):
    screen[i][0] = '|'
for i in range(VW):
    screen[VH//2][i] = '-'
screen[VH//2][0] = '+'
screen[0][0] = '^'
screen[VH//2][VW-1] = '>'
for i in range(len(X)):
    y = Y[i]/DY
    if y == -1:
        y = -0.99
    # y is (-1, 1]
    j = int(y*VH)
    screen[(VH-j)//2][i] = '*'
for lim in realLims:
    label = f"[{lim}]"
    screenY = int(lim / DY * VH)
    for i in range(len(label)):
        screen[(VH - screenY)//2][i+1] = label[i]
print("\nso, here is what we have...\n(1+sin(x*pi/2))*((x-3)/(x+5))\njust let me think now...")
print("\n"+("#"*VW)+"\n")
print(f"[{float(DY):.4}]")
for i in range(VH):
    for j in range(VW):
        if screen[i][j] == '-':
            print('-', end='')
        else:
            print(screen[i][j], end='')
    print()
print(f"\nnotation:\nΔY = {((DY*2)/VH):.4}, ΔX = {DX}, graph depicts range of [{OFFSET} -- {OFFSET+VW-1}] on the X axis, [{-DY:.4} -- {DY:.4}] on the Y axis")
print("\n"+("#"*VW)+"\n")
if len(realLims) == 0:
    print("wow, it seems the sequence is somewhat unbounded, but dont take my word on this(!)")
else:
    print(f"hmm, i think i have found some cool limits(!):\n{realLims}")
if labaTZ_MODE:
    for lim in realLims:
        n = 1
        while abs(lim - f(n))>DM:
            n+=1
        n+=1
        print(f"for limit {lim} the n_0 is {n}")
        n = 1
        while abs(lim - DM)>f(n):
            n+=1;
        print(f"for limit {lim} the m is {n}")