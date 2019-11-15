'''
https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/
'''


BALL
AREA
LEAD
LADY


seq = ['BALL', 'AREA', 'LEAD', 'LADY']
newlist = []

index = 0
word = 'BALL'
for letter in word:
    for i in seq:
        newlist.append(i[index])
    index+=1
    
length = len(word)
indx = 0
p = []
for a in newlist:
    wordy = newlist[indx] + newlist[indx+1]+newlist[indx+2]+newlist[indx+3]
    p.append(wordy)
    indx += 4
    

for a in range(length):
    wordy = newlist[indx] + newlist[indx+1]+newlist[indx+2]+newlist[indx+3]
        print(wordy)
    indx += 4
        