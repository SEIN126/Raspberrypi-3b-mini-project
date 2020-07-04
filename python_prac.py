a=123
print(type(a))
b=1.2
print(type(b))

aa=[10,20,30,40]
print("aa[-1]은 %d, aa[-2]는 %d" %(aa[-1],aa[-2]))
print("aa[-1]은 %d, aa[-2]는 %d" %(aa[len(aa)-1],aa[len(aa)-2]))

a = [0, 0,0,0]
hap = 0
a[0]= int(input("1번째 숫자: ")) ##input : 키보드로 입력받기.
a[1]= int(input("2번째 숫자: "))
a[2]= int(input("3번째 숫자: "))
a[3]= int(input("4번째 숫자: "))
hap = a[0]+a[1]+a[2]+a[3]
print(hap)

b = []
hap2 = 0
b.append(int(input("1번째 숫자: ")))
b.append(int(input("2번째 숫자: ")))
b.append(int(input("3번째 숫자: ")))
b.append(int(input("4번째 숫자: "))) ##int로 캐으팅 해줬기 때문에 숫자로 인식.
hap2 = b[0]+b[1]+b[2]+b[3]
print(hap2)

c = []
c.append("뭘까요")
print(type(c[0]))

d = input()
print(d)
print(type(d))

e = input("할 말:")
print(e)
print(type(e))
##input 함수는 괄호안의 내용과는 상관 없이 진짜 오로지 키보드로 '입력' 받은 것만 인식.
##기본적으로 string으로 인식한다.

#------------------------------------------------------------------ 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#키보드로부터 입력 받기 => input()

##age = input('나이는?: ')
#print(age)
#print(type(age))

##print(type(int(age)))

##age1 = int(input("나이?: "))
##print(age1)

values =[10, 20, 30, 40, 50]
print(values)
print(values[0])
print(values[0:3]) #슬라이싱. [0:3]==[:3]
print(values[3:]) #[3:5]==[3:4] #끝나는 슬라이싱 번호는 포함 x (x-1까지만 호함)
print(values[0:-2]) #0부터 끝에서 3번째까지 print

values.append(60)
print(values[0:-2])

values[1] = "good"
print(values)

#튜플 선언 소괄호 쓰거나, 아예 안쓰거나
data=(1,2,3,4)
tu = 'a', 'b', 'c'

print(type(data))
print(type(tu))

print(data[1])
print(tu[0:2])

#data[1] = 6 #error. tuple은 변경 불가능.

#타입 변환
list_data = list(data)
print(type(list_data)) #list로 캐스팅

#dictionary type 선언
info = {'number': 12, 'age': 4, 'name': 'Hong'}

print(info['age']) #key가 age인 값 가져오

key=info.keys() #key만 가져오기.
print(key)

p = 'practice'
print(p[0:3])
print(type(p[0:3])) ## str

p1 = 'practice','is','best'
print(p1[0:2])
print(type(p1)) ## tuple

##여러 타입을 packing한 채로 return하는 함수

def get_sum_mul(a,b):
    return a+b,a*b #tuple 타입으로 리턴
    
result = get_sum_mul(2,10)
print("get_sum_mul() result: ",result)

sum, mul = get_sum_mul(2,10)
print("get_sum_mul() result - sum %d, mul%d "%(sum,mul))

#서식지정자 참고
print('happy {}, {}, {}'. format(1, 12.3,6)) #format을 이용한 서식지정자
print('Apple {}, Orange {}, kiwi {}'.format(1000,2000,3000))
print('Apple {1}, Orange {0}, kiwi {2}'.format(1000,2000,3000))

#lambda 함수
add = lambda x,y : x+y
print(add(1,2))
#사용예제
cal = [lambda x,y:x+y, lambda x,y:x-y, lambda x,y:x/y]
print(cal[0](1,2))
print(cal[2](1,2))

#map(함수, 리스트) : 리스트의 요소를 지정된 함수로 처리하여 반환하는 함수.
a = list(map(str,range(10))) #range(10)의 값을 모두 문자열로 만들어서 a 리스트에 저장
print(a)
x,y = map(int,input().split(' '))
#입력받은 2개 문자열 데이터를 x,y에 저장 split(' ')=>공백으로 구분.
print(x,y)

arr = list(range(1,6))
arr = list(map(lambda a:a*a,arr)) #요소처리함수에 lambda사용
print(arr)

#라이브러리 추가
import math as m #math 라이브러리추가. math 를 m으로 별칭

print(m.pi)
print(m.pow(2,3))
print(m.factorial(3))

from math import pow 
#math중에서 pow만 import해서 바로 씀
print(pow(2,3))
