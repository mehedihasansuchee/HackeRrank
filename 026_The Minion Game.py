#The Minion Game


def minion_game(string):
    vowels = 'AEIOU'
    kevin_scores = stuart_scores = 0
    lenght = len(string)
    for i in range(lenght):
        if string[i] in vowels:
            kevin_scores += lenght - i
        else:
            stuart_scores += lenght - i
    if stuart_scores > kevin_scores:
        print(f'Stuart {stuart_scores}')
    elif kevin_scores > stuart_scores:
        print(f'Kevin {kevin_scores}')
    else:
        print(Draw)

if __name__ == '__main__':
    s = input()
    minion_game(s)