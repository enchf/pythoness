# Yes, you have a module to check for keywords...
import keyword

# And you can obtain the full list for your python installation
for word in keyword.kwlist:
    print(word)

print(keyword.kwlist)