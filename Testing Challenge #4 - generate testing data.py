#http://testingchallenges.thetestingmap.org/challenge4.php  test task

import random

first_digit = random.randint(1,9)               #random.randint get a random number in a given interval

if first_digit > 4 and first_digit < 7:          # if we get 5 or 6, the person's year of birth cannot be more than the current year
    second_digit = random.randint(0,2)
    third_digit = random.randint(0,2)
else:
    second_digit = random.randint(0, 9)
    third_digit = random.randint(0, 9)

fourth_digit = random.randint(0,1)              #the fourth and fifth numbers are for the month
if fourth_digit < 1:
    fifth_digit = random.randint(1,9)
else:
    fifth_digit = random.randint(0,2)

sixth_digit = random.randint(0,2)               #the sixth and seventh numbers indicate the date
seventh_digit = random.randint(0,8)             #limited the maximum date, in order to bypass errors with invalid data :(

eighth_digit = random.randint(0,5)              #The eighth and ninth indicate the region (01 to 52)
if eighth_digit < 5:
    ninth_digit = random.randint(0,9)
else:
    ninth_digit = random.randint(0,2)
tenth_digit = random.randint(0,9)              #9,10,11 - ordinal number from 000 to 999
eleventh_digit = random.randint(0,9)
twelfth_digit = random.randint(0,9)

x = (2 * first_digit + 7 * second_digit + 9 * third_digit + 1 * fourth_digit + 4 * fifth_digit + 6 *
     sixth_digit + 3 * seventh_digit + 5 * eighth_digit + 8 * ninth_digit + 2 * tenth_digit + 7 * eleventh_digit
     + 9 * twelfth_digit)  #is the result of multiplying each number by the corresponding position number from that line: 279146358279

thirteenth_digit = x % 11  #divide with remainder

print(str(first_digit)+str(second_digit)+str(third_digit)+str(fourth_digit)+str(fifth_digit)+str(sixth_digit)+
      str(seventh_digit)+str(eighth_digit)+str(ninth_digit)+str(tenth_digit)+str(eleventh_digit)+str(twelfth_digit)+
      str(thirteenth_digit))    #str removes spaces between numbers, for easier copying of the whole number






