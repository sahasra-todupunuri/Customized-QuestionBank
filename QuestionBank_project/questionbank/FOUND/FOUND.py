import random
import json
import math
from math import gcd

q_json_file = open("FOUND.json", "w")

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def get_ckt_values():
    s1 = rr(40, 50, 2)
    s2 = rr(40, 50, 2)
    s3 = rr(50, 60, 2)
    s4 = rr(70, 76, 2)

    t1 = rr(52, 60, 2)
    t2 = rr(50, 60, 2)
    t3 = rr(64, 74, 2)
    t4 = rr(80, 86, 2)

    f1 = rr(62, 70, 2)
    f2 = rr(62, 68, 2)
    f3 = rr(78, 86, 2)
    f4 = rr(90, 96, 2)

    return [s1, s2, s3, s4, t1, t2, t3, t4, f1, f2, f3, f4]

q_json = {}
q_json["values"] = []
parameters = ["s1", "s2", "s3", "s4", "t1", "t2", "t3", "t4", "f1", "f2", "f3", "f4",   
              "q1cc", "q1wc1", "q1wc2", "q1wc3",
              "q2cc", "q2wc1", "q2wc2", "q2wc3",
              "q3cc", "q3wc1", "q3wc2", "q3wc3",
              "q4cc", "q4wc1", "q4wc2", "q4wc3",
              "q5cc", "q5wc1", "q5wc2", "q5wc3"]

for x in range(10):
    [s1, s2, s3, s4, t1, t2, t3, t4, f1, f2, f3, f4] = get_ckt_values()
    
    ans1 = ((t2 - s2)/s2)*100
    ans1w1 = ((t3 - t1) /t1)*100
    ans1w2 = ((s3 - s1)/ s1)*100

    # Define the ratios and their simplified forms
    ratios = [((t2 + f4),s1), ((t2 + s4),s1), ((f4 + t3),f2), ((t4 + s1),f4)]
    simplified_ratios = [(num // gcd(num, den), den // gcd(num, den)) for num, den in ratios]
    # Formatting the answers as requested
    ans2, ans2w1, ans2w2, ans2w3 = [f"{num} : {den}" for num, den in simplified_ratios]

    # Data for the number of buildings in each city for 2010 and 2011
    data_2010 = {
        'Hyderabad': s1,
        'Chennai': s2,
        'Delhi': s3,
        'Mumbai': s4
    }

    data_2011 = {
        'Hyderabad': t1,
        'Chennai': t2,
        'Delhi': t3,
        'Mumbai': t4
    }

    # Calculate the percentage growth for each city from 2010 to 2011
    percentage_growth = {}
    for city in data_2010:
        growth = ((data_2011[city] - data_2010[city]) / data_2010[city]) * 100
        percentage_growth[city] = growth

    # Find the city with the maximum percentage growth
    max_growth_city = max(percentage_growth, key=percentage_growth.get)
    max_growth_percentage = percentage_growth[max_growth_city]

    # Store the city with the maximum percentage growth in a variable
    ans3 = max_growth_city

    # Store the other three cities in a list with variables
    other_cities = [city for city in data_2010 if city != max_growth_city]
    ans3w1, ans3w2, ans3w3 = other_cities

    avg_2011 = ((t1 + t2 + t3 + t4)*100000)/4
    avg_2012 = ((f1 + f2 + f3 + f4)*100000)/4
    if (avg_2011 > avg_2012):
        ans4 = avg_2011 - avg_2012
    else:
        ans4 = avg_2012 - avg_2011

    hyd = f1*100000
    che = f2*100000
    delh = f3*100000
    mum = f4*100000
    total = (f1 + f2 + f3 + f4)*100000

    ans5 = (hyd/total)*100
    ans5w1 = (che/total)*100
    ans5w2 = (delh/total)*100
    ans5w3 = (mum/total)*100

    q1cc = f'{ans1:,.2f}\%'
    q1wc1 = f'{ans1 + 2:,.2f}\%'
    q1wc2 = f'{ans1w1:,.2f}\%'
    q1wc3 = f'{ans1w2:,.2f}\%'

    q2cc = ans2
    q2wc1 = ans2w1
    q2wc2 = ans2w2
    q2wc3 = ans2w3

    q3cc = ans3
    q3wc1 = ans3w1
    q3wc2 = ans3w2
    q3wc3 = ans3w3

    q4cc =  f'{ans4:,.0f}'
    q4wc1 = f'{ans4 + 200:,.0f}'
    q4wc2 = f'{ans4 - 80:,.0f}'
    q4wc3 = f'{ans4 + 100:,.0f}'

    q5cc = f'{ans5:,.1f}\%'
    q5wc1 = f'{ans5w1:,.1f}\%'
    q5wc2 = f'{ans5w2:,.1f}\%'
    q5wc3 = f'{ans5w3:,.1f}\%'

    q_json["values"].append([s1, s2, s3, s4, t1, t2, t3, t4, f1, f2, f3, f4, 
                            q1cc, q1wc1, q1wc2, q1wc3,
                            q2cc, q2wc1, q2wc2, q2wc3, 
                            q3cc, q3wc1, q3wc2, q3wc3, 
                            q4cc, q4wc1, q4wc2, q4wc3, 
                            q5cc, q5wc1, q5wc2, q5wc3])

q_json["parameters"] = parameters

json.dump(q_json, q_json_file)
q_json_file.close()
