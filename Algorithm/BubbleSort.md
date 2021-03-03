### BubbleSort

* 버블 소트는 가장 큰 값을 먼저 찾아 리스트의 가장 오른쪽에 정렬한다. 가장 큰 값이 오른쪽으로 옮겨오는 모습이 거품이 올라오는 것 처럼 보여 버블소트라 한다.

```
def BubbleSort(arr):
  n = len(arr)
  for i in range(n-1):  #outer loop가 하나 돌 때마다 리스트의 가장 큰 값이 오른쪽으로 정렬된다.
    for j in range(n-i-1): #위와 같은 이유로 inner loop의 범위값이 하나씩 줄어들게 된다. 
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
```

* 버블 소트의 시간복잡도는 평균, 최악이 O(n^2)이며 최선의 시간복잡도는 모든 리스트의 값이 정렬된 상황이므로 O(N)이다.
