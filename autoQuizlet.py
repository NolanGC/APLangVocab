#Paste this into quizlet ot gen a study set
quizlet = ''
#Words in the unit
words = 20 

def empty(l):
    empty = True
    for i in range(len(l)):
        if(l[i] != '\n'):
            empty = False
    return empty
def num_caps(l):
    return sum(1 for c in l if c.isupper())

with open('raw.txt', 'r', encoding='utf-8') as raw:
    lines = raw.readlines()
#print(lines)
with open("out.txt", "w+") as f:
    for i in range(len(lines)):
        if(lines[i].count(' ') <= 2 and not empty(lines[i]) and num_caps(lines[i]) == 1):
            quizlet += lines[i].replace('\n','').replace(' ','')
            quizlet += '|' + lines[i+1]
    f.write(quizlet)


