# CodeUp_basic100
파이썬 문법 복습

- `map`함수: map(function, iterable) <br>

- `sep` : separation 
```python 
print('s', 'e', 'p', sep = '@') #s@e@p
```

- `end`
```python
print("hello", end=" ")
print("world")
# hello world
```

- format
```python
print("{0}월{1}일 입니다.".format(8,2)) # 8월2일 입니다.
print("%s을 %d개 주세요."%("아이스크림", 10)) # 아이스크림을 10개 주세요.
```

- list
배열 크기 지정해서 선언
```python
lst = [value] * num
```

리스트 요소 대괄호 없이 한번에 출력하기: print(*lst)
```python
lst = [1, 2, 3]
print(*lst) # 1 2 3
# print(lst): [1, 2, 3]
```

배열 역순 정렬
list.reverse(): list 자체를 역순으로 정렬, 함수 반환값 None
reversed(list): 역순으로 정렬된 list 새로운 변수에 할당 가능
```python
lst = [1, 5, 3]
lst2 = lst.reverse()
print(lst) # [3, 5, 1] 메모리 내의 배열 원소들을 직접 수정
print(lst2) # None

lst = [1, 5, 3]
lst2 = reversed(lst)
print(lst) # [1, 5, 3]
print(lst2) # [3, 5, 1]
```