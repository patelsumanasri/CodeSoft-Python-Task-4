import tkinter
import random
r=tkinter.Tk()
r.geometry("500x400")
r.minsize(500,400)
r.maxsize(500,400)
r.title("Rock Paper Scissor")
r.config(bg="darkblue")

roundd=0
myscore=0
comscore=0


def clear_window(i):
    # Destroy all widgets in the window
    for widget in r.winfo_children():
        widget.destroy()

    #print("all clear")
    if i==1:                      # means loading window has cleared, next window round to enter number of rounds 
        r.after(500,round)
        
    elif i==2:                    # means round window has cleared after round selection, next window game_start
        game_start()

    elif i==3:                    # means no rounds left, next window ending to show result and play again option
        ending()
    else:                         # means user select to play again, next window round to enter number of rounds
        r.after(500,round)
        
    
    
    
                                # function to show result and option to play again o quit the game #
                                #==================================================================#
def ending():
    global myscore,comscore
    result="GAME DRAW"                            # initial result is draw
    if myscore > comscore:                        # You won
        result="YOU WON"                          # update result
    elif comscore > myscore:                      # You lose
        result="YOU LOSE"                         # update result
        
    f1=tkinter.Frame(r,bg="blue",padx=10,pady=10)                                            # frame in which other widget are pack
    
    l=tkinter.Label(f1,text=result,bg="darkblue",fg="yellow",font=("Roman",30,"bold"))       # label to show result
    l.pack()
    
    b1=tkinter.Button(f1,text="PLAY AGAIN",bg="orange",command=lambda:clear_window(4))       # button to play again, clear_window function will call and else condition will run that is call round window 
    b1.pack(pady=8)
    b2=tkinter.Button(f1,text="QIUT",fg="yellow",bg="red",command=quit)                      # button to quit the game
    b2.pack()
    
    f1.pack(pady=120)      
    
                                        # function to turn #
                                        #==================#
def turn(i,myscoredigit,comscoredigit,roundleft,buttons):    # i is image nuber 
    
    global roundd,myscore,comscore
    
    roundd=int(roundvar.get())
    roundd-=1                                  # minus 1 from roundd to decrease number of rounds
    roundvar.set(str(roundd))
    
    img=None
    if i==1:                                   # user press button 1 which is rock
        img=image1
    elif i==2:                                 # user press button 2 which is paper
        img=image2
    else:
        img=image3                             # user press button 2 which is scissor

    com=random.randrange(1,4)                 # generate random number for computer between 1 to 3
    

    comimage=None
    if com==1:                                 # computer select image 1 which is rock
        comimage=image1
    elif com==2:                               # computer select image 1 which is paper
        comimage=image2
    else:
        comimage=image3                        # computer select image 1 which is scissor


        # when user press button image, 2 images will show on screen, one of user select 2nd of computer that is generate with random number
    f=tkinter.Frame(r,bg="darkblue")            # frame to pack other widgets in it
    
    computer=tkinter.Label(f,image=comimage,text="Computer",compound=tkinter.TOP,bg="blue",fg="yellow",font=("Roman",10))    # randomly selected image along with text "computer"
    computer.grid(row=0,column=0,pady=5)

    vs=tkinter.Label(f,text="VS",bg="blue",fg="yellow",font=("Roman",10))                       # vs
    vs.grid(row=1,column=0,pady=5)
    
    you=tkinter.Label(f,image=img,text="You",compound=tkinter.TOP,bg="blue",fg="yellow",font=("Roman",10))             # user selected image along with text "you"
    you.grid(row=2,column=0,pady=5)

    f.pack(side="bottom")                               
    
    roundleft.config(text=f"round left: {roundd}")     # update round left label widget
    
    if i==com:                                         # if same no body will get the point
        pass
    elif (i==1 and com==3) or (i==2 and com==1) or (i==3 and com==2):    # rock > scissor or paper > rock or scissor > paper----- you will get the points
        myscore+=1
        myscoredigit.config(text=myscore)              # update myscoredigit label widget
        
    else:                                              # otherwise computer will get the point
        comscore+=1
        comscoredigit.config(text=comscore)            # update comscoredigit label widget

    #print("after turn round left: ",roundd)
    for button in buttons:                             # disabled all button after pressing for 1 second
        button.config(state=tkinter.DISABLED)
        
    state=buttons[0].cget('state')
    if state=="disabled":                              # button state is disabled
        #print("yes state is disabled")
        r.after(1000,lambda:clear_window(2))           # call the clear_window function to destry all the widgets and again call the game_start function to create new window so that buttons and every thing comes to its normal state
        
    if roundd<=0:                                      # no rounds left
        r.after(1000,lambda:clear_window(3))           # call the clear window function to destry all the widgets
        
        
   
    
def game_start():
    global roundd,myscore,comscore

    roundd=int(roundvar.get())                  # assign roundvar string value in roundd with int convrsion

                                              # main frame to pack all other widgets
    mainframe=tkinter.Frame(r,bg="darkblue")
                                              
    f=tkinter.Frame(mainframe,bg="blue")       # frame in which buttons are packed and their text, when any button will press turn function will call
    
    b1=tkinter.Button(f,image=image1,command=lambda: turn(1,myscoredigit,comscoredigit,roundleft,[b1,b2,b3]))       # rock image button
    b1.grid(row=0,column=0,padx=5)
    l1=tkinter.Label(f,text="Rock",bg="darkblue",fg="yellow",font=("Roman",12))                                     # rock label text
    l1.grid(row=1,column=0)
    
    b2=tkinter.Button(f,image=image2,command=lambda: turn(2,myscoredigit,comscoredigit,roundleft,[b1,b2,b3]))       # paper image button
    b2.grid(row=0,column=1,padx=5)
    l1=tkinter.Label(f,text="Paper",bg="darkblue",fg="yellow",font=("Roman",12))                                    # paper label text
    l1.grid(row=1,column=1)
    
    b3=tkinter.Button(f,image=image3,command=lambda: turn(3,myscoredigit,comscoredigit,roundleft,[b1,b2,b3]))       # scissor image button
    b3.grid(row=0,column=2,padx=5)
    l1=tkinter.Label(f,text="Scissor",bg="darkblue",fg="yellow",font=("Roman",12))                                  # scissor label text
    l1.grid(row=1,column=2)
    
    f.pack(side="bottom",pady=10)     # frame pack

    f2=tkinter.Frame(r,bg="darkblue")                # frame in which my score digit and my score text labels are packed
    myscoredigit=tkinter.Label(f2,bg="darkblue",text=myscore,fg="yellow",font=("Roman",30))
    myscoredigit.grid(row=0,column=0,padx=5)
    myscoretext=tkinter.Label(f2,bg="blue",text="Your\nscore",fg="yellow",font=("Roman",15))
    myscoretext.grid(row=1,column=0,padx=5)
    f2.pack(side="left",pady=50)

    f3=tkinter.Frame(r,bg="darkblue")                # frame in which computer score digit and computer score text labels are packed
    comscoredigit=tkinter.Label(f3,bg="darkblue",text=comscore,fg="yellow",font=("Roman",30))
    comscoredigit.grid(row=0,column=0,padx=5)
    comscoretext=tkinter.Label(f3,bg="blue",text="Computer\nscore",fg="yellow",font=("Roman",15))
    comscoretext.grid(row=1,column=0,padx=5)
    f3.pack(side="right",pady=50)

    roundleft=tkinter.Label(r,text=f"round left: {roundd}",bg="blue",fg="yellow",font=("Ariel",10,"bold"))   # label that will show on top of window to show number of rounds left
    roundleft.pack()
    
    mainframe.pack(side="bottom",fill="x")            # main frame packed
   

                                # function to delete round window #
                                #=================================#
def delete_round():
    global roundd
    
    if not (roundvar.get()).isdigit():              # if given value is not digit, round window will remain
        return
    roundd=int(roundvar.get())  
    if roundd<=0 or roundd>10:                      # if digit exceed or subceed the limit, round window will remain
        return
    
    r.after(500,clear_window(2))                    # if everyhing is okay call the clear_window function with value 2 that will call the game_start window

    
                                # function to toggle colors of game name #                          
def color():
    
    if len(load.get())>=70:             # loading string variable value is 70 or more 
        return
    
    
    col=l.cget("fg")                        # get the current colour of game name text
    
    if col=="red":                          # if it is red change it to green and so on
        l.config(fg="green")
        img.config(image=image2)
    elif col=="lightgreen":
        l.config(fg="pink")
        img.config(image=image3)
    elif col=="pink":
        l.config(fg="lightblue")
        img.config(image=image1)
    elif col=="lightblue":
        l.config(fg="yellow")
        img.config(image=image2)
    else:
        l.config(fg="red")
        img.config(image=image3)
    r.after(200,color)                    # change color after every 200 miliseconds

def loading():
    load.set(load.get()+"|"*random.randrange(1,10))    # generate random number multiple it with "|" character and set it in load string variable
    
    if len(load.get())>=70:                            # loading full
        r.after(500,lambda:clear_window(1))            # call the clear_window function, clear_window will call round window to select number of rounds 
        return
    r.after(100,loading)                               # call loading function to complete load varibale after every 100 mili seconds

                                # function to select round #
                                #==========================#
def round():
    roundvar.set("1")               # initial rounds is 1
    global myscore,comscore
    myscore=0                       # scores are 0
    comscore=0
    f1=tkinter.Frame(r,bg="blue",padx=10,pady=10)
    
    roundlabel=tkinter.Label(f1,text="Number of rounds",bg="blue",fg="yellow",font=("Roman",15,"bold"),justify="center")    # label to show text "number of rounds"
    roundlabel.pack()
    roundentry=tkinter.Entry(f1,text=roundvar,width=4,bg="lightblue")          # entry widget where roundvar string is assign
    roundentry.pack(pady=6)
    
    b1=tkinter.Button(f1,text="START",bg="orange",command=delete_round)        # button to start the game, call the delete_round function
    b1.pack(pady=8)
    b2=tkinter.Button(f1,text="QIUT",fg="yellow",bg="red",command=quit)        # button to quit the game
    b2.pack()

    l=tkinter.Label(f1,text="rounds should be between 1 to 10",bg="darkblue",fg="yellow")    # label widget to shwo text about rounds limit
    l.pack(pady=5)
    
    f1.pack(pady=110)     # frame packed

    
    

    

#============================================================================#  intro

f=tkinter.Frame(r,bg="darkblue")

l=tkinter.Label(f,text="Rock Paper Scissor",fg="yellow",bg="darkblue",font=("Roman", 30,"bold"))       # label widget to show game name
l.grid(row=0,column=0)
# image calling in program
image1=tkinter.PhotoImage(file="rock.png")
image1=image1.subsample(4)
image2=tkinter.PhotoImage(file="paper.png")
image2=image2.subsample(3)
image3=tkinter.PhotoImage(file="scissor.png")
image3=image3.subsample(3)

img=tkinter.Label(f,image=image1,bg="darkblue")                     # label widget to show image
img.grid(pady=10,row=2,column=0)


load=tkinter.StringVar()                                            # string variable for loading
loadentry=tkinter.Entry(f,text=load,fg="yellow",readonlybackground="darkblue",width=20,font=("Roman",10,"bold"),state="readonly")    # entry widget, load assign to it

loadentry.grid(pady=20,row=1,column=0)
f.pack(pady=80)

r.after(500,color)                           # calling color function to toggle colors
r.after(1000,loading)                        # calling loading function to complete loading 

roundvar=tkinter.StringVar()                 # roundvar string variable for rounds


r.mainloop()
