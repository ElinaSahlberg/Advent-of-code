into = open(r"C:\Users\elina\OneDrive\Dokument\ett.txt")

gnome = []
foodStock = 0
for line in into:
    if line.strip(' \n') == "":
        gnome.append(foodStock)
        foodStock = 0 
    else:
        foodStock += int(line.strip(' \n'))

sort = sorted(gnome)
print(sort[-1])
print(sum(sort[-3:]))