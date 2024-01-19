

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
