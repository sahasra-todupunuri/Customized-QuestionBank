import random
import json
import math

q_json_file = open("SAHAS.json", "w")

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def get_ckt_values():
    s1 = rr(20, 25, 1)
    s2 = rr(35, 40, 1)
    s3 = rr(35, 40, 1)
    s4 = rr(20, 25, 1)

    t1 = rr(15, 20, 1)
    t2 = rr(10, 15, 1)
    t3 = rr(30, 35, 1)
    t4 = rr(15, 20, 1)

    return [s1, s2, s3, s4, t1, t2, t3, t4]

q_json = {}
q_json["values"] = []
parameters = ["s1", "s2", "s3", "s4", "t1", "t2", "t3", "t4", 
              "q1cc", "q1wc1", "q1wc2", "q1wc3",
              "q2cc", "q2wc1", "q2wc2", "q2wc3",
              "q3cc", "q3wc1", "q3wc2", "q3wc3",
              "q4cc", "q4wc1", "q4wc2", "q4wc3",
              "q5cc", "q5wc1", "q5wc2", "q5wc3"]

for x in range(10):
    [s1, s2, s3, s4, t1, t2, t3, t4] = get_ckt_values()
    if (40*(s1 + s4 - t1 - t4) > 40*t3):
        ans1 = (40*(s1 + s4 - t1 - t4) - 40*t3) 
    else:
        ans1 = (-1)*(40*(s1 + s4 - t1 - t4) - 40*t3)

    if (110*t2 > 40*s3):
        ans2 = 110*t2 - 40*s3
    else:
        ans2 = (-1)*(110*t2 - 40*s3)

    ans3 = (40 / 3) * (t2 + t3 + t4)
    ans4 = (t1 + t3) / t2 if t2 != 0 else 0  # Added error handling
    ans5 = (14/3)*((s4 - t4)/t1)*100

    q1cc = f'{ans1:0.2f}'
    q1wc1 = f'{ans1 + 1:0.2f}'
    q1wc2 = f'{ans1 - 1:0.2f}'
    q1wc3 = f'{ans1 + 3:0.2f}'

    q2cc = f'{ans2:0.2f}'  
    q2wc1 = f'{ans2 + 1:0.2f}'
    q2wc2 = f'{ans2 - 1:0.2f}'
    q2wc3 = f'{ans2 + 3:0.2f}'

    q3cc = f'{ans3:0.2f}'
    q3wc1 = f'{ans3 + 1:0.2f}'
    q3wc2 = f'{ans3 - 1:0.2f}'
    q3wc3 = f'{ans3 + 3:0.2f}'

    q4cc = f'{ans4:0.2f}'
    q4wc1 = f'{ans4 + 1:0.2f}'
    q4wc2 = f'{ans4 - 1:0.2f}'
    q4wc3 = f'{ans4 + 3:0.2f}'

    q5cc = f'{ans5:0.2f}\%'
    q5wc1 = f'{ans5 + 1:0.2f}\%'
    q5wc2 = f'{ans5 - 1:0.2f}\%'
    q5wc3 = f'{ans5 + 3:0.2f}\%'

    q_json["values"].append([s1, s2, s3, s4, t1, t2, t3, t4, 
                            q1cc, q1wc1, q1wc2, q1wc3,
                            q2cc, q2wc1, q2wc2, q2wc3, 
                            q3cc, q3wc1, q3wc2, q3wc3, 
                            q4cc, q4wc1, q4wc2, q4wc3, 
                            q5cc, q5wc1, q5wc2, q5wc3])

q_json["parameters"] = parameters

json.dump(q_json, q_json_file)
q_json_file.close()
