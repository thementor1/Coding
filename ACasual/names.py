import sys

names = ["bill", "charlie", "fred", "george", "ginny", "percy", "ron"]

name = input("Name: ")

name = name.lower()

if name in names:
    print("Name found")
    sys.exit(0)

print("Name NOT found!")
sys.exit(1)