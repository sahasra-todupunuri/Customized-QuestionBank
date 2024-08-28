import random
import json
import math

q_json_file = open("TABLE.json", "w")

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def get_ckt_values():
    c1=rr(10,20,1)
    c2=rr(10,20,1)
    m1=rr(5,10,1)
    m2=rr(8,12,1)
    l1=rr(18,28,1)
    l2=rr(20,30,1)
    s1=rr(6,9,1)
    s2=rr(6,9,1)
    d1=rr(30,40,2)
    d2=rr(40,50,2)
    Va=rr(4000,5000,28)
    rw=rr(128,226,16)
    rc=rr(250,358,10)
    return [c1, c2, m1, m2, l1, l2, s1, s2, d1, d2, Va, rw, rc]

q_json = {}
q_json["values"] = []
parameters = ["c1", "c2", "m1", "m2", "l1", "l2", "s1", "s2", "d1", "d2", "Va", "rw", "rc", 
              "q1cc", "q1wc1", "q1wc2", "q1wc3",
              "q2cc", "q2wc1", "q2wc2", "q2wc3",
              "q3cc", "q3wc1", "q3wc2", "q3wc3",
              "q4cc", "q4wc1", "q4wc2", "q4wc3",
              "q5cc", "q5wc1", "q5wc2", "q5wc3"]

for x in range(10):
    [c1, c2, m1, m2, l1, l2, s1, s2, d1, d2, Va, rw, rc] = get_ckt_values()
    x = 2 * (c1 * c2) + 2 * (m1 * m2) + 2 * (d1 * d2)
    x1 = (2*rw)*((l1 * l2) + (s1 * s2))
    x2 = (c1 * c2) - (m1 * m2)
    x3 = x * rc + x1
    x4 = ((c1 * c2) / Va) * 100

    q1cc = f'{x}'
    q1wc1 = f'{x - 2}'
    q1wc2 = f'{x + 3}'
    q1wc3 = f'{x//2}'

    q2cc = f'{x1}'
    q2wc1 = f'{x1 - 2}'
    q2wc2 = f'{x1//3}'
    q2wc3 = f'{x1//2}'

    q3cc = f'{x2}'
    q3wc1 = f'{x2 - 2}'
    q3wc2 = f'{x2//3}'
    q3wc3 = f'{x2//2}'

    q4cc = f'{x3}'
    q4wc1 = f'{x3 - 2}'
    q4wc2 = f'{x3//3}'
    q4wc3 = f'{x3//2}'

    q5cc = f'{x4:.2f}\%'
    q5wc1 = f'{x4 - 2:.2f}\%'
    q5wc2 = f'{x4 + 3:.2f}\%'
    q5wc3 = f'{x4 + 2:.2f}\%'


    q_json["values"].append([c1, c2, m1, m2, l1, l2, s1, s2, d1, d2, Va, rw, rc, 
                            q1cc, q1wc1, q1wc2, q1wc3,
                            q2cc, q2wc1, q2wc2, q2wc3, 
                            q3cc, q3wc1, q3wc2, q3wc3, 
                            q4cc, q4wc1, q4wc2, q4wc3, 
                            q5cc, q5wc1, q5wc2, q5wc3])

q_json["parameters"] = parameters

json.dump(q_json, q_json_file)
q_json_file.close()
