
#Katya has an unlimited number of cards on which the number 1 is written.
#She wonders if it is possible to put together a number that is divisible by N with these cards. Moreover, she is interested in the number that uses as few cards as possible. Since Katya is not good at math, she asked for your help. 
 
#The format of the input data:
#The only line of input data contains the number N (1≤N≤105). 
 
#Output data format
#In case it is impossible to make up a number, print "NO". Otherwise, output the minimum number composed of units that are divisible by the given




def smallest_number_divisible_by_n(n):
    for i in range(1, n + 1):
        if (10 ** i - 1) % n == 0:
            return str(10 ** i - 1)
    return "NO"

n = int(input().strip())
print(smallest_number_divisible_by_n(n))
