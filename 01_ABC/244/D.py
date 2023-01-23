

if __name__ == '__main__':
    S = ''.join(input().split())
    T = ''.join(input().split())

    team = {'RGB', 'BRG', 'GBR'}

    '''
    偶置換
    RGB
    BRG
    GBR
        
    奇置換
    RBG
    GRB
    BGR
    '''

    if S in team:
        if T in team:
            ans = 'Yes'
        else:
            ans = 'No'
    else:
        if T not in team:
            ans = 'Yes'
        else:
            ans = 'No'

    print(ans)

