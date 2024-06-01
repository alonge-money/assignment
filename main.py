
#   find the maximum of three numbers
def maximum(a , b , c):
    num =[a ,b,c]
    return max(num)
print(maximum(10 ,20, 30))


#   sum all the numbers in list.
def sum(a,b,c,d,e):
    return a + b + c + d + e
print(sum(8,2,3,0,7))

#  multiply all the numbers in a list
def multiply(my_list):
    result =1
    for x in my_list:
        result = result * x
    return result
list =[8,2,3,-1,7]    
print(multiply(list))

#  to reversed a string
text = "1234abcd" [::-1]
print(text)

# function to calculate the factorial of a number (a non-negative integer)
def factorial(n):
    if n ==0:
        return 1
    else:
        return  n * factorial(n -1)
n =int(input("Input a number to compute the factorial: "))

print(factorial(n))

# function to check whether a number falls within a given range
def text_range(x):
    x =int(input("check whether a number falls within a given range: "))
    if x in range(3, 9):
        print("%s is in the range" % str(x))
    else:
        print("the number is outside the given range.")   
text_range(19)     
        
#  count upper and lower case charaters without using inbuit functions
def upper_lower(s):
    d ={"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] +=1

        elif c.islower():
            d["LOWER_CASE"] +=1
        else:
            pass
    print("The quick Brown Fox: ", s)
    print("Upper Case Characters: " , d["UPPER_CASE"])
    print("Lower Case Characters: " , d["LOWER_CASE"])
upper_lower("The quick Brown Fox")    

#   takes a list and return a new list with distinct elemnts from the fist list
def uniqun_list(l):
    x = []

    for a in l:
        if a not in x:
            x.append(a)
    return x
print( [1, 2, 3 , 3 , 3 , 3 , 4, 5])    
print(uniqun_list([1, 2, 3 , 3 , 3 , 3 , 4, 5]))


# test the number in prime or not
def text_prime(n):
    n =int(input("checking if number is a prime number: "))

    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
            return True
print(text_prime(100))

# print the even numbers from the list
def even_num(num):
     list = [1,2,3,4,5,6,7,8,9]
     for num in list:
         if num % 2 == 0:
             print(num, end=" ")
even_num(list)             
    