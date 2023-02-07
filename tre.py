
from difflib import SequenceMatcher

with open(r"C:\Users\elina\OneDrive\Dokument\Advent of Code\tre.txt") as sack:
    for items in sack:
        items = str(items.strip(' \n'))
        lenth = len(items)
        pocket1 = items[:(lenth//2)]
        pocket2 = items[lenth//2:]
        if SequenceMatcher(a=pocket1, b=pocket2).ratio > 0 :
            dert = SequenceMatcher(a=pocket1, b=pocket2).get_matching_blocks()
            value = pocket1[dert[0][0]]
                
    

    