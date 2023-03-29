

if __name__ == '__main__':
    S = input()
    tmp = 'a'
    for s in S:
        if s == tmp:
            print('Bad')
            break
        tmp = s
    else:
        print('Good')