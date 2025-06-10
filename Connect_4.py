class colours:
    red = "\033[0;31m"
    green= "\033[0;32m"
    end = "\033[0m"
    blue = "\033[0;34m"
    yellow = "\033[1;33m"

print("Select game mode: ")
print(colours.red+"[1]"+colours.end, colours.blue+"- Singleplayer / Multiplayer"+colours.end)
print(colours.red+"[2]"+colours.end, colours.blue+"- Simulation (Hypothesis 1)"+colours.end)
print(colours.red+"[3]"+colours.end,colours.blue+"- Simulation (Hypothesis 2) "+colours.end)
print(colours.red+"[4]"+colours.end,colours.green+"- Simulation and prediction rules. "+colours.end,"\n")

while True:
    x = input("Enter [1],[2],[3] or [4]: \n")
    if x == "1" or x == "2" or x == "3" or x=="4":
        break
x=int(x)
print(colours.green+"Please wait..."+colours.end,"\n")
if x == 1:
    import Connect4_Single_and_Multiplayer
elif x ==2:
    import Connect_4_Hypothesis_1_Simulation
elif x ==3:
    import Connect_4_Hypothesis_2_Simulation
elif x==4:
    print(colours.blue+"Simulation and prediction rules"+colours.end)
    print(colours.green+"When the simultions are run, they will run 2000 games & test 2 Hypotheses."+colours.end)
    print(colours.green+"     1. What if you only played in columns 2,3 & 4"+colours.end)
    print(colours.green+"     2. What if you only played in columns 3,4,5 & 6"+colours.end)
    print(colours.green+"After this you must run the Hypotheses analysis in order to get predictions when you play with a strategy."+colours.end)
    print(colours.red+"* strategies are only playable in singleplayer."+colours.end)