n,k = map(int,raw_input().split())
imp=0
count=0
luck=0
con=[]
for i in xrange(n):
    l,t = map(int,raw_input().split())
    if t==1:
        imp+=1
    con.append((l,t))

con.sort(key=lambda tup:tup[0])

for i in xrange(n):
    if (con[i])[1]==1:
        luck-=(con[i])[0]
        count+=1
        con.pop(i)
        n-=1
    if count==imp-k:
        break

for i in xrange(n):
    luck+=(con[i])[0]

print luck
