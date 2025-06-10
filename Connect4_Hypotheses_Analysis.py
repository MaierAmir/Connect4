import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from random import randrange
import csv
import os


if not os.path.exists("connect4 hypothesis 1.csv") and not os.path.exists("connect4 hypothesis 2.csv"):
    print("\033[0;31m"+"Please run BOTH simulation 1 AND 2 before running the analysis."+"\033[0m")
elif not os.path.exists("connect4 hypothesis 1.csv"):
    print("\033[0;31m"+"Please run BOTH simulation 1 AND 2 before running the analysis."+"\033[0m")
elif not os.path.exists("connect4 hypothesis 2.csv"):
    print("\033[0;31m"+"Please run BOTH simulation 1 AND 2 before running the analysis."+"\033[0m")  
else:
    f2 = open('connect4 predictions.csv', mode='w', newline='')
    cs=0
    kl2=1
    kl = 0
    hyp1 = "hypothesis 1"
    hyp2d = "Last 4 columns only"
    hyp2 = "hypothesis 2"
    hyp1d="centre columns only"
    hyp1c="1"
    hyp2c="2"
    c41 = pd.read_csv('connect4 hypothesis 1.csv',header = None)
    c41f= pd.read_csv('connect4 hypothesis 1.csv')
    c4s2= pd.read_csv('connect4 hypothesis 2.csv',header = None)
    c4s2f= pd.read_csv('connect4 hypothesis 2.csv')
    ##################################################wins
    print("Hypothesis 1 analysis:")
    def strat1(strat,stratf,op,hyp,d,hypc):
        global xpm
        global cs
        no = []
        yes=[]
        u=strat.iloc[::1000, :]
        um=strat.iloc[::1000, :]


        x1w=um[1].values
        xpw1=x1w.tolist()
        del xpw1[0]
        xpw=[]
        for i in xpw1:
            
            xpw.append(int(i))

            
        
        print("Player wins =",xpw)
        ########################################moves
        x1m=um[3].values
        xpm1=x1m.tolist()
        del xpm1[0]
        xpm=[]
        for i in xpm1:
            xpm.append(int(i))
            
        print("Player moves =",xpm)
        ###################################################################

        x1c=um[2].values
        xpc1=x1c.tolist()
        del xpc1[0]
        xpc=[]
        for i in xpc1:
            xpc.append(int(i))
            
        print("Computer wins =",xpc)


        ##################################################################names
        def gamefreq():
            global names2
           
            na = strat.iloc[::1000]

            nax=na.loc[:,0]
            names=[]
            for i in nax:
                names.append(i)
            del names[0]

            n1=1
            names2=[]
            nam="test"
            for i in range(len(names)):
                na1 = nam+str(n1)
                n1+=1
                names2.append(na1)
            print("Number of tests =",len(names2))
            print("Total amount of games played =",len(names2)*1000)
        gamefreq()
        #########################################################  averages   
        global leng
        
        leng = len(xpw)*1000

                

        medr=[]
        def truewin(strat):
            global leng
            global winr
            wsum1 = sum(xpw)
            twinrate = (wsum1 / leng) * 100
            winr=round(twinrate,2)
            print("Playerwin rate =",winr,"%")
            medr.append(twinrate)
        truewin(c41)

        def truewinc():
            global leng
            
            wsum2 = sum(xpc)
            twinratec = (wsum2 / leng) * 100
            print("Computer win rate =",round(twinratec,2),"%")
            medr.append(twinratec)
        truewinc()

        def drawchance(stratf):
        #frequency of draw
            global leng
            global freq
            global fcount
            fcount=0
            
            freqcol = stratf.loc[:,"draw"]
            for i in freqcol:
                if i == "yes":
                    fcount+=1
            if fcount>0:
                freq = (fcount/leng)*(100)
                print("Chance of draw =",(freq),"%")
            print("Frequency of draws =",fcount,"draws")
            medr.append(freq)
        drawchance(stratf)       
        ##########################################
        tmsum= sum(xpm)
        avgtm= tmsum / len(xpw)

        ##############################################
        game=[]
        game3=[]
        vardiv =1
        leng2=leng/1000
        for i in range(len(names2)):
            gf= leng2-(leng2-vardiv)
            vardiv+=1
            game.append(gf*1000)
            game3.append(gf)
        game2=[]


        names3=[]
        for i in game3:
            names3.append(i*1000)
        # print(names3)             #no. of games in 1000s

        xv =0

        ###################################################

        if (len(names3) % 2) != 0:
            med1 = (len(names3) / 2)
            median = names3[int(med1)]
            print("median game =",median)
            
        elif (len(names3) % 2) == 0:
            med1 = (len(names3) / 2) -1
            median= names3[int(med1)]+500
            print("median game =",median)
            
        medcols=strat.loc[median+1:median+500:1]

        mcv=medcols[1].values
        mcvm=medcols[3].values
        mcvl=mcv.tolist()
        mcvlm=mcvm.tolist()
        #####################################
        def slope():
            global slopem
            x1cord = randrange(0,500)
            x2cord= randrange(0,500)
            
            x1slope=mcvlm[int(x1cord)]
            y1slope = mcvl[int(x1cord)]
            
            
            x2slope = mcvlm[int(x2cord)]
            y2slope = mcvl[int(x2cord)]
           
            slopey=int(y2slope)-int(y1slope)
            slopex=int(x2slope)-int(x1slope)
            
            slopem1= slopey/slopex
            slopem = round(pow(slopem1,-1))
            print("Average amount of moves played per game(graph2 slope)=",slopem)
            
        slope()
        ###########################################
        co=0
        medw=[]
        ##########################################

        if op == 0:
            print("")
            print("Please close graphs to view Hypothesis 2 analysis.")
        
        
        fig, ax2 = plt.subplots()
        medw.append(fcount)
        ne="Player","Computer","Draws"
        ax2.pie(medr,labels=ne,autopct="%1.1f%%")
        ax2.set_title(("(Graph1) Winrate and Chance of Draw, Using",hyp,d))

        fig, ax = plt.subplots()

        ax.plot(mcvl,mcvlm)

        ax.set_xlabel('Wins')   ############ CHANGE TO TOTAL WINS AGAINST TOTAL MOVES
        ax.set_ylabel('Moves')
        ax.set_title(("(Graph2) Number of moves and wins using",hyp,"Slope used for Average number of moves"))

        myLocator = mticker.MultipleLocator(100)
        ax.xaxis.set_major_locator(myLocator)
        ax.yaxis.set_major_locator(myLocator)
        plt.show()
        
        row=[]

        header = "Hypothesis","Player winrate","Chance of draws","Average moves needed to win"
        row.append(hypc)
        row.append(winr)
        row.append(round(freq,3))
        row.append(int(slopem))
        if cs==0: 
            write = csv.writer(f2)
            write.writerow(header)
            write.writerow(row)
            cs+=1
        else:
            write = csv.writer(f2)
     
            write.writerow(row)
            

    strat1(c41,c41f,kl,hyp1,hyp1d,hyp1c)
    print("")
    print("Hypothesis 2 analysis:")
    strat1(c4s2,c4s2f,kl2,hyp2,hyp2d,hyp2c)
    f2.close()
