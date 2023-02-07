sheat = open(r"C:\Users\elina\OneDrive\Dokument\Advent of Code\två.txt")
summ = 0
#a sten   x loose
#b papper y draw
#c sax    z  win

for battle in sheat:
    
    if battle == 'A X\n':
        summ += 0 + 3
    elif battle == 'A Y\n':
        summ += 3 + 1
    elif battle == 'A Z\n':
        summ += 6 + 2 
        
    elif battle == 'B X\n':
        summ += 0 + 1
    elif battle == 'B Y\n':
        summ += 3 + 2
    elif battle == 'B Z\n':
        summ += 6 + 3
        
    elif battle == 'C X\n':
        summ += 0 + 2
    elif battle == 'C Y\n':
        summ += 3 + 3
    elif battle == 'C Z\n':
        summ += 6 + 1
    else:
        print(battle)
        
answ = summ + 6 + 2

sheat.close
