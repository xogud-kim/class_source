# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int, input().split())

numbers = []
# K 개의 입력을 한줄에 받아서 저장 
numbers = list(map(int, input().split()))

# 1부터 N까지의 합 계산 
i = 1 
sub_sum = 0

for i in range(1, N+1):
	sub_sum += i
	i += 1

#sum에서 입력받은 K개 숫자 빼기
a = sub_sum - sum(numbers)
print(a)
