univ = "inha"
i = 0
while i < len(univ):
    print(univ[i], end=' ')
    i = i + 1

print()

for letter in univ: #오류가능성이 적고 코드가 간단하다
    print(letter, end=' ') #end는 글자 옆으로 나오게 하는 용도

# 특정 구간만 제어하고 싶다 -> while이 좋다(시작점, 인덱스 등 조절 용이)
# 전부 출력하고 싶다 -> for이 좋다(range로 구간 조절 가능함)

print()

for k in range(0, len(univ)): #0부터 univ의 길이까지
    print(univ[k], end=' ')

#primenumber for ver
#prime number
number = int(input("input number : "))
is_prime = True #int -> bool

if number < 2:
  print(f'{number} is not prime number')
else:
  for i in range(2, number):
    if number % 1 == 0:
      is_prime = False
      break

  if is_prime:
    print(f'{number} is prime number')
  else:
    print(f'{number} is not prime number')