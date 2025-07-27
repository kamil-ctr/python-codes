sides = input("Enter the lengths of the polygon sides separated by spaces: ")
sides = [float(side) for side in sides.split()]
perimeter = sum(sides)
print("The perimeter of the polygon is:", perimeter)
