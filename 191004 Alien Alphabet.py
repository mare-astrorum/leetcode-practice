words = ["fxasxpc","dfbdrifhp","nwzgs","cmwqriv","ebulyfyve","miracx","sxckdwzv","dtijzluhts","wwbmnge","qmjwymmyox"]
order = "zkgwaverfimqxbnctdplsjyohu"


order_l = list(order)

big_list = []
for word in words:
    big_list.append(list(word))

index_list = []
ind_l = []
for word in words:
    word_l = list(word)
    index_list = []
    for w in word_l:
        ind = order.index(w)
        index_list.append(ind)
    ind_l.append(index_list)


list_answer = []
for i in range(len(ind_l)-1):
    word1 = ind_l[i]
    word2 = ind_l[i+1]
    print(word1)
    print(word2)
    
    for i in range(len(word1)):
        try:
            if word1[i] < word2[i]:
                list_answer.append("true")
                break
            else:
                list_answer.append("false")
                break
        except IndexError:
            list_answer.append("false")

print(list_answer)
if "false" in list_answer:
    print("false")
    
        



