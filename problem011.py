#Nested Lists

def sort_students(name_scores):
    scores = []
    for student in name_scores:
        scores.append(student[1])

    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]

    name_scores_lowest = []
    for student in name_scores:
        if student[1] == second_lowest:
            name_scores_lowest.append(student[0])
    name_scores_lowest = sorted(name_scores_lowest)

    for name in name_scores_lowest:
        print(name)


if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])

sort_students(names_scores)