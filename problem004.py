#Python: Division

'''The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer
division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.'''

def division (num1, num2):
    print(num1 // num2)
    print(num1 / num2)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    division(a, b)