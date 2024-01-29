import time

print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
                     # epoch = when your computer thinks time began (reference point)

print(time.time()) # return current second since epoch

print(time.ctime(time.time())) # return current date

time_object = time.localtime()
print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)
