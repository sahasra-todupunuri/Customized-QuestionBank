import random
import json
import math
from math import gcd

q_json_file = open("START.json", "w")

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def get_ckt_values():
    s1 = rr(10, 20, 1)
    s2 = rr(20, 30, 1)
    s3 = rr(40, 50, 1)
    s4 = rr(25, 30, 1)
    s5 = rr(70, 80, 1)
    s6 = rr(80, 90, 1)

    t1 = rr(8, 15, 1)
    t2 = rr(18, 25, 1)
    t3 = rr(18, 25, 1)
    t4 = rr(40, 50, 1)
    t5 = rr(45, 50, 1)
    t6 = rr(80, 90, 1)

    f1 = rr(2, 10, 1)
    f2 = rr(8, 15, 1)
    f3 = rr(10, 20, 1)
    f4 = rr(20, 30, 1)
    f5 = rr(30, 40, 1)
    f6 = rr(40, 50, 1)

    return [s1, s2, s3, s4, s5, s6, t1, t2, t3, t4, t5, t6, f1, f2, f3, f4, f5, f6]

q_json = {}
q_json["values"] = []
parameters = ["s1", "s2", "s3", "s4", "s5", "s6", "t1", "t2", "t3", "t4", "t5", "t6", "f1", "f2", "f3", "f4", "f5", "f6",  
              "q1cc", "q1wc1", "q1wc2", "q1wc3",
              "q2cc", "q2wc1", "q2wc2", "q2wc3",
              "q3cc", "q3wc1", "q3wc2", "q3wc3",
              "q4cc", "q4wc1", "q4wc2", "q4wc3",
              "q5cc", "q5wc1", "q5wc2", "q5wc3"]

for x in range(10):
    [s1, s2, s3, s4, s5, s6, t1, t2, t3, t4, t5, t6, f1, f2, f3, f4, f5, f6] = get_ckt_values()
    
    ans1 = (1000*(f1 + f2 + f3 + f4 + f5 + f6))/6
    ans1w1 = (1000*(f1 + f2 + f3))/3
    ans1w2 = (1000*(s1 + s2 + s3))/3

    ans2 = (f5/s2)*100
    ans2w1 = (f4/s2)*100
    ans2w2 = (s4/s2)*100

    ans3 = (1000*t6)*(7/10)
    ans3w1 = (1000*t3)*(7/10)
    ans3w2 = (1000*t4)*(7/10)

    # Define the ratios and their simplified forms
    ratios = [(t1, s5), (s2, s5), (s5, t1), (t1, t4)]
    simplified_ratios = [(num // gcd(num, den), den // gcd(num, den)) for num, den in ratios]
    # Formatting the answers as requested
    ans4, ans4w1, ans4w2, ans4w3 = [f"{num} : {den}" for num, den in simplified_ratios]

    google = (s1 + s2 + s3 + s4 + s5 + s6)*1000
    microsoft = (t1 + t2 + t3 + t4 + t5 + t6)*1000
    oracle = (f1 + f2 + f3 + f4 + f5 + f6)*1000
    totalEmployees = google + microsoft + oracle

    ans5 = (microsoft/totalEmployees)*360
    ans5w1 = (google/totalEmployees)*360
    ans5w2 = (oracle/totalEmployees)*360
    ans5w3 = (microsoft/(google + oracle))*360

    q1cc = f'{ans1:,.0f}'
    q1wc1 = f'{ans1 + 20:,.0f}'
    q1wc2 = f'{ans1w1:,.0f}'
    q1wc3 = f'{ans1w2:,.0f}'

    q2cc = f'{ans2:,.2f}\%'
    q2wc1 = f'{ans2 + 2:,.2f}\%'
    q2wc2 = f'{ans2w1:,.2f}\%'
    q2wc3 = f'{ans2w2:,.2f}\%'

    q3cc = f'{ans3:,.0f}'
    q3wc1 = f'{ans3 + 1000:,.0f}'
    q3wc2 = f'{ans3w1:,.0f}'
    q3wc3 = f'{ans3w2:,.0f}'

    q4cc = ans4
    q4wc1 = ans4w1
    q4wc2 = ans4w2
    q4wc3 = ans4w3

    q5cc = f'{ans5:,.1f}$^\circ$'
    q5wc1 = f'{ans5w1:,.1f}$^\circ$'
    q5wc2 = f'{ans5w2:,.1f}$^\circ$'
    q5wc3 = f'{ans5w3:,.1f}$^\circ$'

    q_json["values"].append([s1, s2, s3, s4, s5, s6, t1, t2, t3, t4, t5, t6, f1, f2, f3, f4, f5, f6, 
                            q1cc, q1wc1, q1wc2, q1wc3,
                            q2cc, q2wc1, q2wc2, q2wc3, 
                            q3cc, q3wc1, q3wc2, q3wc3, 
                            q4cc, q4wc1, q4wc2, q4wc3, 
                            q5cc, q5wc1, q5wc2, q5wc3])

q_json["parameters"] = parameters

json.dump(q_json, q_json_file)
q_json_file.close()
