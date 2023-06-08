x = input("Do you agree? ")

x = x.lower()
if x in ["y","yes"]:
    print("Agreed.")
elif x in ["n","no"]:
    print("Not agreed.")
else:
    print("Use 'Y' or 'N'")