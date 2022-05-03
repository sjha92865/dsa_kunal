#learnings from take u forward,regarding subsequence.
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
arr=[1,2,3]
#arr=[1,2,3]

# def call(ind,arr):
#     global pr
#     print(ind,pr)
#     #print(pr)
#     #print(pr,unpr)
#     if ind==len(arr):
#         print(pr)
#         return
#     pr.append(arr[ind])
#     call(ind+1,arr)
#     pr.pop()
#     call(ind+1,arr)
    
# call(0,arr)  
# def call(ind,pr):
#     #global pr
#     #print(ind,pr)
#     #print(pr)
#     #print(pr,unpr)
#     if ind==len(arr):
#         print("gg",pr)
#         return
#     local_pr=pr.copy()
#     pr.append(arr[ind])
#     call(ind+1,pr)
#     #pr.pop()
#     pr=local_pr
#     #print("local",local_pr)
#     call(ind+1,pr)
    
# call(0,[])  
arr=[3,2,7,5,15,10,66]
def call(ind,pr):
    #global pr
    #print(ind,pr)
    #print(pr)
    #print(pr,unpr)
    if ind>=len(arr):
        print("gg",pr,sum(pr))
        return 0
    local_pr=pr.copy()
    pr.append(arr[ind])
    left=arr[ind]+call(ind+2,pr)
    #pr.pop()
    pr=local_pr
    #print("local",local_pr)
    right=0+call(ind+1,pr)
    return max(left,right)
    
print(call(0,[]) ) 
    
    
    
        

