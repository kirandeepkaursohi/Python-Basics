
fh = open("sample.txt", 'wt')
fh.write("This is a sample text file.\n")
fh.write("It contains multiple lines.")

fh = open("sample.txt", 'r')
content1 = fh.readline()
content2 = fh.readline()

print("Reading file content:")
print(f"Line 1: {content1}",
      f"Line 2: {content2}")

fh.close()
