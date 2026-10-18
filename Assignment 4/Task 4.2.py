"""fh = open("output.txt", 'xt')
fh.close()"""

with open("output.txt", 'w') as fh:
    line1 = input("Enter text to write to the file:")
    fh.write(line1 + "\n")
    print("Data successfully written to output.txt." + "\n")

with open("output.txt", 'a') as fh:
    line2 = input("Enter additional text to append:")
    fh.write(line2 + "\n")
    print("Data successfully appended to output.txt." + "\n")


print("\nFinal content of the output.txt")
with open("output.txt", 'r') as fh:
    print(fh.read())

