#Paste this into quizlet ot gen a study set
quizlet = ''
#Words in the unit
words = 20 
with open('raw.txt', 'r', encoding='utf-8') as raw:
    lines = raw.readlines()
#print(lines)
for i in range(0,4*words - 20,4):
    quizlet += lines[i].rstrip()
    quizlet += '|'
    quizlet += lines[i+1]
    quizlet += '\n'

print(quizlet)