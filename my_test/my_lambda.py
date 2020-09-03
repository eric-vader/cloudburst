 
# Test code
import random
import timeit 
sq = lambda _, x:x*x
incr = lambda _, x:x+1
rand_seq = random.sample(range(-2**50, 2**50), 100)
f = lambda x: sq(None, incr(None, x))

def test():
    for x in rand_seq: 
        f(x)

for rand_seed in range(100):
    random.seed(rand_seed)
    print(timeit.timeit(test, number=10))