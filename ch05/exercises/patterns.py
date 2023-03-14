
# Define Function
def star_pyramid() :
    for x in range(int(input("How many rows of stars would you like?"))) :
        print ("*"*(x+1))

# Call
star_pyramid()

# Define Function
def reverse_star_pyramid() :
    for y in range(int(input("How many rows of stars would you like?")),0,-1) :
        print("*"*y)

# Call
reverse_star_pyramid()