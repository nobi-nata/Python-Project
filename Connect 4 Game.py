from tkinter import*
from tkinter.messagebox import askquestion
from tkinter.messagebox import showerror
import winsound
first=Tk()
first.title("Connect 4 Game")
first.configure()
lab1=Label(first, text="Enter player 1 name:",bg='orange',font=('Arial Bold',25))
lab1.grid(row=0,column=0)
j1=Entry(first, width=30,bg='light blue',font=('Arial Bold',25))
j1.grid(row=0,column=1)
lab2=Label(first, text="Enter player 2 name:",bg='orange',font=('Arial Bold',25))
lab2.grid(row=1,column=0)
j2=Entry(first, width=30,bg="light blue",font=('Arial Bold',25))
j2.grid(row=1,column=1)
label1=Label(first,text="\n \n \n \n \n",bg='yellow')
label1.grid(row=2,column=0)
label2=Label(first, text="RULES:",bg='salmon',font=('Arial Bold',25))
label2.grid(row=3,column=0)
b1=Button(first, text="START GAME", bg="pale green",font=('Arial Bold',8), command=lambda: startgame())
b1.grid(row=4, column=2)
b2=Button(first, text="QUIT", bg="tomato",font=('Arial Bold',8) ,command=lambda: quitgame())
b2.grid(row=4, column=3)

s=0
def startgame():
    first.wm_state('iconic')
    first.iconify()
    root=Tk()
    root.title('Connect 4 Game')
    root.configure(bg='black')
    a= Button(root, padx=5, pady=10, bg="cyan", text="Button1",font=('Arial Bold',14) ,command=lambda: click(a))
    a.grid(row=0,column=0)
    b= Button(root, padx=5, pady=10, bg="cyan", text="Button2",font=('Arial Bold',14), command=lambda: click(b))
    b.grid(row=0,column=1)
    c= Button(root, padx=5, pady=10, bg="cyan", text="Button3",font=('Arial Bold',14), command=lambda: click(c))
    c.grid(row=0,column=2)
    d= Button(root, padx=5, pady=10, bg="cyan", text="Button4",font=('Arial Bold',14), command=lambda: click(d))
    d.grid(row=0,column=3)
    e= Button(root, padx=5, pady=10, bg="cyan", text="Button5",font=('Arial Bold',14), command=lambda: click(e))
    e.grid(row=0,column=4)
    f= Button(root, padx=5, pady=10, bg="cyan", text="Button6",font=('Arial Bold',14), command=lambda: click(f))
    f.grid(row=0,column=5)
    g= Button(root, padx=5, pady=10, bg="cyan", text="Button7",font=('Arial Bold',14), command=lambda: click(g))
    g.grid(row=0,column=6)
    listofbutton=[a,b,c,d,e,f,g]
    li=[]
    for i in range(1,7):
        lis=[]
        for j in range(7):
            u=Entry(root,bg="white", width=10)
            u.grid(row=i, column=j)
            lis.append(u)
        li.append(lis)
    global s
    s=0
    def click(x):
        i=x.grid_info()["column"]
        global s
        if s==42:
            for i in listofbutton:
                i["state"]="disabled"
            MsgBox = askquestion ("Game over","This game is a draw. Click yes to quit the game. Click no to return to the game board ")
            if MsgBox == 'yes':
               root.destroy()
               first.deiconify()
        if li[0][x.grid_info()["column"]]["bg"]!="blue" and li[0][x.grid_info()["column"]]["bg"]!="red":
            s+=1
        else:
            showerror(title="filled column", message="please click another column to continue the game")
        if s%2!=0:
            j=5
            while j>-1:
                if li[j][i]["bg"]=="white":
                    li[j][i]["bg"]="red"
                    break
                else:
                    j-=1
            p=0
            while p<3:
                n=0
                while n<4:
                    if li[p][n]["bg"]==li[p+1][n+1]["bg"]==li[p+2][n+2]["bg"]==li[p+3][n+3]["bg"]=="red" :
                        li[p][n].config(bg="green")
                        li[p+1][n+1].config(bg="green")
                        li[p+2][n+2].config(bg="green")
                        li[p+3][n+3].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"

                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j1.get()))
                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1
            p=0
            while p<3:
                n=0
                while n<7:
                    if li[p][n]["bg"]==li[p+1][n]["bg"]==li[p+2][n]["bg"]==li[p+3][n]["bg"]=="red" :
                        li[p][n].config(bg="green")
                        li[p+1][n].config(bg="green")
                        li[p+2][n].config(bg="green")
                        li[p+3][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j1.get()))
                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1

            p=0
            while p<6:
                n=0
                while n<4:
                    if li[p][n]["bg"]==li[p][n+1]["bg"]==li[p][n+2]["bg"]==li[p][n+3]["bg"]=="red" :
                        li[p][n+1].config(bg="green")
                        li[p][n+2].config(bg="green")
                        li[p][n+3].config(bg="green")
                        li[p][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j1.get()))

                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1

            p=0
            while p<3:
                n=6
                while n>2:
                    if li[p][n]["bg"]==li[p+1][n-1]["bg"]==li[p+2][n-2]["bg"]==li[p+3][n-3]["bg"]=="red" :
                        li[p+1][n-1].config(bg="green")
                        li[p+2][n-2].config(bg="green")
                        li[p+3][n-3].config(bg="green")
                        li[p][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j1.get()))

                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n-1
                p=p+1
        else:
            j=5
            while j>-1:
                if li[j][i]["bg"]=="white":
                    li[j][i]["bg"]="blue"
                    break
                else:
                    j-=1
            p=0
            while p<3:
                n=0
                while n<4:
                    if li[p][n]["bg"]==li[p+1][n+1]["bg"]==li[p+2][n+2]["bg"]==li[p+3][n+3]["bg"]=="blue" :
                        li[p][n].config(bg="green")
                        li[p+1][n+1].config(bg="green")
                        li[p+2][n+2].config(bg="green")
                        li[p+3][n+3].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j2.get()))

                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1

            p=0
            while p<3:
                n=0
                while n<7:
                    if li[p][n]["bg"]==li[p+1][n]["bg"]==li[p+2][n]["bg"]==li[p+3][n]["bg"]=="blue" :
                        li[p][n].config(bg="green")
                        li[p+1][n].config(bg="green")
                        li[p+2][n].config(bg="green")
                        li[p+3][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j2.get()))

                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1

            p=0
            while p<6:
                n=0
                while n<4:
                    if li[p][n]["bg"]==li[p][n+1]["bg"]==li[p][n+2]["bg"]==li[p][n+3]["bg"]=="blue" :
                        li[p][n+1].config(bg="green")
                        li[p][n+2].config(bg="green")
                        li[p][n+3].config(bg="green")
                        li[p][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j2.get()))

                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n+1
                p=p+1

            p=0
            while p<3:
                n=6
                while n>2:
                    if li[p][n]["bg"]==li[p+1][n-1]["bg"]==li[p+2][n-2]["bg"]==li[p+3][n-3]["bg"]=="blue" :
                        li[p+1][n-1].config(bg="green")
                        li[p+2][n-2].config(bg="green")
                        li[p+3][n-3].config(bg="green")
                        li[p][n].config(bg="green")
                        for i in listofbutton:
                            i["state"]="disabled"
                        MsgBox = askquestion ("Game over","Player {} wins. Click yes to quit the game. Click no to return to the game board ".format(j2.get()))
                        if MsgBox == 'yes':
                           root.destroy()
                           first.deiconify()
                        break
                    else:
                        n=n-1
                p=p+1
    root.mainloop()
def quitgame():
    first.destroy()
first.mainloop()
