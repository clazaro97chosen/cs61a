"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if not k:
        return 1
    else: 
        output  = n
        while k != 1:
            output = output * (n - 1) 
            
            n = n - 1
            
            k -= 1
        return output
#print(falling(4,1))

from doctest import run_docstring_examples
#run_docstring_examples(falling,globals(),True)

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    if n <88:
        return False

    flag = 0
    output  = False
    while n != 0:
        num = n % 10
        #print(num)
        if num == 8:
            flag +=1
        else:
            flag = 0
        
        if flag == 2:
            output  = True

        n = n//10

    return output
#run_docstring_examples(double_eights,globals(),True)
