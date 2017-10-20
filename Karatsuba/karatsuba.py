import time

def multiplication(op1, op2):
    return int(op1) * int(op2)


def multiplication_usual(op1, op2):
    base = 10

    length = max(len(op1), len(op2))

    op1 = "0"*(length - len(op1)) + op1
    op2 = "0" * (length - len(op2)) + op2

    result = [0 for x in range(len(op1) + len(op2))]
    for i in range(len(op1)):
        carry = 0
        for j in range(len(op2)):
            index = len(result)-i-j-1
            result[index] += int(op1[len(op1)-i-1]) * int(op2[len(op2)-j-1]) + carry
            carry = result[index] // base
            result[index] %= base
        result[len(result)-i-len(op2)-1] += carry
    return int(''.join(str(x) for x in result))

def multiplication_karatsuba(x, y):

    # print("-"*40)
    # print('Starting multiplication_karatsuba with {} and {}'.format(x,y))
    base = 10
    length = max(len(x), len(y))
    if length < 2:
        result =  int(x) * int(y)
        # print('result is {}'.format(result))
        return result

    x = "0"*(length - len(x)) + x
    y = "0" * (length - len(y)) + y
    m = length // 2


    x1 = x[:m]
    x0 = x[m:]

    y1 = y[:m]
    y0 = y[m:]

    p = len(y0)

    # print('x1={}, x0={}, y1={}, y0={}'.format(x1, x0, y1, y0))

    z2 = multiplication_karatsuba(x1, y1)
    # print('z2={}'.format(z2))
    z0 = multiplication_karatsuba(x0, y0)
    #print('z0={}'.format(z0))
    z1 = multiplication_karatsuba(str((int(x1)+int(x0))), str((int(y1)+int(y0)))) - z2 - z0
    #print('z1={}'.format(z1))
    result = z2 * (base**(2*p)) + z1 *(base**p) + z0
    # print('m is {}, result is {}'.format(m, result))
    return result



multiplicandFirst = input("Enter first multiplicand: ")
multiplicandSecond = input("Enter second multiplicand: ")

print("-"*80)
print("-"*80)
#MACHINE
t1 = time.clock()
res = multiplication(multiplicandFirst, multiplicandSecond)
t2 = time.clock()

delta = (t2 - t1) * 1000000
print("Result is {} by machine multiplication.\nExecution time is {:.3f} ns".format(res, delta))
print("-"*80)

# USUAL
t1 = time.clock()
res = multiplication_usual(multiplicandFirst, multiplicandSecond)
t2 = time.clock()

delta = (t2 - t1) * 1000000
print("Result is {} by usual multiplication.\nExecution time is {:.3f} ns".format(res, delta))
print("-"*80)

#KARATSUBA
t1 = time.clock()
res = multiplication_karatsuba(multiplicandFirst, multiplicandSecond)
t2 = time.clock()

delta = (t2 - t1) * 1000000
print("Result is {} by karatsuba multiplication.\nExecution time is {:.3f} ns".format(res, delta))
print("-"*80)
print("-"*80)