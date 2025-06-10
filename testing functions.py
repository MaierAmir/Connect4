print("Email function test:")
def emailcheck():
    emails=["t",".test@com","test@gmail","test@gmail.com","gmail.com",".com","test@","test123@outlook.ie","@","."]
    for p1 in emails:
        em = 0
        emc=0
        invalid=0
        while em ==0:
            invalid+=1
            if invalid>1:
                print("invalild")
                break
        
            for i in p1: 
                if i == "@":
                    emc+=1
                else:
                    em += 0
                  
                    if i == ".":
                        emc+=1
                    else:
                        em +=0
                           
                if emc == 2:
                    em = 1

        if emc > 1:
            print("Valid")
    return p1
p1=emailcheck()
print("")
################################################################################################################
print("Draw function test:")

X="X"
S="S"

rows = [[[0],[0],[0],[0],[0],[0],[0]],[X,X,X,X,X,X,X],[S,S,S,S,S,S,S],[X,S,S,X,X,S,S],[X,[0],S,X,[0],S,S]]

def Draw():
    for r1 in rows:
        co =0
        for i in r1:
            
            if i == [0]:
                co +=1
        if co == 0:
            print("Draw")
        else:
            print("No draw")
Draw()
print("")
####################################################################################

def horzcheck(player,b1,b2):
    global h
    print("Horizontal win check function test for",player,":")
    h=0
    
    global rows
    def horz(k,b1,b2):
            global X
            global h
            for i in k:
                if i ==b1 or i==b2:
                    h+=1
                    e = k.index(i)
                    
                    if e == 2:
                        if k[e] == b1 and k[e+1]==b1 and k[e+2]==b1 and k[e+3]==b1:
                            print("Horizontal winner found")
                            break
                        else:
                            print("No winner")
                            break
                            

                    elif e >= 4:
                        if k[e] == b1 and k[e-1]==b1 and k[e-2]==b1 and k[e-3]==b1:
                            print("Horizontal winner found")
                            break
                        else:
                            print("No winner")
                            break

                    else:
                    
                        if k[e] == b1 and k[e+1]==b1 and k[e+2]==b1 and k[e+3]==b1:                       
                            print("Horizontal winner found")
                            break
                        else:
                            print("No winner")
                            break
                
            if h==0:
                print("no winner")
    for d in rows:
        horz(d,b1,b2)
horzcheck("X",X,S)
print("")
horzcheck("S",S,X)