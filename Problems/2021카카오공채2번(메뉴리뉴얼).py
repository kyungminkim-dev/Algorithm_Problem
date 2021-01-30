from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in range(len(orders)):
        temp = ''.join(sorted(list(orders[i])))
        orders[i] = temp
            
    for num in course: #course의 음식 수 
        all_list = []
        for order in orders:
            temp = list(map(lambda x : ''.join(x), list(combinations(order,num))))
            all_list.extend(temp)
            
        if not all_list:
            continue
        
        counter = Counter(all_list)
        max_num = counter.most_common(1)[0][1]
        if max_num < 2:
            continue
        for k,v in counter.items():
            if v == max_num:
                answer.append(k)
    answer.sort()                           
    return answer
