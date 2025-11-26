import numpy as np
import random

B = [0.9, 0.1]
R = [[1.0, 0.0], [0.1, 0.9]]
I = [[1.0, 0.0], [0.05, 0.95]]
G = [0.95, 0.05]
S = [[1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [0.01, 0.99]]
M = [[1.0, 0.0], [0.01, 0.99]]
choice = [0, 1]

n = 10000000

def generate_data(B, R, I, G, S, M, n, choice):
    data = []
    for i in range(n):
        b = x = np.random.choice(choice, p=B)
        r = np.random.choice(choice, p=R[b])
        i = np.random.choice(choice, p=I[b])
        g = np.random.choice(choice, p=G)
        s = np.random.choice(choice, p=S[g + 2 * i])
        m = np.random.choice(choice, p=M[s])
        data.append((b, r, i, g, s, m))
    return data

data = generate_data(B, R, I, G, S, M, n, choice)

def find_p(data, goal, b=None, r=None, i=None, g=None, s=None, m=None):
    cnt_0 = 0
    cnt_1 = 0
    for d in data:
        if b is not None and d[0] != b:
            continue
        if r is not None and d[1] != r:
            continue
        if i is not None and d[2] != i:
            continue
        if g is not None and d[3] != g:
            continue
        if s is not None and d[4] != s:
            continue
        if m is not None and d[5] != m:
            continue
        if goal == "b":
            if d[0] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
        elif goal == "s":
            if d[4] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
    return cnt_1 / (cnt_0 + cnt_1)

print(find_p(data, "b", r=1, g=1, s=0)) # radio ok, gas ok, didn't start
print(find_p(data, "s", r=1, i=1, g=1)) # radio ok, gas ok, ignition ok
print(find_p(data, "s", r=0, i=1, g=1)) # radio wrong, gas ok, ignition ok

