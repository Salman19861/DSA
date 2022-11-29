#Q3 lab 5
def multi(n,x):
    if x == 12:
        print(n*x)
    else :
        print(n*x,end =",")
        multi(n,x+1)
multi(2,1)































# #Q2 lab5
# def power(base,exp):
#     if(exp==1):
#         return(base)
#     if(exp!=1):
#         return(base*power(base,exp-1))
# base=int(input("Enter base: "))
# exp=int(input("Enter exponential value: "))
# print("Result:",power(base,exp))











# #Q1 lab5
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 10  #it should be a positive number
# print("Fibonacci sequence:")
# for i in range(nterms):
#     print(recur_fibo(i),end=' ')




