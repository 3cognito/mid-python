# try:
#     # 5 + 'r'
# except Exception as e:
#     print(e)


# if(3 < 6):
#     raise Exception('3 is less than 6')


# assert(9 > 10), '9 is not greater than 10'


class NewErr(Exception):
    pass


try:
    raise NewErr("New Error")
except NewErr as e:
    print(e)
finally:
    print("Finally block")


def test_func():
    try:
        raise NewErr("New Error")
    except:
        return 2
    finally:
        return 3


print(test_func())


class CustomErr(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.value = value
