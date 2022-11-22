

if __name__ == '__main__':
    N = int(input())
    S = input()

    '''
    考察
    ・A→BB
    ・BB→A
    ・全てのAを全部一旦BBにして、左からBBを全部AAにしていけばいい？
    '''

    S = S.replace('A', 'BB')
    S = S.replace('BB', 'A')
    print(S)


