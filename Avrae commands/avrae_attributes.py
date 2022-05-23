embed
<drac2>
#Define variables for later use
rolls = []
attr = []
for i in range(6):
    for j in range(4):
        rolls.append(randint(1,6))
    rolls.pop(rolls.index(min(rolls)))
    attr.append(sum(rolls))
    rolls.clear()
STR = attr[0]
DEX = attr[1]
CON = attr[2]
INT = attr[3]
WIS = attr[4]
CHA = attr[5]
</drac2>
-title "You rolled your attr!"
-desc {STR,DEX,CON,INT,WIS,CHA}
-f "The adventure begins..."
-color
