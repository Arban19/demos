x = (input("Enter the number: "))

try:
    print(f"The multiplication table of {x} is:")
    for i in range(1,21):
        print(f"{int(x)}*{i} = {int(x)*i}")
except ValueError:
    print("Invalid Input")
