#Find the Runner-Up Score!


def runner_up(array_students):
    array_students = list(array_students)
    array_students.sort(reverse=True)
    for score in range(len(array_students)):
        if array_students[score] != array_students[score + 1]:
            runner_up = array_students[score + 1]
            break
        else:
            continue
    print(runner_up)

# Execution part
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)