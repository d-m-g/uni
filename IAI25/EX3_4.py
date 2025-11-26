import numpy as np

p_earthquake = 1 / 111
p_bulglary = 1 / 365
p_earthquake_alarm = 0.81
p_bulglary_alarm = 0.92
p_earthquake_and_bulglary_alarm = 0.97
false_alarm = 0.0095

choice = [0, 1]
E = [1 - p_earthquake, p_earthquake]
B = [1 - p_bulglary, p_bulglary]
A = [[1 - false_alarm, false_alarm], 
     [1 - p_bulglary_alarm, p_bulglary_alarm], 
     [1 - p_earthquake_alarm, p_earthquake_alarm], 
     [1 - p_earthquake_and_bulglary_alarm, p_earthquake_and_bulglary_alarm]]


n = 100000

def generate_data(E, B, A, n, choice):
    data = []
    for i in range(n):
        b = np.random.choice(choice, p=B)
        e = np.random.choice(choice, p=E)
        a = np.random.choice(choice, p=A[b + 2 * e])
        data.append((b, e, a))
    return data

data = generate_data(E, B, A, n, choice)

def find_p(data, goal, b=None, e=None, a=None):
    cnt_0 = 0
    cnt_1 = 0
    for d in data:
        if b is not None and d[0] != b:
            continue
        if e is not None and d[1] != e:
            continue
        if a is not None and d[2] != a:
            continue
        if goal == "b":
            if d[0] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1
        elif goal == "e":
            if d[1] == 0:
                cnt_0 += 1
            else:
                cnt_1 += 1

    return cnt_1 / (cnt_0 + cnt_1)

print(find_p(data, "b", a=1)) # burglary when alarm is given
print(find_p(data, "b", a=1, e=1)) # burglary when alarm is given and earthquake is given