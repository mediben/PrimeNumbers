# PrimeNumbers
A simple rest API that returns a list of numbers and the corresponding values from the normal sequence of prime numbers from 1 to N with support for pagination.


There is a single endpoint "http://127.0.0.1:5000/primes" takes json object contating one parameter : 
{"number" : int} and returns a list of all possible primes numbers from 1 to that number.
