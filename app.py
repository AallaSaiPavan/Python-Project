print("This is a small game which involves eight players")
print("The rules will be:")
print("There will be an initial number and you as a player has to guess it")
print("There will be three prizes")
print("Players with least difference between initial number and their number will win first prize")
print("Players with second least difference between initial number and their number will win second prize")
print("Players with third least difference between initial number and their number will win third prize")
print("")
print("")
import sys
d=[]
print("Enter actual number")
a=int(input())
print("Enter player number 0's guess")
g0=int(input())
d.append(abs(a-g0))
print("Enter player number 1's guess")
g1=int(input())
d.append(abs(a-g1))
print("Enter player number 2's guess")
g2=int(input())
d.append(abs(a-g2))
print("Enter player number 3's guess")
g3=int(input())
d.append(abs(a-g3))
print("Enter player number 4's guess")
g4=int(input())
d.append(abs(a-g4))
print("Enter player number 5's guess")
g5=int(input())
d.append(abs(a-g5))
print("Enter player number 6's guess")
g6=int(input())
d.append(abs(a-g6))
print("Enter player number 7's guess")
g7=int(input())
d.append(abs(a-g7))
print("")
print("")
for i in range(1,4):
    m=min(d)
    b=[]
    for j in range(len(d)):
        if m==d[j]:
            d[j]=sys.maxsize
            b.append(j)
    print("Place ",i," holders are players with numbers",b)
