
import random as rm
import numpy as np
import matplotlib.pyplot as plt


moves = {0: [0,1], 1: [0, -1], 2: [-1, 0], 3: [1, 0]}

X = 0
Y = 0
prev_moves = [[[X, Y], [5, 5, 5, 5]]]

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

def check_move(u, v):
    for pm in prev_moves:
        if pm[0] == [u, v]:
            wts = pm[1]
            idx = prev_moves.index(pm)
            break
        else:
            wts = [5, 5, 5, 5]
            idx = 'False'
    return wts, idx

def get_sequence(a, b, whts):
    move = rm.choices([0, 1, 2, 3], weights=whts)[0]
    x_move = moves[move][0] + a
    y_move = moves[move][1] + b
    return np.linspace(a, x_move, num=10), np.linspace(b, y_move, num=10), move

def update_move_good(m, n, idx, mv):
    if idx == 'False':
        prev_moves.append([[m, n], [5, 5, 5, 5]])
        prev_moves[-1][1][mv] += 1
    else:
        prev_moves[idx][1][mv] += 1

def update_move_bad(m, n, idx, mv):
    if idx == 'False':
        prev_moves.append([[m, n], [5, 5, 5, 5]])
        prev_moves[-1][1][mv] -= 5
    else:
        prev_moves[idx][1][mv] -= 5

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
        wts, idx = check_move(u=x, v=y)
        x_seq, y_seq, mv = get_sequence(a=x, b=y, whts=wts)
        for j in range(len(x_seq)):
            ax.plot(x_seq[j], y_seq[j], 'ro')
            plt.draw()
            plt.pause(.01)
        for p in range(len(x_seq) - 1):
            plt.cla()
            ax.set_xlim(-grd_sz, grd_sz)
            ax.set_ylim(-grd_sz, grd_sz)
            ax.grid('on')
            ax.plot(x_seq[p + 1:], y_seq[p + 1:], 'ro')
            plt.draw()
            plt.pause(0.01)
        xold = int(x)
        yold = int(y)
        x = int(x_seq[-1])
        y = int(y_seq[-1])
        ck = check_limits(u=x, v=y)
        if ck == 'break':
            print('CRASH')
            update_move_bad(m=xold, n=yold, idx=idx, mv=mv)
            break
        else:
            update_move_good(m=xold, n=yold, idx=idx, mv=mv)
    if ck != 'break':
        print('SURVIVE')


lp = 10
print(prev_moves)
for i in range(50):
    animate(loop=lp, x=X, y=Y)
print(prev_moves)

plt.show()



