from tkinter import *
import tkinter.messagebox as tm
root=Tk()
root.geometry("800x800")
root.minsize(200,200)
y=""
x=0
player1=[]
player2=[]
def def_sigh(number):
      global x,y
      global playerx,playery
      from itertools import permutations
      s1=permutations([1,2,3])
      s2=permutations([3,5,7])
      s3=permutations([1,5,9])
      s4=permutations([4,5,6])
      s5=permutations([7,8,9])
      s6=permutations([1,4,7])
      s7=permutations([2,5,8])
      s8=permutations([3,6,9])
      for i  in s1,s2,s3,s4,s5,s6,s7,s8:
          for j in list(i):
              p1=all(elms in player1 for elms in j)
              p2=all(elms in player2 for elms in j)
              if p1==True:
                  tm.showinfo("Game Result","Player1 wins")
                  break
              elif p2==True:
                  tm.showinfo("Game Result","Player2 wins")
                  break
              else:
                  pass
      if number==1:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b1.config(text=y)
          x+=1
      if number==2:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b2.config(text=y)
          x+=1
      if number==3:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b3.config(text=y)
          x+=1
      if number==4:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b4.config(text=y)
          x+=1
      if number==5:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b5.config(text=y)
          x+=1
      if number==6:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b6.config(text=y)
          x+=1
      if number==7:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b7.config(text=y)
          x+=1
      if number==8:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b8.config(text=y)
          x+=1
      if number==9:
          if x%2==0:
              y="X"
              player1.append(number)
              print(player1)
          else:
              y="O"
              player2.append(number)
              print(player2)
          b9.config(text=y)
          x+=1



l1=Label(root,text="Player1:X",font="times 15")
l1.grid(row=0,column=1)
l2=Label(root,text="Player2:O",font="times 15")
l2.grid(row=0,column=2)
b1=Button(root,width=20,height=10,command=lambda:def_sigh(1))
b1.grid(row=1,column=0)
b2=Button(root,width=20,height=10,command=lambda:def_sigh(2))
b2.grid(row=1,column=1)
b3=Button(root,width=20,height=10,command=lambda:def_sigh(3))
b3.grid(row=1,column=2)
b4=Button(root,width=20,height=10,command=lambda:def_sigh(4))
b4.grid(row=2,column=0)
b5=Button(root,width=20,height=10,command=lambda:def_sigh(5))
b5.grid(row=2,column=1)
b6=Button(root,width=20,height=10,command=lambda:def_sigh(6))
b6.grid(row=2,column=2)
b7=Button(root,width=20,height=10,command=lambda:def_sigh(7))
b7.grid(row=3,column=0)
b8=Button(root,width=20,height=10,command=lambda:def_sigh(8))
b8.grid(row=3,column=1)
b9=Button(root,width=20,height=10,command=lambda:def_sigh(9))
b9.grid(row=3,column=2)



root.mainloop()