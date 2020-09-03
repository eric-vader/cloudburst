# Test code
import random
import timeit 
from cloudburst.client.client import CloudburstConnection
local_cloud = CloudburstConnection('127.0.0.1', '127.0.0.1', local=True)
sq = lambda _, x:x*x
incr = lambda _, x:x+1
cloud_sq = local_cloud.register(sq, 'sq')
cloud_incr = local_cloud.register(incr, 'incr')
local_cloud.register_dag('f', ['incr', 'sq'], [('incr', 'sq')])
rand_seq = random.sample(range(-2**50, 2**50), 100)

def test():
    for x in rand_seq: 
        local_cloud.call_dag('f', {'incr':[x]}).get()

for rand_seed in range(100):
    random.seed(rand_seed)
    print(timeit.timeit(test, number=10))