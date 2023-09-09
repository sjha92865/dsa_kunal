# def pattern(r,c):
#     if r==0 :
#         return
#     if c<r:
#         print("*",end='')
#         pattern(r,c+1)
#     else:
#         print()
#         pattern(r-1,0)
'''

*
**
***
****

'''
#2nd pattern
def pattern(r,c):
    if r==0 :
        return
    if r>c:
        pattern(r,c+1)
        print("*",end='')
    else:
        pattern(r-1,0)
        if r!=1:
            print()
#on basis of the same we performed bubble sort. 
def bubble(r,c,arr):
    if r==0 :
        return
    if r>c:
        # print("*",end='')
        if arr[c]>arr[c+1]:
            arr[c+1],arr[c]=arr[c],arr[c+1]
        bubble(r,c+1,arr)
        
    else:
        # print()
        bubble(r-1,0,arr)
 
if __name__=='__main__':
    # v=[5,3,2,4,1]
    # sorting(v)
    # print(v)
    # pattern(4,0)
    arr=[9,5,8,6,2]
    bubble(len(arr)-1,0,arr)
    print(arr)
    
