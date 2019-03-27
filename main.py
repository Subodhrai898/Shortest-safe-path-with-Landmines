
# coding: utf-8

# In[62]:


import random
def shuffle1(n,m,t,M):
    for i in range(t):
        x = random.randint(0, n-1)
        y = random.randint(0,m-1)
        if(x==0 and y==0) or (x==n-1 and y==m-1):
            t+=1
        else:
            M[x][y]=0
    return M
        


# In[63]:

#ALL POSSIBLE MOVES
def possible(x,y,n,m):
    if(x>=0 and x<n and y<m and y>=0):
        return True
    return False


# In[64]:

#SOLVE THE GRAPH USING BFS
def solve(M,n,m):
    closed =[[0]*n for _ in range(m)]
    parent = [[[] for _ in range(n)] for _ in range(m)]
    dt = (n-1,m-1)
    qu = [(0,0),(-1,-1)]
    parent[0][0].append((-1,-1))
    level=1
    while(len(qu)>1):
        node = qu.pop(0)
        x = node[0]
        y = node[1]
        if(node==(-1,-1)):
            level+=1
            qu.append((-1,-1))
            continue
        if(node==dt):
            print("found ")
            break
        
        if(possible(x,y-1,n,m) and M[x][y-1]!=0 and closed[x][y-1]!=1):
            qu.append((x,y-1))
            closed[x][y-1]=1
            parent[x][y-1].append(node)
        
        if(possible(x,y+1,n,m) and M[x][y+1]!=0 and closed[x][y+1]!=1):
            qu.append((x,y+1))
            closed[x][y+1]=1
            parent[x][y+1].append(node)
        
        if(possible(x-1,y,n,m) and M[x-1][y]!=0 and closed[x-1][y]!=1):
            qu.append((x-1,y))
            closed[x-1][y]=1
            parent[x-1][y].append(node)
        
        if(possible(x+1,y,n,m) and M[x+1][y]!=0 and closed[x+1][y]!=1):
            qu.append((x+1,y))
            closed[x+1][y]=1
            parent[x+1][y].append(node)
    else:
        return [False]
    x=n-1
    y=m-1
    
    M[n-1][m-1]=3
    while(True):
        node = parent[x][y][0]
        x = node[0]
        y = node[1]
        if(x==-1 and y==-1):
            break
        M[x][y]=3
    return [True , level,M]
    
    


# In[55]:





# In[65]:

#CLASS TO DRAW GRID
class DrawGrid:
    def __init__(self,canvas,r,c,d):
        self.c = canvas
        self.r=r
        self.y=c
        self.d=d;
        
    def draw(self,n,m,M):
        d = self.d
    
        for i in range(n):
            for j in range(m):
                p='red'
                s='black'
                if(M[i][j]==1):
                    s='white'
                if(M[i][j]==3):
                    s='blue'
                self.c.create_rectangle(self.r+d*j,self.y+d*i,self.r+d*(j+1),self.y+d*(i+1), outline=p, fill=s)
                
                
        
                


# In[112]:


def gameshuffle2():
    global M
    global c
    global n
    global m
    global mines
    c.delete('all')
    M = [[1]*n for _ in range(m)]
    M = shuffle1(n,m,mines,M)
    g = DrawGrid(c,100,50,25)
    g.draw(n,m,M)
    


# In[115]:


def gamesolve2():
    global M
    global c
    global n
    global m
    result = solve(M,n,m)
    if(result[0]):
        print("Found at ",result[1])
        M = result[2]
        
        c.create_text(100+25*n+200,150,fill="white",font="Times 30 italic bold",
                        text="FOUND")
        c.create_text(100+25*n+200,200,fill="white",font="Times 30 italic bold",
                        text="steps "+str(result[1]))
    else:
        print("Not Found")
        c.create_text(100+25*n+200,150,fill="red",font="Times 30 italic bold",
                        text="NOT FOUND")
    
    g = DrawGrid(c,100,50,25)
    g.draw(n,m,M)

    


# In[116]:


from tkinter import *
root=Tk()

root.resizable(False, False)
root.title("Game")
global M      #Matrix
global c      #canvas reference
global n      #row
global m      #column
global mines  #total mines
c = Canvas(root,height='600',width='950',bg='green')
n=20    #change value
m=20    #change value
mines = 130 #change value
c.pack()
frame = Frame(root)
frame.pack()
B = Button(frame, text ="  Shuffle  ", command=gameshuffle2)
B.pack(side=LEFT)
Button(frame,text='  Solve ',command=gamesolve2).pack(side=RIGHT)
root.mainloop()

