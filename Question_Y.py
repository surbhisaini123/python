A,B,C,D=input().split()
A=int(A)    
B=int(B)
C=int(C)
D=int(D)
S=(A*B*C*D)%100

print(f"{S:02d}")


