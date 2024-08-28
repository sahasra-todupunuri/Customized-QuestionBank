# python file to generate the json options for the question
import random, math, json

q_json_file = open("AWRTG.json","w")     

def rr(mn, mx, st):
    return random.randrange(mn, mx, st)

def f2s(no,d):
    s1 = "{z:0."+str(d)+"f}"
    return s1.format(z=no)


def get_ckt_values():
	# given parameters for the question
	s1=rr(25,45,1)  
	s2=rr(46,66,1)  
	s3=rr(15,24,1)  
	s4=rr(90,120,1)  
	s5=rr(78,130,1)  
	return [s1,s2,s3,s4,s5]

q_json={}
q_json["values"]=[]


for x in range(300):
	[s1,s2,s3,s4,s5] = get_ckt_values()
	numbers = [s1,s2,s3,s4,s5]
	mean = sum(numbers) / len(numbers)
	variance = sum([((x - mean) ** 2) for x in numbers]) / len(numbers)
	sd = math.sqrt(variance)
	 	 
	q1cc = f'{sd:0.3f}'
	q1wc1 = f'{sd+1:0.3f}'
	q1wc2 = f'{mean:0.3f}'
	q1wc3 = 'data insufficient'

	q_json["values"].append([s1,s2,s3,s4,s5,
                       q1cc, q1wc1, q1wc2, q1wc3])

q_json["parameters"]=["s1","s2","s3","s4","s5",
                       "q1cc","q1wc1","q1wc2","q1wc3"]

json.dump(q_json, q_json_file)
q_json_file.close()







