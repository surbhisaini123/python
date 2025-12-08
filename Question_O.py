s=input()
S=input()
A,B=s.split()
A = int(A)
B = int(B)

if S=='+':
    print(A+B)
elif S=='-':
    print(A-B)
elif S=='*':
    print(A*B)
elif S=='/':
    print(A//B)            
