l=[2,3,6,7]
#subset,Recursion Subset, Subsequence, String Questions,26:01 timestamp.
def call(pr,unpr):
    local_pr=pr.copy()
    local_unpr=unpr.copy()
    if len(local_unpr)==0:
        print(local_pr)
        return
    take=local_unpr.pop(0)
    temp=local_pr.copy()
    temp.append(take)
    pr=temp
    unpr=local_unpr
    #call(pr,unpr)
    call(temp,local_unpr)
    pr=local_pr
    call(local_pr,unpr)
    #call(pr,unpr)
    
call([],l)
