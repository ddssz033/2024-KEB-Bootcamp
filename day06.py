def good() -> list:
    harry_porter = input().split()
    return harry_porter

print(good())

def get_odds(n):
    for i in range(1, n+1, 2):
        yield i
cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt += 1
    if cnt == 3:
        print(f'Thind number is {odd}')
        break

def test(f):
    #데코레이터 함수, 함수 시작하며 start 출력 끝나면 end 출력
    def test_in(*args, **kwargs):
        print('start')
        result = f(*args, **kwargs)
        print('end')
        # return result
    return test_in

@test
def greeting():
    print("안녕하세요")

greeting()