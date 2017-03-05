import math #//Utilized in the is_prime function for calculating square roots

def main(): #{
    sum_primes()
#}

def is_prime(testNum): #{
    if (testNum == 2 or testNum == 3): #{ //From the various research I've done about primes for this
                                        # //part, it seems that 2 and 3 behave differently than most other primes;
                                        # //thus, I take care of them here.
        return True
    #}
    
    elif (testNum % 2 == 0): #{ //Get rid of all the even numbers
        return False
    #}
    
    for i in range(3, int(math.sqrt(testNum)+1), 2): #{ //Not the most efficient possible, but this is the most efficient I could make work given the
                                                        # //requirements. In fact, the reason this is two days late is becaues I've been trying to
                                                        # //implement the Sieve of Eratosthenes or the Sieve of Atkin (to no avail.) However, I believe
                                                        # //this still behavies as Big O(sqrt(n)), which is fast enough I suppose.
        if ((testNum % i) == 0): #{
            return False
        #}
    #}
    return True

    

def get_primes(startPoint): #{ //The wonderful yield keyword of Python! This actually tripped me up quite a bit;
                            #  //my original attempts were using functions and not generators, which made it impossibly slow.
    while True: #{
        if (is_prime(startPoint)): #{
            yield startPoint
        #}
        startPoint += 1
    #}
#}
        
def sum_primes(): #{
    sumOfPrimes = 0

    for generatedPrime in get_primes(2): #{ //So to my understanding, generatedPrime is assigned the yielded value of get_primes.
                                         #  //Since get_primes is an infinite generator function, the for loop keeps re-assigning generatedPrime
                                         #  //every time get_primes yields, effectively iterating over the primes.
        if generatedPrime < 2000000: #{
            sumOfPrimes += generatedPrime
        #}

        else: #{
            print (sumOfPrimes)
            return
        #}
    #}
#}
        
if __name__ == '__main__': #{
    main()
#}
