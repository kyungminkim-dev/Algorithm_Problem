#### 이항계수(binomial coefficient)
- 이항계수는 정해진 집합안에서 원하는 개수만큼 순서에 상관없이 선택하는 경우의 수를 말한다. nCr은 n개의 원소를 가지는 집합에서 r개를 뽑는 경우의 수를 말한다.

---
```
matrix = [[-1 for col in range(100)] for row in range(100)]
def bino2(n,r):
    if (r == 0 or n == r): return 1

    if matrix[n][r] != -1:
        return matrix[n][r]

    matrix[n][r] = bino2(n-1,r-1) + bino2(n-1,r)
    return matrix[n][r]
```
---
이항계수의 성질에는 nCr = n-1Cr + n-1Cr-1 이라는 성질을 가지고 있다. 이와함께 메모이제이션을 이용하여 이항계수를 구하는 코드이다. 

동적계획법을 이용하여 전에 구했던 값들을 저장해놓고 반복사용할때마다 꺼내어 사용한다. r의 최대값은 전체 집합의 원소의 개수인 n이고 각 문제를 해결할 
때 마다 걸리는 시간은 반복문이 없으니 O(1)이다. bino(n,r)을 구할때 만날 수 있는 문제의 최대 개수는 n^2이므로 위의 알고리즘의 시간복잡도는 O(n^2)이다.
