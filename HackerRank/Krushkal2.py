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

for j in xrange(len(tree)):
    if vis[(tree[j])[0]] == vis[(tree[j])[1]]:
        pass
    else:
        su = su + (tree[j])[2]
        print tree
        print su
        mini= min(vis[(tree[j])[0]],vis[(tree[j])[1]])
        maxi= max(vis[(tree[j])[0]],vis[(tree[j])[1]])
        for i in xrange(n+1):
            if vis[i]==maxi:
                vis[i]=mini
print vis                                   
print su
