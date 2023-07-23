import reduce

assert reduce.max_number([90,103,230,340,999]) == 999
assert reduce.max_number([]) == None
assert reduce.max_number([-90,-892,-733,-1001,-2344,-8234,-5764,9133]) == 9133
assert reduce.min_number([1,2,3,4,5,6]) == 1
print("All tests passed")
