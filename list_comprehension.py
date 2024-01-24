def square_even_mf(n):
    evens = list(filter(lambda x: x%2 == 0, n))
    return list(map(lambda y: y*y, evens))

print(square_even_mf([1,2,3,4,5,6,7,8]))

def square_even_for_loop(n):
    squares = []
    for x in n:
        if x%2 == 0:
            squares.append(x*x)
    return squares

print(square_even_for_loop([1,2,3,4,5,6,7,8]))

def square_even_lc(n):
    return [x*x for x in n if x%2 == 0]

print(square_even_lc([1,2,3,4,5,6,7,8]))
