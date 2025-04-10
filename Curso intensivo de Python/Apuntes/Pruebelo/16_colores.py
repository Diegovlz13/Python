colors = [
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "black",
    "white",
    "gray",
    "orange",
    "purple",
    "pink",
]

print(colors)
colors.append("brown")
print(colors)
colors.insert(0, "violet")
print(colors)
del colors[3]
print(colors)
colors.pop()
print(colors)
colors.pop(5)
print(colors)
colors.remove("pink")
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
print(sorted(colors))
print(sorted(colors, reverse=True))
print(colors)
colors.reverse()
print(colors)
print(len(colors))



