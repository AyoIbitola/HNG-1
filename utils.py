import math


def get_number(n):
    number = int(n)
    return number


def is_prime(n ):
    
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True



def is_perfect(n):
   
    if n < 0:
        return False
    square_rootn = math.sqrt(n)
    perfect_val = square_rootn.is_integer()
    return perfect_val

##answer = is_perfect()
##print(answer)

def is_Armstrong(n):
    
    l = len(str(n))
    Armstrong = "Armstrong number"
    not_Armstrong = ""
    sum = 0
    if n < 0:
        return not_Armstrong
    for i in str(n):
        sum = sum + int(i)**int(l)

    if (sum == n):
        return Armstrong
    else:
        return not_Armstrong
    

# answer = is_armstrong(153)
# print(answer)

def is_Even_or_Odd(n):
    
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

def properties(n):
    number = int(n)
    if is_Armstrong(n) == "Armstrong number":
        property = [is_Armstrong(n),is_Even_or_Odd(n)]
    else:
        property = [is_Even_or_Odd(n)]
    return property


def digit_sum(n):
    
    sum = 0
    for i in str(abs(n)):
        sum += int(i)
    return sum

# answer5 = properties(152)
# print(answer5)


# answer = digit_sum( -152)
# print(answer)
