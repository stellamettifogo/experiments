
import random

from addition import addition

def random5() -> int:
    """ Returns an integer 1 through 5. """
    return random.randint(0,4) + 1



def zero_or_one():
    """ Returns 0 or 1. """
    while True:
        r = random5() - 1
        if r < 2:
            return r


def random7() -> int:
    """ Returns an integer from 1 to 7. """
    while True:
        rnd = ((random5() - 1) * 2) + zero_or_one()
        if rnd < 7:
            return rnd + 1


# test random5

distribution5 = [0, 0, 0, 0, 0]

for i in range(5000):
    rnd = random5()
    #print(rnd)
    assert rnd >= 1 and rnd <= 5
    # keep track of random distribution
    distribution5[rnd -1] = distribution5[rnd -1] + 1 

print(distribution5)

# test random2 base0
distribution2 = [0,0]
for i in range(5000):
    rnd = zero_or_one()
    assert rnd >= 0 and rnd <= 1
    distribution2[rnd] = distribution2[rnd] + 1 
print(distribution2)


# test random7
distribution7 = [0] * 7
for i in range(7000):
    rnd = random7()
    assert rnd >= 1 and rnd <= 7
    distribution7[rnd -1 ] = distribution7[rnd -1 ] + 1 
print(distribution7)


    




