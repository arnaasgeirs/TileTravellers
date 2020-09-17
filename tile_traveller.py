#Við höfum hefur leikborð sem er 3x3  
#Gefið er hvar leikmaður byrjar í 1,1 á leikborði
#Forrit tilkynnir leikmanni hvert hann getur ferðast 
#leikmaður velur, forrit tekur val, ef það er ógild átt, er það tilkynnt
#ef valið er gilt, tilkynnir forrit hvert hann getur ferðast næst

x = 1
y = 1

if_won = False

#direction = input("You can travel: (N)orth.")

def direction(x,y):
    if x == 1 and y == 1:
    result = "You can travel: (N)orth."
    return result

if move == "N" or move == "n":
    move = input("You can travel: (N)orth or (E)ast or (S)outh.")
else:
    print("Not a valid direction!")

#fall sem tékkar hvort unnið

while not if_won:
    #tékkar direction
    #input("")
else:
    print("Victory")


"""