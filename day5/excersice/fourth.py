
def prime_numbers( number ):
    cota_superior = number**0.5
    for num in range(2, int( cota_superior + 1)):
        res =  number % num 
        print( res )
        if res == 0:
            return False
    return True     
print(prime_numbers( 12 ))