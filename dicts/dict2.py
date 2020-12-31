file_counts = {"jpeg":10, "txt":14, "csv":2, "py":23} 
for extension in file_counts:
    print(extension)


for ext, amount in file_counts.items():
    print("There are {} files with the  .{} extension.".format(amount, ext))

file_counts.keys()
file_counts.values()


for value in file_counts.values():
    print(value)
