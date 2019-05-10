n,m = map(int,raw_input().split())
tree=[]
su=0
vis=[]
for i in range(0,n+1):
    vis.append(i)

for i in xrange(m):
    x,y,r = map(int,raw_input().split())
    a=(x,y,r)
    tree.append(a)

tree=sorted(tree, key=lambda u:u[2])

for k in xrange(m):
    ele=[tup for tup in tree if tup[2] == k]
    for j in xrange(len(ele)):
        if vis[(ele[j])[0]] == vis[(ele[j])[1]]:
            pass
        else:
            su = su + (ele[j])[2]
            print ele
            print su
            mini= min(vis[(ele[j])[0]],vis[(ele[j])[1]])
            maxi= max(vis[(ele[j])[0]],vis[(ele[j])[1]])
            for i in xrange(n+1):
                if vis[i]==maxi:
                    vis[i]=mini
                                   
print su
