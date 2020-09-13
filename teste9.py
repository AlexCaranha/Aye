
colours = ["Red", "Green", "Blue", "Black", "White", "Orange", "Yellow"]

print(any("a" in c for c in colours))

print(all("a" in c for c in colours))

output1 = next(c for c in colours if c.startswith("G"))
print(output1)

output = next(c for c in colours if c.startswith("A"))
print(output)

