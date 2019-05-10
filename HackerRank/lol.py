st='hackerrank'
q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    j=0
    flag=0
    for i in (j,len(s)):
        try:
            j=s.index(st[flag])
            flag+=1
        except ValueError:
            print 'NO'
    
    if flag==9:
        print 'YES'
