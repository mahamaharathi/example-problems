# Euclidean Algorithm
# The algorithm is based on the below facts.

#  If we subtract a smaller number from a larger (we reduce a larger number), GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
#  Now instead of subtraction, if we divide the smaller number, the algorithm stops when we find remainder 0.

def gcd_of_two_numbers(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be integers only"
    if b == 0:
        return a
    return gcd_of_two_numbers(b, a % b)


print(gcd_of_two_numbers(14, 58))
