'''def palindrome(str):
    op=""
    for x in range(len(str)-1,-1,-1):
        op+=str[x]
    print(op)
    if str==op:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")      
palindrome(str("eye"))          

'''

def undscr(str):
    op=""
    for i in range(len(str)):
        if str[i]=="_":
            continue
        op+=str[i]
    print(op)
undscr("Full_St_ac_k")      