"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오
"""

N= int(input())
li=[]
for _ in range(N):
    li.append(int(input()))
li.sort()
for ele in li:
    print(ele)