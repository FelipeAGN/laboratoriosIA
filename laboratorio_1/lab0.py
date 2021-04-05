


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.


# What version of Python do we *recommend*  for this course?
#   1. Python v2.3
#   2. Python v2.6 or Python v2.7
#   3. Python v3.XX
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x**3

def factorial(x):
    if(x < 0):
         return 0
    if(x == 0 or x == 1):
         return 1
    i = 2
    sum = 2
    while(i<x):
        i = i + 1
        sum = sum * i
    return sum

def count_pattern(pattern, lst):
    sum = 0
    for i in range (len(lst)- len(pattern)+1):
        for j in  range (len(pattern)):
            if((lst[i+j]) != pattern[j]):
                break
        else:
            sum+=1
    return sum


# Problem 2.2: Expression depth

def depth(expr):
    maxDepth = 0
    if not (hasattr(expr,'__getitem__') and type(expr) != str):
        return 0
    for elem in expr:
        maxDepth = max(maxDepth, depth(elem))
    return maxDepth+1

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    raise NotImplementedError


# Section 3: Symbolic algebra

# La solucion a esta pregunta no debe ser escrita en este archivo
# En su lugar es necesario completar el codigo en el archivo algebra.py

from algebra import Sum, Product, simplify_if_possible


