def search(key_table, char):
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == char:
                return i, j
    return None
def encrypt(msg,mat):
    if len(msg)%2 != 0:
         msg += 'x'
    en_msg = ''
    i = 0
    while i<len(msg):
        first = msg[i]
        second = msg[i+1]
        row1,col1 = search(mat,first)
        row2,col2 = search(mat,second)
        if row1 == row2:
            en_msg += mat[row1][(col1+1)%5]
            en_msg += mat[row2][(col2+1)%5]
        if col1 == col2:
            en_msg += mat[(row1+1)%5][col1]
            en_msg += mat[(row2+1)%5][col2]
        else:
            en_msg += mat[row1][col2]
            en_msg += mat[row2][col1]
        i+=2
    return en_msg
def decrypt(en_msg,mat):
    de_msg = ''
    i = 0
    while i<len(msg):
        first = en_msg[i]
        second = en_msg[i+1]
        row1,col1 = search(mat,first)
        row2,col2 = search(mat,second)
        if row1 == row2:
            de_msg += mat[row1][(col1-1)%5]
            de_msg += mat[row2][(col2-1)%5]
        if col1 == col2:
            de_msg += mat[(row1-1)%5][col1]
            de_msg += mat[(row2-1)%5][col2]
        else:
            de_msg += mat[row1][col2]
            de_msg += mat[row2][col1]
        i+=2
    return de_msg
        
key = "monarchy"
mat = [[0 for _ in range(5)] for _ in range(5)]
char = 0
used_char = set('abcdefghiklmnopqrstuvwxyz')
for i in range(5):
    if char>=len(key):
            break
    else:
         for j in range(5):
            if char>=len(key):
                 break
            mat[i][j] = key[char]
            used_char.remove(key[char])
            char+=1
used_char = list(used_char)
used_char.sort()
char = 0
for jj in range(j,5):
     mat[i-1][jj] = used_char[char]
     char+=1
for ii in range(i,5):
    for jj in range(5):
        mat[ii][jj] = used_char[char]
        char+=1
msg = "attack"
en_msg = encrypt(msg,mat)
de_msg = encrypt(en_msg,mat)
print(encrypt(msg,mat))
print(de_msg)