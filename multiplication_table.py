x = (input("Enter the number: "))

try:
    print(f"The multiplication table of {x} is:")
    y = int(x)
    for i in range(1,21):
        print(f"{y}*{i} = {y*i}")
except ValueError:
    print("Invalid Input")
