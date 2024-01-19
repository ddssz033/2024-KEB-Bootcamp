import random
numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)

try:
    pick = int(input(f"input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
except IndexError as err:
    print(f"wrong idx number\n{err}")
except ValueError as err:
    print(f"input only number\n{err}")
except ZeroDivisionError as err:
    print(f"the denominator cannot be 0. \n{err}")
except Exception: #가장 범위가 넓은 에러는 가장 밑으로
    print('error occurs')