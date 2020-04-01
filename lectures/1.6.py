def memoize(f):
    cache = {}
    def helper(x):
        if x not in cache:            
            cache[x] = f(x)
        return cache[x]
    return helper
    
def trace(f):
    def helper(x):
        call_str = '{0}({1})'.format(f.__name__, x)
        print('Calling {0} ...'.format(call_str))
        result = f(x)
        print('... returning from {0} = {1}'.format(call_str, result))
        return result
    return helper

@memoize
@trace
def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2) 



def type_check(correct_type):
    def insurance(old_function):
            def new_function(arg):
                if (isinstance(arg,correct_type)):
                    return old_function(arg)
                else:
                    print('Bad Type')
            return new_function
    return insurance

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])



# def score(dice):
#     score = 0
#     for i in range(6):
#         if i == 0:
#             if dice.count(i+1) >= 3:
#                 score   = score + 1000 + (dice.count(i+1)-3) * 100
#             else:
#                 score = score + (dice.count(i+1) * 100)

#         elif i == 4:
#             if dice.count(i+1) >= 3:
#                 score   = score + 500 + (dice.count(i+1) -3)* 100
#             else:
#                 score = score + (dice.count(i+1) * 50)

#         else:
#             if dice.count(i+1) >=3:
#                 score = score + (i+1) *100
#     return score

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    print(die)
    counter[die-1] += 1
    print(counter)
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

  return sum 

print(score([1,1,1,3,1]))






