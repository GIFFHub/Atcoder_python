

if __name__ == '__main__':
    S = input()
    answers = []
    for i in range(len(S)):
        tmp = S[i:] + S[:i]
        answers.append(tmp)
    answers.sort()

    print(answers[0])
    print(answers[-1])
