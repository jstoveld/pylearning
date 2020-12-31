def format_address (address_string):
    number = []
    street = []
    address = address_string.split()

    for x in address:
        number = address[0]
        name = address[1]
        street = ' '.join(address[2::])

        number = str(number)
        road = str(name) + " " + street

        return f"house number {number} on street named {road}"

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"