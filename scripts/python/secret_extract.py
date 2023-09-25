import sys

abc = sys.argv[1]

print("Printing secret now...")
# abc length:
print("Length: " + str(len(abc)))
for letter in abc:
    print("Letter: " + letter)