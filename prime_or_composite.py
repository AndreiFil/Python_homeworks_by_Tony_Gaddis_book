# This a small code defines is it number prime or composite and sort it by group

my_range = int(input("The range starts from 1 and ends with the number you specify:  "))

prime_nums = []
composite_nums = []

def prime_or_composite():
    for num in range(2, my_range+1):
        if is_prime(num):
            prime_nums.append(num)
        else:
            composite_nums.append(num)
    print("It's composite numbers in range", composite_nums)
    print("It's prime numbers in range", prime_nums)



def is_prime(numb):
    step = 0
    divider = 0
    acum= []
    while step < numb:
        step += 1
        divider += 1
        if (numb % step == 0):
            acum.append(divider)
        else:
            continue
    if len(acum) > 2:
        status = False
        return status
    else:
        status = True
        return status

prime_or_composite()
