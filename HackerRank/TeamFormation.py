t = int(raw_input().strip())
for i in xrange(t):
    skills = map(int, raw_input().split())
    n = skills[0]-1
    skills.pop(0)
    skills.sort()
    mini=n+1
    count=1
    for i in xrange(n):
        if skills[i]+1==skills[i+1]:
            count+=1
        else:
            mini=min(count,mini)
            count=1
    mini=min(count,mini)
    print mini
