lst = [1,2,3,4,5]

def update_list(n, i):
    n[i] = 100 # mutating n here

print(lst)
update_list(lst,1)
print(lst)


gst = [1,2,3,4,5,6,7,8,9]

def reverse_list(n):
    n = n[::-1] # re-referencing n

print(gst)
reverse_list(gst)
print(gst)


hst = [1,2,3,4,5,6,7,8,9]

def reverse_list_dot_reverse(n):
    n.reverse()

print(hst)
reverse_list_dot_reverse(hst)
print(hst)
