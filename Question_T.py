# T. Sort Numbers
A,B,C=input().split()
A=int(A)
B=int(B)
C=int(C)
# # NUM=A,B,C

# # print(NUM.sort())
# # print(A,B,C)

# if A<=B and A<=C:
#     if B<=C:
#         print(A,B,C)
#     else:
#         print(A,C,B)   
# elif B<=A and B<=C: 
#     if A<=C:
#         print(B,A,C)
#     else:
#         print(B,C,A)
# else:
#     if A<=B:
#         print(A,B,C)       
#     else:
#         print(C,B,A)

# print(A,B,C)

        
 


nums = [A,B,C]
sorted_nums = sorted(nums)
for x in sorted_nums:
    print(x)

print()
print(A)
print(B)
print(C)
