from random import randrange
import os
import csv
import pandas as pd


class colours:
    red = "\033[0;31m"
    green= "\033[0;32m"
    end = "\033[0m"
    blue = "\033[0;34m"
    yellow = "\033[1;33m"

print(colours.blue+"Connect"+colours.end,colours.red+"4"+colours.end)
if not os.path.exists("connect4 predictions.csv"):
    print(colours.red+"No previous hypotheses data, please run simulation and analysis for game hypotheses predictions first."+colours.end)
    predr=1
else:
    pred= pd.read_csv('connect4 predictions.csv')
    predr=0
def emailcheck():
    em = 0
    global p1
    while em==0:
        p1 = input("Enter player 1 email: ")
        si = p1.find("@")
        di = p1.find(".")
        if si > 0 and di > si:
            un = p1[:si]
            dmn = p1[si+1:di]
            ext = p1[di+1:]
            if len(un) >= 3 and len(dmn) >= 3 and len(ext) >= 2:
                em=1
   
emailcheck()

while True:
    multi = input("enter [0] for singleplayer or [1] for multiplayer: ")
    if multi == "0" or multi=="1":
        break
        
multi = int(multi)
if multi == 0:
    cname = "Computer"
else:     
    def emailcheck2():
        em = 0
        global cname
        while em==0:
            cname = input("Enter player 2 email: ")
            si = cname.find("@")
            di = cname.find(".")
            if si > 0 and di > si:
                un = cname[:si]
                dmn = cname[si+1:di]
                ext = cname[di+1:]
                if len(un) >= 3 and len(dmn) >= 3 and len(ext) >= 2:
                    em=1
   
    emailcheck2()

req1=False
req3=False
strat=""
req=""
strat2=""
req2=""
def strategy(stratv,request,request2):
    
    global pred
    global redr
    global swin

    while request2 == False:
        while True:
            request= input("Do you wish to play with a strategy?, enter [1] for yes or [0] for none:")
            if request == "1" or request =="0":
                break
        request = int(request)
      
        if request == 1 or request == 0:
            request2=True
        else:
            pass
    if request==1:
        while True:
            stratv=input("Enter [1] for strategy 1(Only play in centre columns), or [2] for strategy 2(Only play in last 4 cloumns):")
            if stratv == "1" or stratv=="2":
                break
        stratv=int(stratv)
        if predr ==0:
            if stratv==1 and predr==0:
                prow=pred.loc[pred["Hypothesis"] == 1]
                
                swin=prow.iloc[0]['Player winrate']
                sdr=prow.iloc[0]["Chance of draws"]
                sam=prow.iloc[0]["Average moves needed to win"]
                print("")
                print(colours.green+"You have chosen strategy 1."+colours.end)
                print("This strategy has a",colours.green+str(swin)+colours.end,"% predicted win rate.")
                print("It takes an average of",colours.green+str(sam)+colours.end,"moves needed to win.")
                print("It has a",colours.green+str(sdr)+colours.end,"% predicted chance of draw. \n")


            elif stratv == 2 and predr==0:
                prow=pred.loc[pred["Hypothesis"] == 2]
                swin=prow.iloc[0]['Player winrate']
                sdr=prow.iloc[0]["Chance of draws"]
                sam=prow.iloc[0]["Average moves needed to win"]
                print("")
                print(colours.green+"You have chosen strategy 2."+colours.end)
                print("This strategy has a",colours.green+str(swin)+colours.end,"% predicted win rate.")
                print("It takes an average of",colours.green+str(sam)+colours.end,"moves needed to win.")
                print("It has a",colours.green+str(sdr)+colours.end,"% predicted chance of draw. \n")
            elif predr==1:
                pass
    else:
        

    
        stratv=0
    
    return stratv,request,request2
    

if multi == 0:
    stratv,request,request2=strategy(strat,req,req1)
    req = request
    strat = stratv
else:
    req = 0
    
    
    
    
m = 0
cm = 0
pw = 0
cw = 0
dc=0
r1 = [[0],[0],[0],[0],[0],[0],[0]]
r2 = [[0],[0],[0],[0],[0],[0],[0]]
r3 = [[0],[0],[0],[0],[0],[0],[0]]
r4 = [[0],[0],[0],[0],[0],[0],[0]]
r5 = [[0],[0],[0],[0],[0],[0],[0]]
r6 = [[0],[0],[0],[0],[0],[0],[0]]
key ="  0    1    2    3    4    5    6   " 
def board():

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(key)
    print("")


go = False


pw=0
cw=0
X = "X"
S="S"
board()
print(p1, colours.green+"counter = X"+colours.end)
print(cname,colours.green+"counter = S"+colours.end)

while go == False:

    def Draw():
        global dc
        global go
        co =0
        for i in r1:
            if i == [0]:
                co +=1
        if co == 0:
            print(colours.red+"NO WINNER, DRAW"+colours.end)
            dc+=1
            go = True
    Draw()
    t=0

 

    inp=0
    
    x=0
    def colfull(requestc,stratc,position,name):
        v = 0
        v2 = 0
        og = name,"Enter which column you wish to drop counter:"
        og1 = cname," ,Enter which column you wish to drop counter:" 
        rego = "That column is full, please choose another:"
        global x
        global cx
        global inp
        if inp ==0:
            pr =name,"enter [2],[3] or [4], to drop counter:"
            pr1 = name,"enter [3],[4],[5] or [6], to drop counter:"
        else:
            pr=name,"enter which column you wish to drop counter:"
        
        reqc=False
        if requestc==1:
            if stratc== 1 and inp==0:
                 while reqc==False:
                     while True:
                         position = input(pr)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                     position = int(position)
                     
                     if r1[position] != [0] :
                         print("centre column is full please place elsewhere")
                         
                         if r1[2] != [0] and r1[3] != [0] and r1[4] != [0]:
                             print("center columns are full,strategy is no longer possible, please drop elsewhere.")
                             requestc =0
                             inp+=1
                                                   
                         else:
                             reqc = False
                     elif position != 2 and position!= 3 and position!= 4:
                         if r1[2] != [0] and r1[3] != [0] and r1[4] != [0]:
                             print("center columns are full, please drop elsewhere.")
                             requestc =0
                             inp+=1
                             break
                         else:
                             print("Please enter column 2,3 or 4.")

                     else:
                         reqc=True
            elif stratc== 2 and inp==0:
                 while reqc==False:
                     while True:
                         position = input(pr1)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                     position = int(position)
                     if r1[position] != [0] :
                         print("Last 4 columns are full please place elsewhere")
                         
                         if r1[3] != [0] and r1[4] != [0] and r1[5] != [0] and r1[6]!=[0]:
                             print("Last 4 columns are full,strategy is no longer possible, please drop elsewhere.")
                             requestc =0
                             inp+=1
                             
                         else:
                             reqc = False
                     elif position != 3 and position!= 4 and position!= 5 and position!=6:
                         if r1[3] != [0] and r1[4] != [0] and r1[5] != [0] and r1[6]!=[0]:
                             print("Last columns are full, please drop elsewhere.")
                             requestc =0
                             inp+=1
                             break
                         else:
                             print("Please enter column 3,4,5 or 6.")

                     else:
                         reqc=True
                
            else:
                
                while v == 0:            
                    if v2 == 0:
                        while True:
                             position = input(og)
                             if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                                 break
                        position = int(position)
                        if r1[position] == [0]:
                            v= 1
                        else:
                            v2=1
                            v=0
                    else:
                        while True:
                            position = input(rego)
                            if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                                 break
                        position = int(position)
                        if r1[position] == [0]:
                            v=1
            
        else:    
            while v == 0:            
                if v2 == 0:
                    while True:
                         position = input(og)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                    position = int(position)
                    if r1[position] == [0]:
                        v= 1
                    else:
                        v2=1
                        v=0
                else:
                    while True:
                         position = input(rego)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                    position = int(position)
                    if r1[position] == [0]:
                        v=1
    
        if r1[2] != [0] and r1[3] != [0] and r1[4] != [0]:
            while v == 0:            
                if v2 == 0:
                    while True:
                         position = input(og)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                    position = int(position)
                    if r1[position] == [0]:
                        v= 1
                    else:
                        v2=1
                        v=0
                else:
                    while True:
                         position = input(rego)
                         if position == "0" or position == "1" or position == "2" or position == "3" or position == "4" or position == "5" or position == "6":
                             break
                    position = int(position)
                    if r1[position] == [0]:
                        v=1        
    
        return requestc,stratc,position,name    
    if not go:
        requestc,stratc,position,name=colfull(req,strat,x,p1)
    req=requestc
    strat=stratc
    x=position
  
    m+=1
    def pos(j,l):
        if r6[j] == [0]:
            del r6[j]
            r6.insert(j,l)
                        
        elif r5[j] == [0]:
            del r5[j]
            r5.insert(j,l)
            
        elif r4[j] == [0]:
            del r4[j]
            r4.insert(j,l)
            
        elif r3[j] == [0]:
            del r3[j]
            r3.insert(j,l)
            
        elif r2[j] == [0]:
            del r2[j]
            r2.insert(j,l)
            
        elif r1[j] == [0]:
            del r1[j]
            r1.insert(j,l)
    pos(x,X)
    board()

####################################################################### vertical wins
    def wins(b1, o1):
        global go
        global pw
        global cw
        def vert5(b,o1):
            global pw
            global cw
            global go
            if r6[b] == b1 and r5[b] == b1 and r4[b] == b1 and r3[b] == b1:
                print(o1,colours.green+"wins!"+colours.end)
                if o1 == p1:
                    pw+=1
                else:
                    cw+=1
                go = True
                
            else:
                pass
        
        for i in range(0,7):
            vert5(i,o1)    
    #######################################################################
    #vertical win check (r6-r3)
        def vert3(b,o1):
            global pw
            global cw
            global go
            if r4[b] == b1 and r3[b] == b1 and r2[b] == b1 and r1[b] == b1:
                print(o1,colours.green+"wins!"+colours.end)
                if o1 == p1:
                    pw+=1
                else:
                    cw+=1
                go = True
                
            else:
                pass
        for i in range(0,7):
            vert3(i,o1)
    ######################################################################## vert
        def vert4(b,o1):
            global pw
            global cw
            global go
            if r5[b] == b1 and r4[b] == b1 and r3[b] == b1 and r2[b] == b1:
                print(o1,colours.green+"wins!"+colours.end)
                if o1 == p1:
                    pw+=1
                else:
                    cw+=1
                go = True
                
            else:
                pass
        
        for i in range(0,7):
            vert4(i,o1)
    ############################################################### horz
        def horz(k,o1):
          
            global pw
            global cw
            global go
            for i in k:
                if i ==b1:
                    e = k.index(i)
                    
                    if e == 2:
                        if k[e] == b1 and k[e+1]==b1 and k[e+2]==b1 and k[e+3]==b1:
                            print("Game over, ",o1,colours.green+"wins!"+colours.end)
                            if o1 == p1:
                                pw+=1
                            else:
                                cw+=1
                            go = True
                            break
                        break                        
                    
                    
                    
                    elif e >= 4:
                        if k[e] == b1 and k[e-1]==b1 and k[e-2]==b1 and k[e-3]==b1:
                            print("Game over, ",o1,colours.green+"wins!"+colours.end)
                            if o1 == p1:
                                pw+=1
                            else:
                                cw+=1
                            go = True
                            break
                        break
                    
                    else:
                    
                        if k[e] == b1 and k[e+1]==b1 and k[e+2]==b1 and k[e+3]==b1:                       
                            print("Game over, ",o1,colours.green+"wins!"+colours.end)
                            if o1 == p1:
                                pw+=1
                            else:
                                cw+=1
                            go = True
                            break
                        break
        horz(r6,o1)
        horz(r5,o1)
        horz(r4,o1)
        horz(r3,o1)
        horz(r2,o1)
        horz(r1,o1)

    ################################################################################################## dia
        for i in r3:
            if i ==b1:
                e = r3.index(i)
                if e == 3:
                    if r3[e] == b1 and r4[e-1]==b1 and r5[e-2]==b1 and r6[e-3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                    
                    if r3[e] == b1 and r4[e+1]==b1 and r5[e+2]==b1 and r6[e+3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                    
                   
                if e >= 4:
                    if r3[e] == b1 and r4[e-1]==b1 and r5[e-2]==b1 and r6[e-3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                    
                elif e < 3:
                    if r3[e] == b1 and r4[e+1]==b1 and r5[e+2]==b1 and r6[e+3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1                     
                        go = True
                        break
                   
        for i in r2:
            if i == b1:
                e = r2.index(i)
                if e == 3:
                    if r2[e] == b1 and r3[e-1]==b1 and r4[e-2]==b1 and r5[e-3]==b1:    
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                    
                    if r2[e] == b1 and r3[e+1]==b1 and r4[e+2]==b1 and r5[e+3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                  

        for i in r1:
            if i ==b1:
                e = r1.index(i)
                if e == 3:
                    if r1[e] == b1 and r2[e-1]==b1 and r3[e-2]==b1 and r4[e-3]==b1:
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                   
                    if r1[e] == b1 and r2[e+1]==b1 and r3[e+2]==b1 and r4[e+3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                   
                if e >= 4:
                    if r1[e] == b1 and r2[e-1]==b1 and r3[e-2]==b1 and r4[e-3]==b1:                       
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                   
                elif e < 3:
                    if r1[e] == b1 and r2[e+1]==b1 and r3[e+2]==b1 and r4[e+3]==b1:
                        
                        print("Game over, ",o1,colours.green+"wins!"+colours.end)
                        if o1 == p1:
                            pw+=1
                        else:
                            cw+=1
                        go = True
                        break
                 
    wins(X,p1)
###############################################################
    cx=0
    if go == False:
        go = False
        
        if multi == 0:
            vc = 0
            while vc == 0:            
                cx = randrange(0,7)
                if r1[cx] == [0]:
                    vc= 1
                else:
                    vc=0
                cm +=1
        else:
            if not go:
                requestc,stratc,position,name=colfull(req2,strat2,cx,cname)
                req2=requestc
                strat2=stratc
                cx=position
              

            cm+=1
                
        pos(cx,S)
        board()
    wins(S,cname)
######################################################################## (vert checks)

print(p1,colours.blue+"moves = "+colours.end,m)
print(cname,colours.blue+" moves= "+colours.end,cm)

print("")

if req == 1:
    if strat==1:
        strathyp="1"
    elif strat == 2:
        strathyp="2"
else:
    strathyp="0"
    
if req2 == 1:
    if strat2==1:
        strathyp2="1"
    elif strat2 == 2:
        strathyp2="2"
else:
    strathyp2="0"
    

data = ["Player 1 email","Player 2 email","Winner","no. of player 1 moves","no. of player 2 moves", "draw","Hypothesis P1","hypothesis P2"]

def write1():
    global dc
    global pw
    global cw
    global cnaame
    global p1
    global m
    global cm
    global strathyp
    global data

    draw=0
    w=0
    if dc > 0:
        draw = "yes"
    else:
        draw="no"
    if pw>0:
        w = p1
    elif cw>0:
        w=cname
    elif pw ==0 and cw==0:
        w = "No winner"

    row = [p1,cname,w,m,cm,draw,strathyp,strathyp2]

    if not os.path.exists("Connect4 Game.csv"):
        print(colours.red+"Data file not found,"+colours.end, colours.green+"creating new file and uploading data...."+colours.end)
        print(colours.blue+"Please play another game."+colours.end)
        f = open('Connect4 Game.csv', mode='w', newline='')
        write = csv.writer(f)
        write.writerow(data)
        write.writerow(row)
    else:
        f = open("Connect4 Game.csv", mode='a', newline='')
        write = csv.writer(f)   
        write.writerow(row)

    f.close()


if not os.path.exists("Connect4 Game.csv"):
    print(colours.red+"Data file not found,"+colours.end, colours.green+"creating new file and uploading data...."+colours.end)
    f = open('Connect4 Game.csv', mode='w', newline='')
    write = csv.writer(f)
    write.writerow(data)
    f.close()

else:
    
    c4=pd.read_csv("Connect4 Game.csv")

    def winrate(player,strategyv,Hypothesis):
        
        if (c4['Player 1 email'].eq(player)).any() == True or (c4['Player 2 email'].eq(player)).any() == True:
            cemail=c4.loc[c4["Player 1 email"] == player]
            colemail=cemail.loc[cemail[Hypothesis]==int(strategyv)]
            colcount = colemail.loc[:,"Player 1 email"]
            cemail2=c4.loc[c4["Player 2 email"] == player]
            colemail2=cemail2.loc[cemail2[Hypothesis]==int(strategyv)]
            colcount2 = colemail2.loc[:,"Player 2 email"]
            if colemail.empty and colemail2.empty and strategyv == "0":
                print("No previous data for",player,"playing with no strategy yet, please play again, uploading new data...")
            elif colemail.empty and colemail2.empty:
                print("No previous data on this hypothesis yet for ",player,", uploading new data.... Please play another game with the same strategy.")
            elif not colemail.empty and not colemail2.empty:

                count1=0
                count2=0
                wincount1=0
                wincount2=0
                for i in colcount2:
                    count2+=1
                for i in colcount:
                    count1+=1
              
                totalgames=count1+count2
                winner2=colemail2.loc[colemail2['Winner']==player]
                colcountw2 = winner2.loc[:,"Winner"]
                
                winner=colemail.loc[colemail['Winner']==player]
                colcountw = winner.loc[:,"Winner"]
              
                if not winner2.empty:
                    for i in colcountw2:
                        wincount2+=1
                if not winner.empty:
                    for i in colcountw:
                        wincount1+=1
         
                
                wincounter = wincount1 + wincount2
                winrate= (wincounter/totalgames) * 100
                if strategyv == "0":
                    print(player,"'s winrate from previous games, using no strategy =",round(winrate,2),"%")
                elif strategyv == "1":
                    print(player,"'s winrate from previous games, using strategy 1 =",round(winrate,2),"%")
                elif strategyv == "2":
                    print(player,"'s winrate from previous games, using strategy 2 =",round(winrate,2),"%")
               
            elif not colemail.empty:
                count1=0
                wincount1=0
                for i in colcount:
                    count1+=1
                winner=colemail.loc[colemail['Winner']==player]
                colcountw = winner.loc[:,"Winner"]
                if not winner.empty:
                    for i in colcountw:
                        wincount1+=1
                winrate= (wincount1/count1) * 100
                if strategyv == "0":
                    print(player,"'s winrate from previous games, using no strategy =",round(winrate,2),"%")
                elif strategyv == "1":
                    print(player,"'s winrate from previous games, using strategy 1 =",round(winrate,2),"%")
                elif strategyv == "2":
                    print(player,"'s winrate from previous games, using strategy 2 =",round(winrate,2),"%")

                
            elif not colemail2.empty:
                count2=0
                wincount2=0
                for i in colcount2:
                    count2+=1
                winner=colemail2.loc[colemail2['Winner']==player]
                colcountw2 = winner.loc[:,"Winner"]
                if not winner.empty:
                    for i in colcountw2:
                        wincount2+=1
                winrate= (wincount2/count2) * 100
                if strategyv == "0":
                    print(player,"'s winrate from previous games, using no strategy =",round(winrate,2),"%")
                elif strategyv == "1":
                    print(player,"'s winrate from previous games, using strategy 1 =",round(winrate,2),"%")
                elif strategyv == "2":
                    print(player,"'s winrate from previous games, using strategy 2 =",round(winrate,2),"%")
                

            else:
                print(colours.blue+"no data on this hypothesis for",player,", please play again, uploading new data....."+colours.end)
            
        else:
            print(colours.blue+"no data on this hypothesis for", player,", please play again, uploading new data....."+colours.end)
    winrate(p1,strathyp,"Hypothesis P1")
    winrate(cname,strathyp2,"hypothesis P2")
write1() 