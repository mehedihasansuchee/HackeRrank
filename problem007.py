#Print Function

'''The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.'''

def print_consecutive_numbers(num):
    final_str = ''

    for i in range (1, num + 1):
        final_str = final_str + str(i)

    print(final_str)

if __name__ == '__main__':
    n = int(input())
    print_consecutive_numbers(n)