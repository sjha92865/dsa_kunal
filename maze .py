#1
def countPathsEndofMaze(r,c):
    
    
    if r==1 or c==1:
        return 1
    else:
        return countPathsEndofMaze(r-1,c)+countPathsEndofMaze(r,c-1)
        
    
        
print(countPathsEndofMaze(3,3))
print(countPathsEndofMaze(4,3))

#2
def printPathsEndofMaze(P,r,c):
    
    #whenever we need to print the ans, we take processed and unprocessed,
    #in this we just print the ans when base condition reaches and we are
    #  adding the ans from above calls, root->leaf, leaf pe ans and return nothing.
    #but in countPathsEndofMaze function we are adding the ans from left and right calls
    # and  we got ans at the root.
    # diff is there in both qns.
    if r==1 and c==1:
        print(P)
        return 
    if  c>1:
        printPathsEndofMaze(P+"R",r,c-1)
    if  r>1:
        printPathsEndofMaze(P+"D",r-1,c)
    
    
        
print(printPathsEndofMaze("",3,3))
print(countPathsEndofMaze(4,3))

#3, to be discussed.
def ListprintPathsEndofMaze(L,P,r,c):
    
    
    if r==1 and c==1:
       
        L.append(P)
        
        return L
    if  c>1:
        (ListprintPathsEndofMaze(L,P+"R",r,c-1))
    if  r>1:
        ListprintPathsEndofMaze(L,P+"D",r-1,c)
    return L#line runs for that call when either c>1 or r>1,hence at (3,3)also, which is root.
    
        
print(ListprintPathsEndofMaze([],"",3,3))

#3, another way of writing
def ListprintPathsEndofMaze(P,r,c):
    
    L=[]
    if r==1 and c==1:
        l=[]
       
        l.append(P)
        
        return l
    if  c>1:
        L.extend(ListprintPathsEndofMaze(P+"R",r,c-1))
    if  r>1:
        L.extend(ListprintPathsEndofMaze(P+"D",r-1,c))
    return L
    
        
print(ListprintPathsEndofMaze("",3,3))
#4, includes Diagonal
def ListprintPathsEndofMazeDiagonal(P,r,c):
    
    L=[]
    if r==1 and c==1:
        l=[]
       
        l.append(P)
        
        return l
    if  c>1 and r>1:
        L.extend(ListprintPathsEndofMazeDiagonal(P+"D",r-1,c-1))#Diagonal
    if  c>1:
        L.extend(ListprintPathsEndofMazeDiagonal(P+"H",r,c-1))#Horizontal
    if  r>1:
        L.extend(ListprintPathsEndofMazeDiagonal(P+"V",r-1,c))#Vertical
    return L
    
        
print(ListprintPathsEndofMazeDiagonal("",3,3))

#5, maze that has obstacle.
def ListprintPathsEndofMaze(P,r,c):
    
    L=[]
    if r==1 and c==1:
        l=[]
       
        l.append(P)
        
        return l
    if  c>1 and r>1:
        L.extend(ListprintPathsEndofMaze(P+"D",r-1,c-1))#Diagonal
    if  c>1:
        L.extend(ListprintPathsEndofMaze(P+"H",r,c-1))#Horizontal
    if  r>1:
        L.extend(ListprintPathsEndofMaze(P+"V",r-1,c))#Vertical
    return L
    
        
print(ListprintPathsEndofMaze("",3,3))

#6, 
def pathRestrictions(P,maze,r,c):
    
    #print(r,c)
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(P)
        return
    
    if  maze[r][c]=='F':
        return
    
    if  r<len(maze)-1:
        pathRestrictions(P+"D",maze,r+1,c)
    if  c<len(maze[0])-1:
        pathRestrictions(P+"R",maze,r,c+1)
    
    
maze=[['T','T','T'],['T','F','T'],['T','T','T']]       
print(pathRestrictions("",maze,0,0))

#7,
def allPath(P,maze,r,c):
    
    L=[]
    if r==len(maze)-1 and c==len(maze[0])-1:
        l=[]
        l.append(P)
        #print(P)
        return l
    
    
    if (maze[r][c]!='T'):
        return ''
    maze[r][c]='F'
    
    if  r<len(maze)-1:
        L.extend(allPath(P+"D",maze,r+1,c))# Down
    if  c<len(maze[0])-1:
        L.extend(allPath(P+"R",maze,r,c+1))# Right
    if r>0:    
        L.extend(allPath(P+"U",maze,r-1,c))# Up
    if c>0:
        L.extend(allPath(P+"L",maze,r,c-1))# Left
    
    maze[r][c]='T'
    return L
    
maze=[['T','T','T'],['T','T','T'],['T','T','T']]       
print(allPath("",maze,0,0))
############################################

def minimumPathSum(triangle, n):
    # Write your code here.
    mx=0
    arr=[]
    for i in triangle:
        arr.append(len(i))
    mx=max(arr)
        
        
    for i in range(0,len(triangle)-1):
        while mx-len(triangle[i])!=0:
            triangle[i].append('X')
        
    def call(r,c):
        if r==n-1 :
#             print(r,c,"h")
            return triangle[r][c]
        if triangle[r+1][c+1]=='X':
            return
#         else:
#             p1=p2=1000001
        if r<n-1 :
#                 if triangle[r+1][c]!='X':
#                     print(r,c)
            p1=call(r+1,c)+triangle[r][c]    
        if r<n-1 and c<n-1:
#                 if triangle[r+1][c+1]!='X':
            p2=call(r+1,c+1)+triangle[r][c]    
        return min( p1 , p2)
    return call(0,0)

#another way of above
def minimumPathSum(triangle, n):
    # Write your code here.
    mx=0
    arr=[]
    for i in triangle:
        arr.append(len(i))
    mx=max(arr)
        
        
    for i in range(0,len(triangle)-1):
        while mx-len(triangle[i])!=0:
            triangle[i].append('X')
        
    def call(r,c):
        if r==n-1 :
#             print(r,c,"h")
            return triangle[r][c]
        
        else:

            p1=p2=1000001
            if r<n-1 :
                if triangle[r+1][c]!='X':
                    print(r,c)
                    p1=call(r+1,c)+triangle[r][c]    
            if r<n-1 and c<n-1:
                if triangle[r+1][c+1]!='X':
                    p2=call(r+1,c+1)+triangle[r][c]    
        return min( p1 , p2)
    return call(0,0)


