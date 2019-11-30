"""


"""
# 判断一个数是否为质数
def isprime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                    break
        else:
            return num



print(isprime(1))

# 给定范围内所有质数求和
def sum_prime(a,b):
    sum=0
    for i in range(a,b):
        if isprime(i)==i:
            sum+=i
    return sum

print(sum_prime(1,10001))

