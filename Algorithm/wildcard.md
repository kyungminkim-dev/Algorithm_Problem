#### 문제 <https://www.algospot.com/judge/problem/read/WILDCARD>
---
```
def match(w,s):
    pos = 0
    while(pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos] == s[pos])):
        pos += 1
    if pos == len(w):
        return pos == len(s)
    if (w[pos] == "*"):
        for skip in range(len(s) - pos + 1):
            if match(w[pos+1:],s[pos+skip:]):
                return True
    return False 
```
---
#### 고찰
"알고리즘 문제해결 전략" 이라는 책에서 저자가 재귀함수를 사용해서 풀어낸 알고리즘이다. 재귀함수와 완전탐색만을 이용하여 답을 구했다.

저자는 "*"의 개수가 많아질수록 시간이 많이 걸린다는 것을 말하며, 메모이제이션을 쓰는 코드를 뒷부분에 추가해 두었다.

나는 이 문제를 처음 접했을 때, s와 w의 길이가 같을때 와 다를때의 경우를 나누어서 생각했는데 길이가 다를때 어떻게 짜야하는지 막혔었다.

그런데 while문과 if문을 사용해서 처리하는것이 신기하고 이해될때 까지 시간이 많이 걸렸다. 아직 재귀함수를 쓸 수 있는 능력이 부족한것 같다.

추후에 메모이제이션을 이용하여 중복을 제거해 더 빠른 속도를 내는 알고리즘도 공부해서 올려야겠다.
