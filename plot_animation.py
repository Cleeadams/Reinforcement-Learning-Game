
import matplotlib.pyplot as plt
import random as rm
import numpy as np

X = 0
Y = 0
grd_sz = 2
bounds = []
for i in [-grd_sz, grd_sz]:
    for j in range(grd_sz*2+1):
        bounds.append([i, -grd_sz+j])
        bounds.append([-grd_sz + j, i])

fig, ax = plt.subplots()
ax.set_xlim(-grd_sz, grd_sz)
ax.set_ylim(-grd_sz, grd_sz)
ax.grid('on')
lp = 7
rf = []
wts = [5, 5, 5, 5]
for p in range(lp):
    rf.append(wts.copy())


def get_sequence(a, b, it):
    moves = {0: [0,1], 1: [0,-1], 2: [-1,0], 3: [1,0]}
    move = rm.choices([0, 1, 2, 3], weights=rf[it])[0]
    x_move = moves[move][0] + a
    y_move = moves[move][1] + b
    return np.linspace(a, x_move, num=10), np.linspace(b, y_move, num=10), move

def check_limits(u, v):
    for bd in bounds:
        if bd == [u, v]:
            ck_lm = 'break'
            break
        else:
            ck_lm = 'continue'
    return ck_lm

def animate(loop=1, x=None, y=None):
    for i in range(loop):
        x_seq, y_seq, mv = get_sequence(a=x, b=y, it=i)
        for j in range(len(x_seq)):
            ax.plot(x_seq[j], y_seq[j], 'ro')
            plt.draw()
            plt.pause(.03)
        for p in range(len(x_seq)-1):
            plt.cla()
            ax.set_xlim(-grd_sz, grd_sz)
            ax.set_ylim(-grd_sz, grd_sz)
            ax.grid('on')
            ax.plot(x_seq[p+1:], y_seq[p+1:], 'ro')
            plt.draw()
            plt.pause(0.03)
        x = x_seq[-1]
        y = y_seq[-1]
        ck = check_limits(u=x, v=y)
        if ck == 'break':
            print('CRASH')
            rf[i][mv] -= 1
            break
        else:
            rf[i][mv] += 3
    if ck != 'break':
        print('SURVIVE')

print(rf)
for i in range(1):
    animate(loop=lp, x=X, y=Y)
print(rf)
plt.show()

