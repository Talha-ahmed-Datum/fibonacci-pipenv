import sys
def fibonacci(n):
    first = 0
    second = 1
    num = n
    if (num == 1):
        val = int(first)
    elif (num == 2):
        val = int(second)
    else:
        for i in range(num-2):
            val= first + second
            first =  second
            second = val
    print (num)
    print (val)
    return val

if __name__ == '__main__':
    n=int(sys.argv[1])
    val=fibonacci(n)
    print("The {0} value of fibonacci series is {1}".format(n,val))