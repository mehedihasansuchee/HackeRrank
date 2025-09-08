#Merge the Tools!


def merge_the_tools(string, k):
    start = 0
    end = k

    while end <= len(string):
        # DO SOME STUFF HEHE
        temp = string[start:end]
        chunk = list(set(list(temp)))

        print(''.join(chunk))

        # KEEP MOVING THE WINDOW
        start += k # start = start + k
        end += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)