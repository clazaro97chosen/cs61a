



# def icascade(n):
#     grow(n)
#     print(n)
#     shrink(n)

# def f_then_g(f,g,n):
#     if n:
#         f(n)
#         g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# grow = lambda n: f_then_g(lambda f: grow(n//10) print(n) if f > 10,print(n),n)
# shrink = lambda n: f_then_g(print(n) if n < 10 , print(n) shrink(n//10))

# def ishrink(n):
#     if n < 10:
#         print(n)
#     else:
#         print(n)
#         icascade(n//10)
# def igrow(n):
#     if n > 10:
#         icascade(n//10)
#         print(n)
#     else:
#         print(n)
def cascade(n):
        """Print a cascade of prefixes of n."""
        print(n)
        if n >= 10:
            cascade(n//10)
            print(n)
cascade(1234)
#prints
#1
#12
#123
#1234
#123
#12
#1

