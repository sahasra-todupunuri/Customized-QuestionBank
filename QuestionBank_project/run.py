import os
import random
import json

def gen_code(ln):
    Alpha = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    code = ""
    for x in range(ln):
        code+=Alpha[random.randrange(0,26)]
    return code


del_cmd = 'del ' # for windows
#del_cmd = 'rm ' # for ubuntu

exam_title = "IDP Questions Creation"
no_papers = 1
remove_old_files = 1
generate_key_pdf = 0
generate_exam_pdf = 1
shuffle_questions = 1
show_question_code = 0
key={}
path_to_questionbank ='questionbank/'


if (remove_old_files == 1):
    os.system(del_cmd+" *.pdf")
    os.system(del_cmd+" *.tex")
    os.system(del_cmd+" *.json")
    os.system(del_cmd+" *.aux")
    os.system(del_cmd+" *.log")
    os.system(del_cmd+" *.out")
    os.system(del_cmd+"-d -r ??????????/")

start_text = r"""
\documentclass{exam}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage{pgfplots}
\usetikzlibrary{patterns}
\usepackage{circuitikz}
\ctikzset{bipoles/length=0.8cm}
\usepackage{tikz,lipsum,lmodern}
\usepackage[most]{tcolorbox}
\usepackage{pgfplots}
\renewcommand{\baselinestretch}{1.4}
\definecolor{foo}{HTML}{98777B}
\definecolor{foa}{HTML}{FF5733}
\definecolor{dcm}{HTML}{AA967E}
\setlength\columnsep{20pt}
\usepackage{exam-randomizechoices}
\usepackage{pgfbaseshapes}
\usepackage{geometry}
\usepackage{multirow}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{grffile}
\usepackage{wrapfig}
\usepackage{afterpage}
\usepackage{enumerate}

%\printanswers
\begin{document}
\newgeometry{left=1.5cm,bottom=2cm,right=1.5cm, top=2cm}
\begin{tcolorbox}[colupper=white, arc=0mm, height=4cm,valign=center, halign=center,
enlarge left by=-1.5cm, enlarge top by=-2cm, width=\linewidth+3cm,
colback=dcm, colframe=white]
  {\sffamily \huge """+exam_title+r"""}
\end{tcolorbox}
\begin{tcolorbox}[arc=0mm, height=1.5cm, valign=center, enlarge top by= -3.2cm, enlarge left by=-1cm, width=\linewidth+2cm, colback=white!90!black, colframe=white]
  \flushleft {\sffamily \large \hspace{1cm} Name: \hfill Roll no: \hfill Code : --code-- \hspace{2cm}}
\end{tcolorbox}
\begin{multicols}{2}
\begin{questions}
"""


start_text_key = start_text.replace("%\printanswers","\printanswers")

end_text_key = r"""
\end{questions}
\end{multicols}
\centering{* * * All the Best * * *}
\printkeytable	  
\end{document}
\writekeylist
"""
end_text = r"""
\end{questions}
\end{multicols}
\centering{* * * All the Best * * *}
\vspace{1cm}

%\printkeytable	  
\end{document}
%\writekeylist
"""

codes=[]
key_dict={}
q_dict={}
q_allocation={}

key_dict_f = open('keys.json','w')
q_dict_f = open('questions.json','w')
q_allocation_f = open('question_allocation.json','w')

for x in range(no_papers):
    code = gen_code(10)
    key[code]=[]
    q_dict[code]=[]
    exm = open('exam_'+code+'.tex','w')
    exm_jsn = open('key_'+code+'.json','w')

    exm.write(start_text.replace('--code--',code))
    exm_key = open('exam_key_'+code+'.tex','w')
    exm_key.write(start_text_key.replace('--code--',code))

    sec = os.listdir('sections/')
    random.shuffle(sec)
    qno=0;
    for y in sec:
        exm.write('\section{'+y+'}')
        exm_key.write('\section{'+y+'}')
        print('sections/'+y+'/q_map.csv')
        question_map=open('sections/'+y+'/q_map.csv','r')

        #print("question_map",question_map)
        q_first = question_map.readline()
        #print("First Question",q_first)
        q_second_onwards = []
        for q_line in question_map:
              q_second_onwards.append(q_line)            
        #print("before:", q_second_onwards)
        if shuffle_questions==1:
              random.shuffle(q_second_onwards)
        #print("after:",q_second_onwards)
        final_q_list = [q_first]+q_second_onwards

        for q_line in final_q_list:
            #print(q_line)
            q_selected = random.choice(q_line.strip().split(","))
            q_dict[code].append(q_selected)
            if q_selected in q_allocation:
                q_allocation[q_selected].append(code)
            else:
                q_allocation[q_selected] = [code]
            q_text = open(path_to_questionbank+q_selected+'/'+q_selected+'.tex','r').read()
            print(q_selected)
            #print(q_text)
            if os.path.exists(path_to_questionbank+q_selected+'/'+q_selected+'.json'):
                p_json = json.load(open(path_to_questionbank+q_selected+'/'+q_selected+'.json','r'))
                pars = p_json["parameters"]
                vals = random.choice(p_json["values"])
                key[code].append([q_selected,pars,vals])
                for idx,p in enumerate(pars):
                    q_text=q_text.replace("--"+p+"--",str(vals[idx]))
                qno+=1
                if (show_question_code==1):
                    q_text=q_text.replace("\\begin{randomizechoices}",
                                          "("+q_selected+")\\begin{randomizechoices}")
            exm.write(q_text)
            exm_key.write(q_text)
    exm.write(end_text)
    exm.close()
    exm_key.write(end_text_key)
    exm_key.close()
    if (generate_exam_pdf == 1):
        os.system('pdflatex exam_'+code+'.tex')
        #os.system('del exam_'+code+'.aux')
        os.system(del_cmd+' exam_'+code+'.log')
    if (generate_key_pdf == 1):
         os.system('pdflatex exam_key_'+code+'.tex')
         os.system('pdflatex exam_key_'+code+'.tex')
         os.system(del_cmd+' exam_key_'+code+'.aux')
         os.system(del_cmd+' exam_key_'+code+'.log')
    json.dump(key,exm_jsn)
    exm_jsn.close()


    answer_list= []
    f_aux = open('exam_'+code+'.aux','r')
    for line in f_aux:
        if "correctchoice}{{" in line:
            answer_list.append(line.split("correctchoice}{{")[1][0])
    key_dict[code] = answer_list
    f_aux.close()


    #moving files
    os.system("mkdir "+code)
    os.system("move exam_" + code + ".tex " + code + "/")
    os.system("move exam_key_" + code + ".tex " + code + "/")
    os.system("move exam_" + code + ".aux " + code + "/")
    os.system("move exam_" + code + ".out " + code + "/")
    os.system("move key_" + code + ".json " + code + "/")

#print(key_dict)

json.dump(key_dict, key_dict_f)
key_dict_f.close()


json.dump(q_dict, q_dict_f, indent=2)
q_dict_f.close()

json.dump(q_allocation, q_allocation_f)
q_allocation_f.close()

