#Capitalize!


def sovle(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s

if __name__ == '__main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input

    result = sovle(S)

    fptr.write(result + '\n')

    fptr.close()