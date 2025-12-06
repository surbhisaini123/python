
# V. Comparison
A,S,B=input().split()
A=int(A)
B=int(B)
# S=int(S)
# if A>B or A==B:
#     print("Right")
    
# else:
#     print("Wrong")    

if S=='>':
    if A>B:
        print("Right")
    else:
        print("Wrong")
elif S=='<':
    if A<B:
        print("Right")
    else:
        print("Wrong")
elif S=='=':
    if A==B:
        print("Right")
    else:
        print("Wrong")                     
