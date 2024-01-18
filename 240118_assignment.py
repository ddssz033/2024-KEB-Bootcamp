# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']


my_list = good()
print(my_list)


# 9.2
def get_odds():
    for a in range(1, 10, 2):
        yield a


counts = 1
for num in get_odds():
    if counts == 3:
        print(num)
        break
    counts += 1


# 9.3
def test(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


@test
def call_finish():
    print("please wait...")


call_finish()


# 9.4

def OopsException(x, y):
    try:
        ans = x / y
        print(ans)
    except ZeroDivisionError:
        print("Caught an oops")


OopsException(3, 0)