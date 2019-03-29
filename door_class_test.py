from door_class import C, D, Door
assert(str(C(2,3)) == "<2 and 3>")
assert(C(2,3) == eval(repr(C(2,3))) == C(2,3))
assert(isinstance(D(42), C))
assert(str(D(42)) == "<Just 42>")
assert(D(42) == C(42, 42))
assert(C(1,2) + C(3,4) == C(1+3,2+4))
assert(D(42) + C(3,4) == C(42+3,42+4))
c1 = C(4,5)
c1.reverse()
assert(str(c1) == "<5 and 4>")
c2 = c1.reversed() # note: c1.reversed() is not c1.reverse()
assert(str(c1) == "<5 and 4>")
assert(str(c2) == "<4 and 5>")
#
# #Write the class Door that passes the following test cases.
# #You may not hardcode any test cases.
#
door1 = Door(True, False)
assert((door1.closed == True) and (door1.locked == False))
# print(str(door1))
assert(str(door1) == "Closed and unlocked door")
assert(str(Door(False, False)) == "Open and unlocked door")
door1.turnKey()
assert(door1.locked == True)
assert(str(door1) == "Closed and locked door")
assert(door1 == Door(True, True))
assert(door1 != Door(False, True))
assert(door1 != "Closed and locked door")
# # don’t crash!
s = set()
s.add(Door(False, False))
assert(Door(False, False) in s)
print("Passed")