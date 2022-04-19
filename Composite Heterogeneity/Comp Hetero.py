## NOTES
## 202204191347
## to avoid redundancy


## import libraries
import numpy as np
import math
import pandas as pd
from pandas import DataFrame


## define functions
def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            #print(n)
            #print(i)
            i += 1
        else:
            #print(n)
            #print(i)
            n //= i
            #print(n)
            #print(i)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


## needed lists
list_of_numbers = range(1,1000 + 1)
exponent_hetero = []
mod_hetero = []


## loop through list of numbers
for the_number in list_of_numbers:
    
    ## get prime factors of number
    prime_factors = get_prime_factors(the_number)
    number_of_factors = len(prime_factors)
    
    ## reset counters
    hetero_counter = 0
    mod_counter = 0
    
    ## if number is not a prime
    if number_of_factors > 1:
        
        ## looping through list of prime factors twice
        for index_1, prime_1 in enumerate(prime_factors):
            for index_2, prime_2 in enumerate(prime_factors):
                if index_1 <= index_2: ## 202204191347
                    if prime_1 > prime_2:
                        
                        ## exponent approach
                        exponent = math.log(prime_1,prime_2)
                        exponent_round_up = math.ceil(exponent)
                        exponent_round_down = math.floor(exponent)
                        if abs(prime_1 - prime_2 ** exponent_round_up) <= abs(prime_1 - prime_2 ** exponent_round_down):
                            hetero_counter = hetero_counter + abs(prime_1 - prime_2 ** exponent_round_up)
                        else:
                            hetero_counter = hetero_counter + abs(prime_1 - prime_2 ** exponent_round_down)
                        
                        ## mod approach
                        mod_value = prime_1 % prime_2
                        if mod_value <= (prime_2 - mod_value):
                            mod_counter = mod_counter + mod_value
                        else:
                            mod_counter = mod_counter + (prime_2 - mod_value)
                        
                        
                    else:
                        
                        ## exponent approach
                        exponent = math.log(prime_2,prime_1)
                        exponent_round_up = math.ceil(exponent)
                        exponent_round_down = math.floor(exponent)
                        if abs(prime_2 - prime_1 ** exponent_round_up) <= abs(prime_2 - prime_1 ** exponent_round_down):
                            hetero_counter = hetero_counter + abs(prime_2 - prime_1 ** exponent_round_up)
                        else:
                            hetero_counter = hetero_counter + abs(prime_2 - prime_1 ** exponent_round_down)
                            
                        ## mod approach
                        mult_factor = round(prime_2 / prime_1)
                        mod_counter = mod_counter + abs(prime_2 - prime_1 * mult_factor)
        
        exponent_hetero.append(hetero_counter)
        mod_hetero.append(mod_counter)
        
    ## if number is prime
    else:
        exponent_hetero.append(None)
        mod_hetero.append(None)


## create dataframe and write to csv
hetero_df = DataFrame({'Number': list_of_numbers, 'Modulus Approach': mod_hetero, 'Exponent Approach': exponent_hetero})
hetero_df.to_csv('Composite Hetero.csv',index = False)
