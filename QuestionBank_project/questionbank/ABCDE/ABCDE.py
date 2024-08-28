import random
import json

q_json_file = open("ABCDE.json", "w")

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def f2s(no, d):
    s1 = "{z:0." + str(d) + "f}"
    return s1.format(z=no)

def get_ckt_values():
    s1 = rr(7, 10, 1)
    s2 = rr(2, 5, 1)
    return [s1, s2]

q_json = {}
q_json["values"] = []
parameters = ["s1", "s2", "q1cc", "q1wc1", "q1wc2", "q1wc3"]

for x in range(10):
    [s1, s2] = get_ckt_values()
    P = (s1 ** 2) / s2
    
    q1cc = f'{P:0.3f}'
    q1wc1 = f'{P + 1:0.3f}'
    q1wc2 = f'{P - 1:0.3f}'
    q1wc3 = f'{P - 2:0.3f}'

    q_json["values"].append([s1, s2, q1cc, q1wc1, q1wc2, q1wc3])

q_json["parameters"] = parameters

json.dump(q_json, q_json_file)
q_json_file.close()
