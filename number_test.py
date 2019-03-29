from numbers import A, B

# A's constructor takes variable of arguments
a1 = A(1,5,3,4,2,3)
assert(a1.evens == [2, 4])   # evens are in sorted order
assert(a1.odds == [1,5,3,3]) # but odds are in the original order
# use __class__.__name__
assert(str(A(4,3,2,5)) == 'A(evens=[2, 4],odds=[3, 5])')
# Two A's are equal if their evens are equal,
# regardless of their odds.
assert(A(4,3,2,5) == A(2,3,4))
assert(A(4,3,2,5) != A(3,4,5))
assert(A(4,3,2,5) != "don't crash here!")
# Note: clearOdds and clearedOdds are not the
# same (only one is destructive)
a2 = A(4,3,2,5)
a2.clearOdds()
assert(str(a2) == 'A(evens=[2, 4],odds=[])')
a3 = A(4,3,2,5)
a4 = a3.clearedOdds()
assert(isinstance(a4, A))
assert(str(a3) == 'A(evens=[2, 4],odds=[3, 5])')
assert(str(a4) == 'A(evens=[2, 4],odds=[])')
# creates an A using values [3,4,5,6,7]
b1 = B(3, 7)
assert(isinstance(b1, A))
assert(str(b1) == 'B(evens=[4, 6],odds=[3, 5, 7])')
# Note: only B's and no other A's can call shifted:
b2 = b1.shifted(2) # so instead of (3,7) it's now (3+2,7+2)
assert(str(b2) == 'B(evens=[6, 8],odds=[5, 7, 9])')
assert(type(b2) == B)
print("Passed!")