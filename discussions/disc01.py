def wears_jacket_with_if(temp,raining):
    if temp<= 60 or raining:
        return True
    else:
        return False
def wears_jacket(temp,raining):
    return temp<=60 or raining 

def is_prime(n):
    if n == 1:
        return False
    else:
        num = n-1
        flag = True
        while num!=1:
            if n % num == 0:
                flag = False
            num -=1
        return flag

def double(x):
    return x * 2
def triple(x):
    return x * 3
hat = double
double = triple
print(hat(2))