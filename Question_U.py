N = input().strip()

if '.' in N:
    integer_part, decimal_part = N.split('.')
    
    if decimal_part.strip('0') == "":
        print("int", integer_part)
    else:
        print("float", integer_part, "0." + decimal_part)
else:
    print("int", N)
