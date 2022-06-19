# import library
from tkinter import *
import tkinter

# import mô hình
import pickle
bet365modelHome = pickle.load(open('modelSav/modelHomeWinWithBet365.sav', 'rb'))
blueSquaremodelHome = pickle.load(open('modelSav/modelHomeWinWithBlueSquare.sav', 'rb'))


# tạo hàm
def bet365model():
    B365H = float(entry1.get())
    B365D = float(entry2.get())
    B365A = float(entry3.get())
    predicted_Home=bet365modelHome.predict([[B365H,B365D,B365A]])
    lbl.config(text='Kết quả nhà cái Bet365= '+str(predicted_Home))

def blueSquare():
    B365H = float(entry4.get())
    B365D = float(entry5.get())
    B365A = float(entry6.get())
    predicted_Home=blueSquaremodelHome.predict([[B365H,B365D,B365A]])
    lbl.config(text='Kết quả nhà cái Blue Square= '+str(predicted_Home))

# Create a window
win=Tk()
#set title for the window
win.title("Dự báo điểm bàn thắng của đội nhà")
#set the geometry of the window
win.geometry("1000x400") # ngang x dọc

# B365
#create an entry widget
# ----- entry1 -----
lbl1=Label(win,text="Tỷ lệ thắng của đội nhà theo B365")
lbl1.grid(column=0,row=0)
entry1=Entry(win,width=20)
entry1.grid(column=0,row=1)

# ----- entry2 -----
lbl2=Label(win,text="Tỷ lệ hoà của 2 đội theo B365")
lbl2.grid(column=2,row=0)
entry2=Entry(win,width=20)
entry2.grid(column=2,row=1)

# ----- entry3 -----
lbl3=Label(win,text="Tỷ lệ thắng của đội khách theo B365")
lbl3.grid(column=4,row=0)
entry3=Entry(win,width=20)
entry3.grid(column=4,row=1)

#create a button to display the text of entry
button1=Button(win, text="Dự báo điểm thắng thua theo B365",borderwidth=0,bg = 'blue',fg='white',command=bet365model)
button1.grid(column=5,row=1)



# Blue Square

# ----- entry4 -----
lbl4=Label(win,text="Tỷ lệ thắng của đội nhà theo Blue Square")
lbl4.grid(column=0,row=2)
entry4=Entry(win,width=20)
entry4.grid(column=0,row=3)

# ----- entry5 -----
lbl5=Label(win,text="Tỷ lệ hoà của 2 đội theo Blue Square")
lbl5.grid(column=2,row=2)
entry5=Entry(win,width=20)
entry5.grid(column=2,row=3)

# ----- entry6 -----
lbl6=Label(win,text="Tỷ lệ thắng của đội khách theo Blue Square")
lbl6.grid(column=4,row=2)
entry6=Entry(win,width=20)
entry6.grid(column=4,row=3)


#create a button to display the text of entry
button2=Button(win, text="Dự báo điểm thắng thua theo Blue Square",borderwidth=0,bg = 'blue',fg='white',command=blueSquare)
button2.grid(column=5,row=3)



lbl=Label(win,text="", font=('Century 12 bold'))
lbl.grid(row=4,sticky="w")

win.mainloop()