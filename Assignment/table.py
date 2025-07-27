registration_numbers = [
    "23BCE10029", "23BCE10030", "23BCE10031", "23BCE10032", "23BCE10033",
    "23BCE10034", "23BCE10035", "23BCE10036", "23BCE10037", "23BCE10038"
]

names = [
    "Joe", "Alice", "Bob", "Charlie", "David", 
    "Eva", "Frank", "Grace", "Helen", "Ivy"
]

print(f"{'Registration Number':<20}{'Name':<10}")
print('-' * 30)

for reg_num, name in zip(registration_numbers, names):
    print(f"{reg_num:<20}{name:<10}")