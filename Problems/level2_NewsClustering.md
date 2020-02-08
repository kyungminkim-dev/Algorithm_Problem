#### 문제 : <https://programmers.co.kr/learn/courses/30/lessons/17677> #2018 KAKAO BLIND RECRUITMENT

---
```
def make_same(str1):   #문자열의 모든 문자를 소문자로 바꾸어준다.
    trans_str = ''
    for i in str1:
        temp = ''
        if ord(i)>=65 and ord(i)<=90:
            temp = chr(ord(i)+32)
        else:
            temp = i
        trans_str += temp
    return trans_str

def make_list(str1): #주어진 문자열을 두 문자씩 끊고 영문자가 아닌 문자열의 경우를 뺀 글자들을 반환한다. 
    list_1 = []
    last_list = []
    temp = ''
    for i in str1:
        temp += i
        if len(temp) ==2:
            list_1.append(temp)
            temp = temp[1]
    for i in range(len(list_1)):
        if (ord(list_1[i][0]) >=97 and ord(list_1[i][0]) <=122) and (ord(list_1[i][1]) >=97 and ord(list_1[i][1]) <=122):
            last_list.append(list_1[i])     
    return last_list

def gyo_function(a,b):  # 두 리스트의 교집합을 구한다. 문제에서 주어진 집합은 다중집합이므로 set사용불가
    gyolist =[]
    for i in a:
        if i in b:
            b.remove(i)
            gyolist.append(i)
    return gyolist

def solution(str1,str2):
    answer = 0
    str_1 = make_same(str1)
    str_2 = make_same(str2)
    list_1 = make_list(str_1)
    list_2 = make_list(str_2)
    
    gyolist = gyo_function(list_1,list_2)
    hap = make_list(str_1)
    hap.extend(make_list(str_2))
    for i in gyolist:
        if i in hap:
            hap.remove(i)
    if len(list_1) == 0 and len(list_2) == 0:
        answer = 65536
        return answer
    jacad =  len(gyolist) / len(hap) 
    answer = int(jacad*65536)
    return answer
```
---
### 고찰
**이 문제는 주어진 문자열집합이 다중집합인것이 까다로웠다. set함수를 쓸 수 없어 합집합과 교집합을 구할 때 list관련 함수를 이용해 jacad값을 구하여 문제를 풀었다.**
