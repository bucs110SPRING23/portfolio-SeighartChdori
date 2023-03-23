def twomult(x,y) :
    result = 0
    for _ in range(y) :
        result += x
    return result

def exponent(x,y) :
    blank = 1
    for _ in range (y) :
        blank = blank * x
    return blank

def square(x) :
    return exponent(x,2)

num1 = 5
num2 = 2
print(twomult(num1,num2))
print(exponent(num1,num2))
print(square(num1))
print(square(num2))