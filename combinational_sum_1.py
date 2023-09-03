def abc():
  #gfg ka hai.
  #wahi take and not take but elements can be picked any no of times so,ind+1 nhi kra hai.
  # but pick krne se pehle yeh jarur dekhna hai ki element to be picked should be smaller than the target.
        # 5
        # 8 1 8 6 8
        # 12
        # wouldn't pass for above case without set thing.
        A=list(set(A))
        n=len(A)
        # print(A)
        A.sort()
        ans=[]
        def foo(ind,tar,ds):
            
            if ind==len(A):
                if tar==0:
                    ans.append(ds[:])
                return
            if tar>=A[ind]:
                ds.append(A[ind])
                tar=tar-A[ind]
                foo(ind,tar,ds)#take
                ds.pop()
                tar=tar+A[ind]
            foo(ind+1,tar,ds)#not take
        foo(0,B,[])
        return ans
